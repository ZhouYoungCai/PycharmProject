import requests

class Test_Demo:
    def test_post_form(self):
        payload = {"username": "zhouyongcai","password": "123456"}
        r = requests.post("http://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200