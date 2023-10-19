import requests
def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {"Cookie": "Insane_Cookie","User-Agent": "Insane"}
    r = requests.get(url, headers = header, verify=False)
    print(r.request.headers)
    assert r.status_code == 200