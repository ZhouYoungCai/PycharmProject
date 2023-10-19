import requests

class Test_Req:
    def test_timeout(self):
        r = requests.get('https://www.baidu.com/',timeout = 0.05)
        print (r.text)
        assert r.status_code == 200