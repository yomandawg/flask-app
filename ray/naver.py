import json
import urllib.request

def naver(**kwargs):
    with open('ray.json') as ray:
        data = json.load(ray)
        url = data["RequestURL"]
        client_id = data["ClientID"]
        client_secret = data["ClientSecret"]
    body = "{\"startDate\":\"2020-01-01\",\"endDate\":\"2020-03-01\",\"timeUnit\":\"month\",\"category\":[{\"name\":\"패션의류\",\"param\":[\"50000000\"]},{\"name\":\"화장품/미용\",\"param\":[\"50000002\"]}],\"device\":\"pc\",\"ages\":[\"20\",\"30\"],\"gender\":\"f\"}"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        return "Error Code:" + rescode