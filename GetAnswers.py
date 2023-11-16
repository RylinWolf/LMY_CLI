import requests as rt
import json
import bs4
from requests.packages.urllib3.exceptions import InsecureRequestWarning

rt.packages.urllib3.disable_warnings(InsecureRequestWarning)

"""
POST /web/index.php?c=interaction_quiz&m=person_result HTTP/1.1
Host: www.mosoteach.cn
Cookie: _uab_collina=163836922173518136731092; acw_tc=707c9fd716383801220292365e3e922274b058beb3f1df4ae6e99b87aba3a8; teachweb=8fe0d86735c36e044c528c423250e72b3e561648; SERVERID=5da4142ab453b5c560efefb22dcfbe6a|1638381238|1638380663
Content-Length: 84
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
X-Token: d0fe003b625ade3ba0a27086d599b555
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
Referer: https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id=DB201808-1393-11EC-80AB-B8599FE847B4&id=72E3E726-C6A8-4B09-A84D-1F7F91C6135F&order_item=group
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

id=72E3E726-C6A8-4B09-A84D-1F7F91C6135F&user_id=FC9C4296-92D2-42FD-9C8C-BF778904BC39
"""


def get_answer(class_id, section_id, user_id, cookie):
    url = "https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_result"
    data = {
        # "c": "interaction_quiz",
        # "m": "person_quiz_result",
        # "order_item": "group",
        # "clazz_course_id": class_id,
        # v2 接口无需上述 data，且 clazz_course_id 更名为 cc_id
        "cc_id": class_id,
        "id": section_id,
        "user_id": user_id
    }

    headers = {
        "Host": "www.mosoteach.cn",
        "Cookie": cookie,
        "Content-Length": "127",
        "Content-Type": "application/x-www-form-urlencoded",
        "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": f"https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id={class_id}&id={section_id}&order_item=group",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }

    response = rt.post(url=url, headers=headers, data=data, verify=False)
    content = bs4.BeautifulSoup(response.content, "html.parser")
    # try:
    #     res = json.loads(content.text.replace("<br \\=""/>", "").replace("\"一带一路\"建", "一带一路建"))["data"]
    # except KeyError:
    #     print("该章节尚未答题，请先答题!")
    #     return False

    res = json.loads(content.text)
    # 个人信息
    stat = res["stat"]

    # 活动信息
    activity = res["activity"]

    result = {"title": activity["title"],
              "user_score": stat["user_score"],
              "user_total_score": stat["user_total_score"],
              "user_duration": "%s分%s秒" % divmod(stat["duration"], 60),
              "rows": activity["topics"]}
    return result

# clazz_course_id = "4905CDFC-9BDA-4A59-8FA4-D0698F406B04"
# s_id = "56400F10-A4D8-4C2B-A200-8BAEEDBB6BC6"
# u_id = "FC9C4296-92D2-42FD-9C8C-BF778904BC39"
# c = "_uab_collina=170002305914632026958164; login_token=1f9842d01cb4046fbd409e3a6c1076f0; acw_tc=76b20f6c17001031435744103e6882f6d6ea69f5cee13ab672f1f031e5f8ef; teachweb=5565665d788947e61b357c79d752d330c6c23887; SERVERID=f83e20313967653971d0618a2ae74747|1700103159|1700103143"
# print(get_answer(clazz_course_id, s_id, u_id, c))
