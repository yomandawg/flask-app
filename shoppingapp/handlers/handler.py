from flask_restful import Resource
from pymongo import MongoClient
import requests
import json

try:
    from shoppingapp import config as cfg
except NotImplementedError:
    print("Please register config")
    print("If you dont know how to register it,")
    print("See : git log 40c1ad8093212ac47482181e40bdf9e1095a58c1")

DATALAB_URL = "https://openapi.naver.com/v1/datalab/shopping/categories"
QUERY = {
    "startDate": "2017-08-01",
    "endDate": "2017-09-30",
    "timeUnit": "month",
    "category": [
        {"name": "패션의류", "param": ["50000000"]},
        {"name": "화장품/미용", "param": ["50000002"]}
    ],
    "device": "pc",
    "gender": "f",
    "ages": ["20",  "30"]
}

TREND_URL = "https://openapi.naver.com/v1/datalab/search"
TREND_QUERY = {
    "startDate": "2020-01-01",
    "endDate": "2020-03-01",
    "timeUnit": "week",
    "keywordGroups": [
        {"groupName": "코로나", "keywords": ["우한"]},
        {"groupName": "코로나", "keywords": ["마스크"]}
    ],
    "device": "mo",
    "gender": "f",
    "ages": ["3", "4", "5"]
}

client = MongoClient('localhost', 27017)

headers = {
    "X-Naver-Client-Id": cfg.client_id,
    "X-Naver-Client-Secret": cfg.client_secret,
    "Content-Type": "application/json"
}

class DBRouter(Resource):
    def get(self):
        online_users = list(client.db.users.find())
        print(type(online_users))
        
        for user in online_users:
            print(user)
            user["_id"] = ""
            print(user)
        print("====> ", online_users[0])
        return json.dumps(online_users[0])


class ShoppingRouter(Resource):
    def get(self):
        r = requests.post(DATALAB_URL, data=json.dumps(QUERY), headers=headers)
        print(r)
        return r.json()


class TrendRouter(Resource):
    # def get(self):
    #     trend_headers = headers
    #     r = requests.post(TREND_URL, data=json.dumps(TREND_QUERY), headers=trend_headers)
    #     print(r)
    #     return r.json()
    
    def get(self, search):
        trend_headers = headers
        trend_query = TREND_QUERY
        trend_query["keywordGroups"] = [{"groupName": "코로나", "keywords": [str(search)]}]
        print(TREND_QUERY)
        r = requests.post(TREND_URL, data=json.dumps(TREND_QUERY), headers=trend_headers)
        print(r)
        return r.json()
        


class TestHandler(Resource):
    def get(self):
        return json.dumps({"name":"cs", "age":34})