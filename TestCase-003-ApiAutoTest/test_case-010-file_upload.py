import requests
class Test_file_upload:
    def test_file_upload(self):
        r = requests.post("https://httpbin.ceshiren.com/post",
                          files={"hogwarts_file":("hogwarts",open("1.txt","rb"))},
                          proxies = {"http":"http://127.0.0.1:8080","https":"http://127.0.0.1:8080"},
                          verify = False
                          )
        print(r.json())
        assert r.status_code = 200