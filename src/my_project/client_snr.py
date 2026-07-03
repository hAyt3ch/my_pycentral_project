import argparse
import json
import os
from typing import Any, Optional

from pycentral import NewCentralBase
from pycentral.new_monitoring.clients import Clients


SNR_KEYS = (
    "signalToNoiseRatio",
    "signal_to_noise_ratio",
    "snr",
    "SNR",
    "signalNoiseRatio",
)


def extract_snr(payload: dict[str, Any]) -> Optional[float]:
    """Return the first SNR-like value found in a client payload."""
    if not isinstance(payload, dict):
        return None

    for key in SNR_KEYS:
        value = payload.get(key)
        if value is not None:
            return float(value)

    for value in payload.values():
        if isinstance(value, dict):
            nested = extract_snr(value)
            if nested is not None:
                return nested

    return None


def renew_access_token(token_file: str, app_name: str = "new_central") -> str:
    """Renew the access token for the given application and save it back to the token file."""
    if not os.path.exists(token_file):
        raise FileNotFoundError(f"Token file '{token_file}' not found")

    with NewCentralBase(token_info=token_file) as conn:
        new_token = conn.create_token(app_name)

    return new_token


def fetch_client_snr(
    token_file: str,
    site_id: Optional[str] = None,
    site_name: Optional[str] = None,
) -> list[dict[str, Any]]:
    """Fetch client records and extract SNR values for each client."""
    if not os.path.exists(token_file):
        raise FileNotFoundError(f"Token file '{token_file}' not found")

    results: list[dict[str, Any]] = []
    with NewCentralBase(token_info=token_file) as conn:
        items = Clients.get_all_clients(
            central_conn=conn,
            site_id=site_id,
            site_name=site_name,
        )

        for item in items:
            client_mac = item.get("clientMac") or item.get("mac") or item.get("id")
            snr = extract_snr(item)

            if snr is None and client_mac:
                details = Clients.get_client_details(central_conn=conn, client_mac=client_mac)
                if isinstance(details, dict):
                    snr = extract_snr(details)

            results.append(
                {
                    "clientMac": client_mac,
                    "status": item.get("status"),
                    "snr": snr,
                }
            )

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch client SNR values from Aruba Central")
    parser.add_argument("--token-file", default="/home/blackhole/my_project/src/my_project/token.yaml")
    parser.add_argument("--site-id")
    parser.add_argument("--site-name")
    parser.add_argument("--renew-token", action="store_true", help="Renew the configured access token in the token file")
    parser.add_argument("--app-name", default="new_central", choices=["new_central", "glp"], help="Application to renew when --renew-token is used")
    parser.add_argument("--output", help="Optional JSON file to write results to")
    args = parser.parse_args()

    if args.renew_token:
        token = renew_access_token(token_file=args.token_file, app_name=args.app_name)
        print(f"Renewed token for {args.app_name}: {token}")
        return

    results = fetch_client_snr(
        token_file=args.token_file,
        site_id=args.site_id,
        site_name=args.site_name,
    )

    print(json.dumps(results, indent=2))

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            json.dump(results, handle, indent=2)
            handle.write("\n")


if __name__ == "__main__":
    main()
