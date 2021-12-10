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
        "c": "interaction_quiz",
        "m": "person_quiz_result",
        "clazz_course_id": class_id,
        "id": section_id,
        "order_item": "group",
        "user_id": user_id
    }

    headers = {
        "Host": "www.mosoteach.cn",
        "Cookie": cookie,
        "Content-Length": "84",

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
    try:
        res = json.loads(content.text.replace("<br \\=""/>", "").replace("\"一带一路\"建", "一带一路建"))["data"]
    except KeyError:
        print("该章节尚未答题，请先答题!")
        return False

    result = {"title": res["title"],
              "user_score": res["user_score"],
              "user_total_score": res["user_total_score"],
              "user_duration": res["user_duration"],
              "rows": res["rows"]}
    return result