import requests

class Test_proxy:
    def test_post_proxy(self):
        proxiy = {"http":"http://127.0.0.1:8080",
                  "https":"http://127.0.0.1:8080"
                  }
        requests.post(url="https://httpbin.testing-studio.com/post",proxies=proxy)
