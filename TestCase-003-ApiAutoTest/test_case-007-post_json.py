import requests

class Test_Demo:
    def test_post_json(self):
        payload = {"level":1,"name":"zyc"}
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1
