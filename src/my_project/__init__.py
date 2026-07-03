from pycentral import NewCentralBase
import os

def greet(name: str = "world") -> str:
    # Validate token file exists
    token_file = "/home/blackhole/my_project/src/my_project/token.yaml"
    if not os.path.exists(token_file):
        raise FileNotFoundError(
            f"Token file '{token_file}' not found. Please provide a valid token file."
        )

    # Initialize NewCentralBase class with the token credentials for New Central/GLP
    with NewCentralBase(token_info=token_file) as conn:

        # Make the API call to retrieve device inventory
        resp = conn.command(
            api_method="GET",
            api_path="network-monitoring/v1/device-inventory"
        )

        # If the response code is 200, print the device inventory response; otherwise, print the error code and message
        if resp["code"] == 200:
            print(resp["msg"])
        else:
            print(f"Error {resp['code']}: {resp['msg']}")
    return f"Hello, {name}!"

__all__ = ["greet"]
