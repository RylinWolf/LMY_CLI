import requests as rt
from requests.packages.urllib3.exceptions import InsecureRequestWarning

rt.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_cookie(token):
    url = "https://www.mosoteach.cn/web/index.php"
    params = {
        "c": "passport",
        "m": "save_proxy_token",
        "proxy_token": "",
        "remember_me": "N"
    }

    headers = {
        "Host": "www.mosoteach.cn",
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.mosoteach.cn/web/index.php?c=passport",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }


    params["proxy_token"] = token

    response = rt.get(url, headers=headers, params=params, verify=False)
    cookie = response.headers["Set-Cookie"]
    cookie_list = cookie.split(";")
    for each in cookie_list.copy():
        cookie_list.remove(each)
        cookie_list.extend([e.strip() for e in each.split(",") if len(e) > 30])
    cookie = ""
    for each in cookie_list:
        cookie += each + ";"
    return cookie


