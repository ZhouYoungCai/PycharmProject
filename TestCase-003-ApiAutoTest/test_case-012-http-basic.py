import requests
from requests.auth import HTTPBasicAuth

def test_auth():
    r = requests.get(
        url="https://httpbin.testing-studio.com/basic-auth/insane/123",
        auth = HTTPBasicAuth("Insane", "123"),
        verify = False
        )
    print(r.request.headers)