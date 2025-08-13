from requests import get

import __auth__ as auth
from helpers import endpoints

api_key = auth.api_key
file_type = 'json'
base_url = 'https://api.stlouisfed.org/fred/'


def prep_payload(endpoint: str, payload: dict) -> dict:
    keys = list(endpoints[endpoint])
    payload_keys = list(payload.keys())
    for payload_key in payload_keys:
        if payload_key not in keys:
            del payload[key]
    payload['file_type'] = file_type
    payload['api_key'] = api_key

    return payload


def craft_query_string(endpoint: str, payload: dict) -> str:
    payload = prep_payload(endpoint, payload)
    url = f'{base_url}{endpoint}?'
    for key, value in payload.items():
        url += f'&{key}={value}'

    return url


def request(endpoint: str, payload: dict):
    return get(craft_query_string(endpoint, payload))


endpoint = 'series'
payload = {'series_id': 'GNPCA'}
response = request(endpoint, payload)
print(response.content)
