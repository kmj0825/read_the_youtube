import os
import sys
import requests
import json


# 키와 url 정의
key = 'ttbkangmj08250027001'
with open("/Users/a11/PycharmProjects/OSS_Project/data/result.json", "r") as f:
    data = json.load(f)
keyword = data["keyword"]
print(keyword)
all_data = []
for i in keyword:
    print(i)
    url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={key}&Query={i}&QueryType=Keyword&Cover=Big&MaxResults=5" \
          "&start=1&SearchTarget=Book&output=js&Version=20131101&CategoryId=0&outofStockFilter=1"
    response = requests.get(url)
    response_json = json.loads(response.text)
    all_data.append(response_json)
# request 보내기
all_data = json.dumps(all_data, ensure_ascii=False, indent=4)

with open("/Users/a11/PycharmProjects/OSS_Project/data/book.json", "wb") as f:
    f.write(all_data.encode("utf-8"))

# 받은 response를 json 타입으로 바뀌주기

# 확인
print(all_data)