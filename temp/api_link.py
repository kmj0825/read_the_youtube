import os
import sys
import requests
import json


def call_api(file_path, output_path):
    # 키와 url 정의
    key = 'ttbkangmj08250027001'
    with open(file_path, "r") as f:
        data = json.load(f)
    keyword = data["keyword"]
    print(keyword)
    all_data = []
    for i in keyword:
        print(i)
        url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={key}&Query={i}&QueryType=Keyword&Cover=Big&MaxResults=5" \
              "&start=1&SearchTarget=Book&output=js&Version=20131101&CategoryId=987&outofStockFilter=1"
        response = requests.get(url)
        response_json = json.loads(response.text)
        all_data.append(response_json)
    # request 보내기
    all_data = json.dumps(all_data, ensure_ascii=False, indent=4)

    with open(output_path, "wb") as f:
        f.write(all_data.encode("utf-8"))
        # output path = "/Users/a11/PycharmProjects/OSS_Project/data/book.json"

    # 받은 response를 json 타입으로 바뀌주기

    # 확인
    print(all_data)
    return all_data


call_api("/Users/a11/PycharmProjects/OSS_Project/data/result.json",
         "/Users/a11/PycharmProjects/OSS_Project/data/book_test.json")


# 인문 사회 : 90853
# 과학 : 987
# 소설 : 1
# 경제경영 : 170