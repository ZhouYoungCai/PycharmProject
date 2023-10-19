import requests

class Test_Demo:
    def test_file_upload(self):
        files = {'file': open('report.xls', 'rb')}
        r = requests.post("http://httpbin.testing-studio.com/post", files=files)
        print(r.text)
        assert r.status_code == 200