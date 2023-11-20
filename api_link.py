import os
import sys
import requests
import json

# 키와 url 정의
key = 'ttbkangmj08250027001'
url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType=ItemNewAll&MaxResults=100" \
      "&start=1&SearchTarget=Book&output=js&Version=20131101&CategoryId=50993"

# request 보내기
response = requests.get(url)

# 받은 response를 json 타입으로 바뀌주기
response_json = json.loads(response.text)
# 확인
print(response_json)