from my_project.client_snr import extract_snr


def test_extract_snr_from_nested_payload():
    payload = {
        "clientMac": "00:11:22:33:44:55",
        "radio": {"signalToNoiseRatio": 34.5},
        "stats": {"snr": 33.0},
    }

    assert extract_snr(payload) == 34.5


def test_extract_snr_returns_none_when_missing():
    payload = {"clientMac": "00:11:22:33:44:55", "status": "Connected"}

    assert extract_snr(payload) is None
