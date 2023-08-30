import json

import requests

import requests

cookies = {
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2230686692%22%2C%22first_id%22%3A%2217fac9208e1f02-028fa07b9c44d42-5617185b-2024099-17fac9208e2105a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%2217fac9208e1f02-028fa07b9c44d42-5617185b-2024099-17fac9208e2105a%22%7D',
    'xt_lang': 'zh',
    'x_access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjMwNjg2NjkyLCJlaWQiOjU0Nzk5OSwiY2lkIjoiMTAyNDI0MDYiLCJleHAiOjE2NDc5NzA3NjQsInJvIjowfQ.YdE7U864FCLrff-7UAf9Jf-Db00AgYoSS3bTGfQ3pfE',
}

headers = {
    'authority': 'examination.xuetangx.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    'dnt': '1',
    'xtbz': 'cloud',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'accept': 'application/json, text/plain, */*',
    'x-client': 'web',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://examination.xuetangx.com/result/547999?isFrom=0',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2230686692%22%2C%22first_id%22%3A%2217fac9208e1f02-028fa07b9c44d42-5617185b-2024099-17fac9208e2105a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%2217fac9208e1f02-028fa07b9c44d42-5617185b-2024099-17fac9208e2105a%22%7D; xt_lang=zh; x_access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjMwNjg2NjkyLCJlaWQiOjU0Nzk5OSwiY2lkIjoiMTAyNDI0MDYiLCJleHAiOjE2NDc5NzA3NjQsInJvIjowfQ.YdE7U864FCLrff-7UAf9Jf-Db00AgYoSS3bTGfQ3pfE',
}

params = {
    'exam_id': '547999',
}

response = requests.get('https://examination.xuetangx.com/exam_room/problem_results', headers=headers, params=params, cookies=cookies)

# print(response.text)

paper_url = "https://examination.xuetangx.com/exam_room/show_paper"
papers = requests.get(paper_url,headers=headers,params=params,cookies=cookies)
questions =  papers.json()["data"]['problems']
answer_lst = []
answer_only = []
for index,i in enumerate(questions):
    dic_question = {}
    title  = str(index+1) + "." +i['Body'].replace("<p>","").replace("</p>","").strip()
    answer = "".join(i["Answer"])
    options = i["Options"]
    print(options)
    dic_opt = {option["key"]:option["value"].replace("<p>","").replace("</p>","").strip()  for option in options}
    print(dic_opt)
    dic_question['question'] = title
    dic_question['options'] = dic_opt
    dic_question['answer'] = answer
    answer_lst.append(dic_question)
    dic_only = {}
    dic_only["question"] = title
    dic_only['answer'] = answer
    answer_only.append(dic_only)


with open("exam.json",'w',encoding='utf-8') as fp:
    fp.write(json.dumps(answer_only,ensure_ascii=False))