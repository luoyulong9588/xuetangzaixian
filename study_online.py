# -*- coding:utf-8 -*- 

"""
作者：luoyu
日期：2021年05月12日
学堂在线
"""
import time

import requests
import json
import re
from rich import print


def get_classid():
    headers = {
        'authority': 'www.xuetangx.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
        'django-language': 'zh',
        'dnt': '1',
        'accept-language': 'zh',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
        'app-name': 'xtzx',
        'content-type': 'application/json',
        'accept': 'application/json, text/plain, */*',
        'terminal-type': 'web',
        'x-client': 'web',
        'xtbz': 'xt',
        'x-csrftoken': 'NmgfUKU6n2nFN45KtiEQsCuhEwCyeQ9h',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.xuetangx.com/learn/sxyz62011005322/sxyz62011005322/14769683/video/30328712?channel=i.area.learn_title',
        # Requests sorts cookies= alphabetically
        'cookie': 'provider=xuetang; _abfpc=9b2cb0fb2c637f3792329f38aae4c1f5e5956b4c_2.0; cna=f7f1b7350caf1de941166c1ae8324371; django_language=zh; sajssdk_2015_cross_new_user=1; point={%22point_active%22:true%2C%22platform_task_active%22:true%2C%22learn_task_active%22:true}; login_type=WX; csrftoken=NmgfUKU6n2nFN45KtiEQsCuhEwCyeQ9h; sessionid=2cjs3c36d7i9wltzx780mufbditikhox; k=30686692; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2230686692%22%2C%22first_id%22%3A%22188579ae34c4e7-0ce6db449e2a48-26031a51-2359296-188579ae34d173d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%22188579ae34c4e7-0ce6db449e2a48-26031a51-2359296-188579ae34d173d%22%7D; 30686692video_seconds=135',
    }

    params = (
        ('cid', '14769683'),
        ('sign', 'sxyz62011005322'),
    )

    "cid=10242406&product_sign=sxyz62011005322"
    response = requests.get('https://www.xuetangx.com/api/v1/lms/learn/course/chapter', headers=headers, params=params)
    result = response.json()
    classlst = result['data']['course_chapter']

    # print(classlst)
    clssLst = []
    for item in classlst:
        q = json.dumps(item['section_leaf_list'], ensure_ascii=False)
        b = json.loads(q)
        for item2 in b:
            try:
                result2List = item2['leaf_list']
                for result2 in result2List:
                    if "测试题" in result2['name'] or "自测题" in result2['name']:
                        clssLst.append(result2)
            except:
                pass
    questionLst = []
    for each in clssLst:
        question = {}
        question['name'] = each['name']
        question['id'] = each['id']
        questionLst.append(question)
    print(questionLst)
    return questionLst


def get_true_id(class_id):
    headers = {
        'authority': 'www.xuetangx.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh',
        'app-name': 'xtzx',
        'cookie': '_abfpc=9b2cb0fb2c637f3792329f38aae4c1f5e5956b4c_2.0; cna=f7f1b7350caf1de941166c1ae8324371; sajssdk_2015_cross_new_user=1; login_type=WX; csrftoken=NmgfUKU6n2nFN45KtiEQsCuhEwCyeQ9h; sessionid=2cjs3c36d7i9wltzx780mufbditikhox; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2230686692%22%2C%22first_id%22%3A%22188579ae34c4e7-0ce6db449e2a48-26031a51-2359296-188579ae34d173d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22188579ae34c4e7-0ce6db449e2a48-26031a51-2359296-188579ae34d173d%22%7D; _ga=GA1.2.316921517.1685100476; _gid=GA1.2.603311647.1685100476; provider=xuetang; k=30686692; point={%22point_active%22:true%2C%22platform_task_active%22:true%2C%22learn_task_active%22:true}; university_id=0; platform_id=0; avatar=http://thirdwx.qlogo.cn/mmopen/aDRKsRebBibdoZ8B4vMdBejO2h9JpvQlicDvo4qVGBvsibVUfpT35VgbXXQPxc81ErqH43yhq1Pj2Cdn3lThOttZAChHyRszMFA/132; name=%E7%BD%97%E7%8E%89%E9%BE%99; user_number=null; term=latest; user_role=null; xtbz=xt; django_language=zh; 30686692video_seconds=384',
        'django-language': 'zh',
        'dnt': '1',
        'referer': f'https://www.xuetangx.com/learn/sxyz62011005322/sxyz62011005322/14769683/exercise/{class_id}',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'terminal-type': 'web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-client': 'web',
        'x-csrftoken': 'NmgfUKU6n2nFN45KtiEQsCuhEwCyeQ9h',
        'xtbz': 'xt',
    }

    params = {
        'sign': 'sxyz62011005322',
    }
    response = requests.get(f'https://www.xuetangx.com/api/v1/lms/learn/leaf_info/14769683/{class_id}/',
                            headers=headers, params=params)
    true_id = response.json()["data"]["content_info"]["leaf_type_id"]
    print(true_id, class_id)
    return true_id


