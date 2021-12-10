import json
import time

import requests as rt


def reg_action(course_id, section_id, cookie):
    """
    注册活动，开始答题
    :param course_id:
    :param section_id:
    :param cookie:
    :return:
    """
    headers = {
        "Host": "www.mosoteach.cn",
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "Cookie": cookie,
        "Accept": "application/json, text/plain, */*",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
        "Origin": "https://www.mosoteach.cn",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": f"https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=reply&clazz_course_id={course_id}&id={section_id}&order_item=group",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }

    params = {"c": "interaction_quiz", "m": "start_quiz"}
    data = {"act_id": section_id}
    url = "https://www.mosoteach.cn/web/index.php"
    response = rt.post(url, headers=headers, params=params, data=data, verify=False)
    try:
        res = json.loads(response.text)
        if "error" in str(res):
            raise json.decoder.JSONDecodeError
    except json.decoder.JSONDecodeError:
        print("答题注册失败! ")
        return False
    print("答题注册成功, 已开始答题, 请等待! ")
    return True


"""
POST /web/index.php?c=interaction_quiz&m=save_answer HTTP/1.1
Host: www.mosoteach.cn
Cookie: _uab_collina=163836922173518136731092; teachweb=32561e9da0c8fa8c9240fbf9f428d6d7ee901d90; acw_tc=2f624a5916384369393997175e1422f1c1ce2d70ee84c12256011a62f7b980; SERVERID=5da4142ab453b5c560efefb22dcfbe6a|1638437542|1638435116
Content-Length: 6539
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
X-Token: e7d2da2fe1963aea115132c9c0d7a95f
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: application/json, text/plain, */*
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Platform: "macOS"
Origin: https://www.mosoteach.cn
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=reply&clazz_course_id=DB201808-1393-11EC-80AB-B8599FE847B4&id=9965020F-7D09-41B9-8276-5AF7CBDBD128&order_item=group
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

id=9965020F-7D09-41B9-8276-5AF7CBDBD128&clazz_course_id=DB201808-1393-11EC-80AB-B8599FE847B4&data=%5B%7B%22id%22%3A%22924DEBF8-E871-43EE-B5BD-DE028AD9E410%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%220F013BF4-8D07-486C-83EF-829D75776181%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22FF7B2104-7ACB-4ACF-A4A9-0576C04853E6%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%226C477976-4553-4F75-8059-4CBE4229DF1B%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%226EC60094-A3E6-4F31-99A0-0F2FE900102A%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%2258AC1189-8FF5-4BF4-9F32-F6ABDCA41210%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%228FAEE28E-CC17-47BF-9F75-2A74F0781514%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%2290D6D7D0-96E3-4035-B745-DBA95A777F5A%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22EFC78BB8-B7E9-4431-BD71-61671F767E02%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%224E2D49BB-AB0C-4518-BD0A-B7A614D2A424%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%2234E5A54B-0F51-4158-8E33-FFDA736A9933%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%229F0DF26F-A395-4F87-96FA-C5597E34D7EE%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22C362916C-AE79-4B8E-9A9C-F02E81735D93%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22072449A2-8A6A-4379-BFBC-19D249DAFCC7%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22A420DC01-83C2-48DF-A641-3CA6B6C3B8A5%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22F428C329-0C5F-47CA-A6E2-8A9B2D5BDC76%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22AFC02D5C-426E-4AB2-98C3-7905CA818CA9%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%2298DCF171-D235-42A1-9E82-BBB13241A823%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%226BBEC1F1-C0F3-417F-B589-0CE9F74DD186%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22D467B1D5-FCE7-4135-8142-2DDDE5F5998C%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%224E5CF4CB-C490-44D5-8F80-495FF9C7E3B0%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22044BAB99-113D-426D-BCF8-BD3C7D90E113%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22EF962ED4-DAA6-4780-9588-E8EC15E50F15%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%229B166392-F0E0-468A-99B2-A421CBB4EE0B%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%2284CB87FE-A190-43A3-AC94-4DB8FBCE343A%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22AB08398A-87BB-4F33-9D2E-9215A32A5D87%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%2206F6D7CC-A58B-4D79-98A2-7B0F24238A97%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%222F1711AF-A0E7-48FE-A295-6017F983DCC7%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22599F3A37-4551-4EC5-BE79-7B5A8C606B23%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22E16A3F62-FAC1-436E-BF0A-9EE38BB8895F%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22B7B4C474-5C55-4D55-9281-50DAB21A5504%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%226842FE3B-FACD-4DFD-9C5D-A1918BEAA042%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22DC90CB21-D550-4ECD-A1FE-B5E4B328A150%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%229F2FAD34-E86E-4E9F-BED6-67AB1915E592%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%224836913F-AA9F-4471-A6B4-A9633C9328E1%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%223CB9C605-0CC6-40B5-9024-69059FD5CA9A%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%222E50778E-8A94-4F1C-8471-5A460506093A%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22FB71D63E-0DAA-40DA-88CF-623884F7F246%22%2C%22type%22%3A%22MULTI%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22EA5BDFBE-7D97-4E8C-A8C1-38C81B495D95%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22478A50DB-173D-4723-AA26-495FFD13BBDA%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%220EDD1118-2B2F-4563-B19A-A929E93B48CB%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22EBAE0886-6B32-4908-AAE7-36C3C27994A4%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%2C%7B%22id%22%3A%22408FCE5C-B0B8-4182-A55A-72C646437064%22%2C%22type%22%3A%22SINGLE%22%2C%22proof_attachments%22%3A%5B%5D%2C%22answers%22%3A%5B%5D%7D%5D

data/json [{"id":"924DEBF8-E871-43EE-B5BD-DE028AD9E410","type":"MULTI","proof_attachments":[],"answers":[]}]
"""


def submit(course_id, section_id, cookie, answer_rows, sleep_time=30):
    reg_action(course_id, section_id, cookie)
    for i in range(1, sleep_time+1):
        print("\r请等待..."+">"*int(100*i/sleep_time)+f"{i}/{sleep_time}", end="")
        time.sleep((sleep_time-1)/sleep_time)

    headers = {
        "Host": "www.mosoteach.cn",
        "Cookie": cookie,
        "Content-Length": "6539",
        "Content-type": "application/x-www-form-urlencoded",
        "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Platform": "macOS",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "empty",
        "Referer": f"https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id={course_id}&id={section_id}&order_item=group",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }
    url = "https://www.mosoteach.cn/web/index.php"
    params = {"c": "interaction_quiz", "m": "save_answer"}
    answer = []
    for each in answer_rows:
        # print(each)
        answer.append({"id": each["id"], "type": each["type"], "proof_attachments": [], "answers": each["answers"]})
    # print(answer)
    data = {"id": section_id, "clazz_course_id": course_id,
            "data": str(answer).replace(" ", "").replace("'", "\"")
            }
    # print(data)

    response = rt.post(url, headers=headers, params=params, data=data, verify=False)
    res = json.loads(response.text)
    if "data" not in res:
        print("自动答题失败!")
        return False

    if res["result_msg"] == "OK":
        print("答题成功! ")
        score_details = res["data"]
        print(f"本次成绩: {score_details['score']}, 最好成绩: {score_details['best_score']}")
        return True

    print("未知错误! "+res)
    return False
