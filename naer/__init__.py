from http.client import HTTPConnection
import json


def segment(語句):
    連線 = HTTPConnection('coct.naer.edu.tw')
    資料 = json.dumps({'RawText': 語句})
    連線.request(
        "POST", "/Segmentor/Func/getSegResult/",
        資料,
        {'Content-Type': 'application/json'}
    )
    回應字串 = 連線.getresponse().read().decode('utf-8')
    連線.close()
    return json.loads(回應字串)['result']
