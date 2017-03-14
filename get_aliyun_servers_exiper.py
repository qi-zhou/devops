#!/usr/bin/env python3
from datetime import datetime
import time
from datetime import date
import requests
import sys
import os
import base64
from urllib import parse import hmac
import hashlib
from hashlib import sha1
import time
import uuid
import json

access_key_id = 'LTAIK1M7g0huDmwX'
access_key_secret = 'I19ejmSif4pPJbCKoSaKzkV93EC58G'
server_address = 'https://ecs.aliyuncs.com'
now = datetime.now()


def get_user_params(Action, RegionId):
    dict = {}
    dict['Action'] = Action
    dict['RegionId'] = RegionId
    return dict


def percent_encode(s):
    res = parse.quote(s.encode('utf-8'), '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res


def compute_signature(parameters, access_key_secret):
    sortedParameters = sorted(
        parameters.items(), key=lambda parameters: parameters[0])
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + \
            percent_encode(k) + '=' + percent_encode(v)
    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])
    h = hmac.new(access_key_secret.encode('utf-8') +
                 "&".encode('utf-8'), stringToSign.encode('utf-8'), sha1)
    signature = base64.encodestring(h.digest()).strip()
    return signature


def compose_url(user_params):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    parameters = {
        'Format': 'JSON',
        'Version': '2014-05-26',
        'AccessKeyId': access_key_id,
        'SignatureVersion': '1.0',
        'SignatureMethod': 'HMAC-SHA1',
        'SignatureNonce': str(uuid.uuid1()),
        'TimeStamp': timestamp,
    }
    for key in user_params.keys():
        parameters[key] = user_params[key]
    signature = compute_signature(parameters, access_key_secret)
    parameters['Signature'] = signature
    url = server_address + "/?" + parse.urlencode(parameters)
    return url


def make_request(user_params, quiet=False):
    url = compose_url(user_params)
    response = requests.get(url)
    j = response.json()
    return j


all_region = make_request(get_user_params(
    Action='DescribeRegions', RegionId='cn-beijing'))
for i in range(len(all_region["Regions"]["Region"])):
    region_id = all_region["Regions"]["Region"][i]["RegionId"]
    per_region_servers = make_request(get_user_params(
        Action='DescribeInstances', RegionId=region_id))
    instance_list = list(per_region_servers["Instances"]["Instance"])
    for n in range(len(instance_list)):
     # print(instance_list[n]["InstanceName"])
        hostname = instance_list[n]["InstanceName"]
        ExpiredTime = instance_list[n]["ExpiredTime"]
        deadline = datetime.strptime(ExpiredTime, "%Y-%m-%dT%H:%SZ")
        rest_of_time = (deadline - now).days
        if 0 < rest_of_time < 15:
            print('服务器{}即将到期，还剩{}天，具体到期时间:{}'.format(
                hostname, rest_of_time, deadline))
        elif rest_of_time < 0:
            print('服务器{}已经到期{}天，具体到期时间:{}'.format(
                hostname, abs(rest_of_time), deadline))
