#coding=utf-8
from core.rsa_client import rsa_client as rsa

from openapi_client import openapi_client as client
import pickle
import core.Global as Global
import json
import time
import datetime
import os

def authorize():
    #step 1 授权
    authorizeStr = client.authorize(appid=Global.AppId, code=Global.code) #获得授权
    authorizeObj = pickle.loads(authorizeStr) # 将返回的authorize对象反序列化成对象，成功得到 OpenID、AccessToken、RefreshToken、ExpiresIn
    print authorizeObj
    # 
    #{"OpenID":"e3aa0536409044f8a035ba2a73d2c4c7",
    #"AccessToken":"dd537d68-3945-4e27-b0d7-ca5b2cca5842",
    #"RefreshToken":"3780d739-1029-42a6-a30a-c56aef5b3fab",
    #"ExpiresIn":604800}

def get_user_fund_balance(appid, access_token):
    #获取用户资金余额
    access_url = "http://gw.open.ppdai.com/balance/balanceService/QueryBalance"
    data = {}
    sort_data = rsa.sort(data)
    sign = rsa.sign(sort_data)
    list_result = client.send(access_url,json.dumps(data) , appid, sign,access_token)

def get_batch_listing_infos(appid, data):
    #新版散标详情批量接口（请求列表不大于10）
    utctime = datetime.datetime.utcnow()
    #data = {"timestamp":utctime.strftime('%Y-%m-%d %H:%M:%S')}#time.strftime('%Y-%m-%d %H:%M:%S',)

    access_url = "http://gw.open.ppdai.com/invest/LLoanInfoService/BatchListingInfos"
    sort_data = rsa.sort(data)
    sign = rsa.sign(sort_data)
    list_result = client.send(access_url, json.dumps(data) , appid, sign)

def get_listingids(appid, access_token):
    #获得投标标的
    access_url = "http://gw.open.ppdai.com/invest/LLoanInfoService/LoanList"
    data = {
      "PageIndex": 3, 
      "StartDateTime": "2015-11-11 12:00:00.000"
    }
    sort_data = rsa.sort(data)
    sign = rsa.sign(sort_data)
    list_result = client.send(access_url,json.dumps(data) , appid, sign)



data = {
  "ListingIds": [
    23886149, 
    23886150
  ]
}
# get_user_fund_balance(Global.AppId, Global.AccessToken)

# get_batch_listing_infos(Global.AppId, data)

get_listingids(Global.AppId, Global.AccessToken)





来一个计算累计收益率的


