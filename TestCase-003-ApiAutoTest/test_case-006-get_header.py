import requests

class Test_Demo:
    def test_header(self):
        header = {"h":"headers"}
        r = requests.get("http://httpbin.testing-studio.com/get", headers=header)
        print(r.headers)
        print(r.status_code)
        print(r.headers)
        assert r.status_code == 200


