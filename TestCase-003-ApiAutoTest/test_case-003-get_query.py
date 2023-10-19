import requests

class Test_Demo:
    def test_query(self):
        payload = {"level": 1,"name": "zhouyongcai"}
        r = requests.get("http://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200