def get_answers(classId, trueId):
    headers = {
        'authority': 'www.xuetangx.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh',
        'app-name': 'xtzx',
        'content-type': 'application/json',
        'cookie': '_abfpc=9b2cb0fb2c637f3792329f38aae4c1f5e5956b4c_2.0; cna=f7f1b7350caf1de941166c1ae8324371; sajssdk_2015_cross_new_user=1; login_type=WX; csrftoken=NmgfUKU6n2nFN45KtiEQsCuhEwCyeQ9h; sessionid=2cjs3c36d7i9wltzx780mufbditikhox; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2230686692%22%2C%22first_id%22%3A%22188579ae34c4e7-0ce6db449e2a48-26031a51-2359296-188579ae34d173d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22188579ae34c4e7-0ce6db449e2a48-26031a51-2359296-188579ae34d173d%22%7D; _ga=GA1.2.316921517.1685100476; _gid=GA1.2.603311647.1685100476; provider=xuetang; k=30686692; point={%22point_active%22:true%2C%22platform_task_active%22:true%2C%22learn_task_active%22:true}; university_id=0; platform_id=0; avatar=http://thirdwx.qlogo.cn/mmopen/aDRKsRebBibdoZ8B4vMdBejO2h9JpvQlicDvo4qVGBvsibVUfpT35VgbXXQPxc81ErqH43yhq1Pj2Cdn3lThOttZAChHyRszMFA/132; name=%E7%BD%97%E7%8E%89%E9%BE%99; user_number=null; term=latest; user_role=null; xtbz=xt; django_language=zh; 30686692video_seconds=384',
        'django-language': 'zh',
        'dnt': '1',
        'referer': f'https://www.xuetangx.com/learn/sxyz62011005322/sxyz62011005322/14769683/exercise/30328098{classId}',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'terminal-type': 'web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-client': 'web',
        'x-csrftoken': 'NmgfUKU6n2nFN45KtiEQsCuhEwCyeQ9h',
        'xtbz': 'xt',
    }
    response = requests.get(f'https://www.xuetangx.com/api/v1/lms/exercise/get_exercise_list/{trueId}/6805030/',
                            headers=headers)
    result = response.json()['data']['problems']
    problem_List = []
    answer_return = ""
    count = 0
    for item in result:
        problem_dic = {}
        contains = item['content']["Body"]
        contains2 = re.findall('<p>(.*)', contains)

        problem_dic['question'] = contains2[0].replace("\u2002", "")
        options = item['content']["Options"]
        opt_lst = []
        for opt in options:
            option = opt['key'] + "." + re.findall("<p>(.*)</p>", opt["value"])[0]
            opt_lst.append(option)
        # print(option)
        answer = "None"
        try:
            answer = item['user']["answer"]
        except:
            print("get anwer Error！")
        problem_dic['option'] = opt_lst
        problem_dic['answer'] = answer
        problem_List.append(problem_dic)
        count += 1
        if count % 6 == 0:
            answer_return += "  |  "
        answer_return += str(answer)
    return answer_return


def main():
    classLst = get_classid()
    problemsList = []
    for item in classLst:
        class_Name = item['name']
        class_id = item['id']

        try:
            trueId = get_true_id(item['id'])
            problem_list = get_answers(class_id, trueId)
            problemDic = {}
            problemDic['class'] = class_Name
            problemDic['answers'] = problem_list
            problemsList.append(problemDic)
        except:
            print(f"error--?{item}")
    json_str = json.dumps(problemsList, ensure_ascii=False)
    with open('test_data.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)


if __name__ == '__main__':
    # get_answers(9260358, 989472)
    # main()
    main()
