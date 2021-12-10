import bs4
import requests as rt
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import GetCookie
import json

rt.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_sections(clazz_id: str, cookie: str) -> list:
    """
    获取所有章节

    :param clazz_id:  课程ID
    :param cookie:
    :return:
    """
    params = {
        "c": "interaction",
        "m": "index",
        "clazz_course_id": ""
    }
    headers = {
        "Host": "www.mosoteach.cn",
        "Cookie": "",
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.mosoteach.cn/web/index.php?c=clazzcourse&m=index",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }

    url = "https://www.mosoteach.cn/web/index.php"
    params["clazz_course_id"] = clazz_id
    headers["Cookie"] = cookie

    response = rt.get(url, headers=headers, params=params, verify=False)
    content = bs4.BeautifulSoup(response.text.replace(" ", ""), "html.parser")
    details = content.find_all("div", "interaction-row")
    sections = []
    for each_part in details:
        part_name = each_part.find("span", "interaction-name").text.strip()
        part_id = each_part.attrs["data-id"]
        part_info_list = each_part.text.replace(" ", "").replace("\n", "").split("共")[1:]
        for info in part_info_list.copy():
            part_info_list.remove(info)
            info = info.split("|")
            info.remove("") if "" in info else None
            part_info_list.extend(info)
        part_info = ""
        for each in part_info_list:
            part_info += each + " "
        sections.append({"name": part_name, "id": part_id, "info": part_info})

    return sections


"""
POST /web/index.php?c=interaction_quiz&m=get_quiz_ranking HTTP/1.1
Host: www.mosoteach.cn
Cookie: _uab_collina=163836922173518136731092; acw_tc=2f624a5416384299647027659e747a7c0f67752c067205cb507e69bdc23597; teachweb=ad40ad7d64243c7ffd95cc702763cdb8d46e6434; SERVERID=f83e20313967653971d0618a2ae74747|1638430060|1638429964
Content-Length: 39
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
Referer: https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=quiz_ranking&clazz_course_id=DB201808-1393-11EC-80AB-B8599FE847B4&id=9965020F-7D09-41B9-8276-5AF7CBDBD128&order_item=group&user_id=FC9C4296-92D2-42FD-9C8C-BF778904BC39
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

id=9965020F-7D09-41B9-8276-5AF7CBDBD128
"""


def get_section_detail(course_id, section_id, user_id, cookie):
    """
    获取章节的完成情况
    :param course_id:
    :param section_id:
    :param user_id:
    :param cookie:
    :return:
    """
    headers = {
        "Host": "www.mosoteach.cn",
        "Cookie": cookie,
        "Content-Length": "39",
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": f"https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=quiz_ranking&order_item=group&clazz_course_id={course_id}&id={section_id}&user_id={user_id}",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }
    params = {"c": "interaction_quiz", "m": "get_quiz_ranking"}
    data = {"id": section_id}
    url = "https://www.mosoteach.cn/web/index.php"

    response = rt.post(url, headers=headers, params=params, data=data, verify=False)
    detail_list = json.loads(response.text)["data"]["rows"]
    res = []
    for info in detail_list:
        full_name = info["full_name"]
        student_no = info["student_no"]
        score = info["score"]
        time = info["end_time"]
        duration = info["duration"]
        res.append({"name": full_name, "no": student_no, "score": score, "time": time, "duration": duration})
    return res
