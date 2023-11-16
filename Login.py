import requests as rt
import bs4
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

rt.packages.urllib3.disable_warnings(InsecureRequestWarning)


def login(username, password):
    url = "https://coreapi-proxy.mosoteach.cn/index.php/passports/account-login"
    headers = {
        "Host": "coreapi-proxy.mosoteach.cn",
        "Content-Length": "48",
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
        "Sec-Ch-Ua-Platform": "macOS",
        "Origin": "https://www.mosoteach.cn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.mosoteach.cn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "connection": "close"
    }
    data = {
        "account": username,
        "password": password
    }

    response = rt.post(url, headers=headers, json=data, verify=False)
    login_info = json.loads(bs4.BeautifulSoup(response.content, "html.parser").text)
    if login_info["status"] is False:
        return login_info

    user_info = login_info["user"]
    # print(login_info["token"])
    return {
        "status": login_info["status"],
        "token": login_info["token"],
        "id": user_info["userId"],
        "full_name": user_info["fullName"],
        "nick_name": user_info["nickName"],
        # 学号
        "no": user_info["studentNo"]
    }
