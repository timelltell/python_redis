import sys
import os
import json
import requests
import subprocess
import redis

if __name__ == '__main__':
    url_wehook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=212f5d3c-707d-4388-a3dd-01f28ff34e9c'
    header = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": "今天你学习了吗 <@shichaoliao><@zekeeliu><@timellchen>",
            "mentioned_list": ["shichaoliao","zekeeliu","timellchen","@all"]
        }
    }
    requests.post(url_wehook, headers=header, json=data)