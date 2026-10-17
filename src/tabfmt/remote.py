def load_json(url, timeout=10):
    """Fetch a JSON array of objects from ``url``. Requires the ``http`` extra."""
    import requests

    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    if not isinstance(data, list):
        raise ValueError("expected a JSON array of objects")
    return data
