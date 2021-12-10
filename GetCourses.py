import requests as rt
import bs4
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

rt.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_courses(cookie):
    headers = {
        "Host": "www.mosoteach.cn",
        "Cookie": "",
        "Content-Length": "0",
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.mosoteach.cn/web/index.php?c=clazzcourse&m=index",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }

    url = "https://www.mosoteach.cn/web/index.php"
    param = {"c": "clazzcourse", "m": "my_joined"}
    headers["Cookie"] = cookie

    response = rt.get(url, headers=headers, params=param, verify=False)
    courses_info = json.loads(bs4.BeautifulSoup(response.text, "html.parser").text)["data"]
    courses_result = []
    for index, detail in enumerate(courses_info):
        course_id = detail["id"]
        course_name = detail["course"]["name"]
        course_time = detail["course"]["create_time"]
        teacher_name = detail["creater"]["full_name"]
        clazz_name = detail["clazz"]["name"]

        courses_result.append({"course_name": course_name,
                               "teacher": teacher_name,
                               "class": clazz_name,
                               "time": course_time,
                               "id": course_id})
    return courses_result

