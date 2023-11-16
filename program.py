import os
import pickle
import sys

import AutoSubmit
import GetCookie
import GetSection
import GetCourses
import GetAnswers
import Login

setting_file = "settings.cfg"
abs_st_file = os.path.join(os.getcwd(), setting_file)
setting_format = {
    "account": None,
    "passcode": None,
}


def login(settings: dict | None):
    print("===================")
    user = None
    password = None
    if settings:
        user = settings["account"]
        password = settings["passcode"]

    user = input("账号: ") if not user else (user, print(f"当前账号: {user}"))[0]
    password = input("密码: ") if not password else password

    while True:
        user_info = Login.login(user, password)

        if not user_info["status"]:
            print("==========提示信息==========")
            print("登录失败! " + user_info["errorMessage"])
            print("==========================\n")
            user = input("账号: ")
            password = input("密码: ")
            continue
        return {"user_info": user_info, "account": user, "passcode": password}


def get_cookie(token):
    print("正在获取Cookie...")
    return GetCookie.get_cookie(token)


def get_courses(user_info, cookie):
    print("正在获取课程...")
    courses = GetCourses.get_courses(cookie)
    courses_ids = []
    while True:
        print(f"\n==========用户{user_info['nick_name']}的课程如下==========")
        for index, course in enumerate(courses):
            print(f"{index + 1}、{course['course_name']}  {course['teacher']}  {course['class']}  {course['time']}")
            courses_ids.append((course['course_name'], course["id"]))

        select_course = input("\n请选择(输入0以退出): ")
        if not (select_course.isdigit() and 0 <= int(select_course) <= len(courses_ids)):
            print("输入有误！请重新选择")
            continue
        select_course = int(select_course)
        if select_course == 0:
            return False
        print(courses_ids[select_course - 1])
        return courses_ids[select_course - 1]


def get_sections(class_name, class_id, cookie):
    """
    获取全部章节
    :param class_name:
    :param class_id:
    :param cookie:
    :return:
    """
    print("正在获取章节...")
    sections = GetSection.get_sections(class_id, cookie)
    sections_ids = []
    while True:
        print(f"==============={class_name}===============")
        for index, section in enumerate(sections):
            print(f"{index + 1}、{section['name']}  {section['info']}")
            sections_ids.append((section['name'], section["id"]))

        select_section = input("\n请选择(输入0以返回): ")
        if not (select_section.isdigit() and 0 <= int(select_section) <= len(sections_ids)):
            print("输入有误！请重新选择")
            continue
        select_section = int(select_section)
        if select_section == 0:
            return False
        print(sections_ids[select_section - 1])
        return sections_ids[select_section - 1]


def get_section_detail(course_id, section_name, section_id, user_id, cookie):
    """
    获取章节答题情况
    :param course_id:
    :param section_name:
    :param section_id:
    :param user_id:
    :param cookie:
    :return:
    """
    details = GetSection.get_section_detail(course_id, section_id, user_id, cookie)
    print(f"===================={section_name}答题情况====================")
    for detail in details:
        print(
            f"{detail['name']}  \t学号: {detail['no']}  得分: {detail['score']}  答题时长: {detail['duration']}  提交时间: {detail['time']}")


def get_answer(class_id, section_id, user_id, cookie, show=False):
    answer = GetAnswers.get_answer(class_id, section_id, user_id, cookie)
    if not answer:
        return False
    if not show:
        return answer['rows']
    answer_alpha = ["A", "B", "C", "D", "E"]
    print(f"===================={answer['title']}====================")
    print(f"章节标题: {answer['title']}\n"
          f"百分制得分: {answer['user_score']}\n得分: {answer['user_total_score']}\n完成时间: {answer['user_duration']}")
    for index, each_part in enumerate(answer['rows']):
        print(f"==========第{index + 1}道题目==========")
        # print(f"题目id: {each_part['id']}\n题目类型: {each_part['type']}\n题目标题: {each_part['subject']}\n"
        #       f"题目选项: {each_part['options']}\n题目答案: {[answer_alpha[each] for each in each_part['answers']]}")

        topic_options = []
        for option in each_part["options"]:
            topic_options.append(f"{answer_alpha[option['item_no']]}. {option['content']}")
        # v2 接口有 key 变动
        print(f"题目id: {each_part['topic_id']}\n题目类型: {each_part['type']}\n题目标题: {each_part['subject']}\n"
              f"题目选项: {topic_options}\n题目答案: {[answer_alpha[each] for each in each_part['answers']]}\n"
              f"用户答案: {[answer_alpha[each] for each in each_part['user_answers']]}")
    return answer['rows']


def auto_submit(course_id, section_id, cookie, answer_rows, sleep_time):
    return AutoSubmit.submit(course_id, section_id, cookie, answer_rows, sleep_time)


def section_func(course_id, section_name, section_id, user_id, cookie):
    """
    单章节功能选择
    :param course_id:
    :param section_name:
    :param section_id:
    :param user_id:
    :param cookie:
    :return:
    """
    while True:
        print("===============章节功能选择===============")
        print("1、查看章节答题情况\n2、获取答案\n3、自动答题\n4、返回")
        select = input("请选择: ")
        if select == "4":
            return
        if select not in ("1", "2", "3"):
            print("输入有误!")
            continue
        if select == "1":
            get_section_detail(course_id, section_name, section_id, user_id, cookie)
            continue
        if select == "2":
            get_answer(course_id, section_id, user_id, cookie, True)
            continue
        if select == "3":
            seconds = input("请输入答题秒数: ")
            if not seconds.isdigit() or int(seconds) <= 0:
                print("输入有误! 需为正整数! ")
                continue
            seconds = int(seconds)
            auto_submit(course_id, section_id, cookie, get_answer(course_id, section_id, user_id, cookie, False),
                        seconds)


def enter_course(user_info):
    while True:
        cookie = get_cookie(user_info["token"])
        print(cookie)
        print(user_info['id'])
        course_info = get_courses(user_info, cookie)
        if not course_info:
            return
        select_course_name, select_course_id = course_info

        while True:
            section_info = get_sections(select_course_name, select_course_id, cookie)
            if not section_info:
                break

            select_section_name, select_section_id = section_info
            section_func(select_course_id, select_section_name, select_section_id, user_info["id"], cookie)


def initialize_settings():
    """
    初始化设置文件
    :return: None
    """
    if os.path.isfile(abs_st_file):
        return
    with open(abs_st_file, "wb+") as f:
        pickle.dump(setting_format.copy(), f)


def load_settings():
    """
    加载配置信息
    :return:
    """
    with open(abs_st_file, "rb+") as f:
        settings = pickle.load(f)
    return settings


def save_settings(settings):
    """
    保存配置信息
    :param settings: 配置字典
    :return: None
    """
    with open(abs_st_file, "wb") as f:
        pickle.dump(settings, f)
    return


def toggle_settings(settings=None, account=None, passcode=None):
    """
    切换指定配置
    :param settings: 配置字典
    :param account: 要保存的账号信息
    :param passcode: 要保存的密码信息
    :return: None
    """
    logout = settings is None
    settings = load_settings() if not settings else settings
    settings["account"] = account
    settings["passcode"] = passcode
    save_settings(settings)
    sys.exit() if logout else None


def setting(account, passcode):
    while True:
        settings = load_settings()
        is_ac = settings["account"] is not None
        is_pc = settings["passcode"] is not None

        print("\n========== 当前设置 ==========")
        print(f"记住账号[{is_ac}]")
        print(f"记住密码[{is_pc}]")

        print("\n【切换设置】")
        print(f"1. {'记住' if not is_ac else '取消记住'}账号")
        print(f"2. {'记住' if not is_pc else '取消记住'}密码")
        print(f"3. 返回")
        ix = input("请选择: ")
        if ix == "1":
            toggle_settings(settings, None if is_ac else account, None if is_ac else settings['passcode'])
            continue
        if ix == "2":
            toggle_settings(settings, settings['account'] if is_pc else account, None if is_pc else passcode)
            continue
        if ix == "3":
            break


def main(login_info):
    while True:
        user_info = login_info["user_info"]
        account = login_info["account"]
        passcode = login_info["passcode"]
        funcs = {
            "1": ("进入课程", enter_course, (user_info,)),
            "2": ("设置", setting, (account, passcode,)),
            "3": ("临时切换账号", run, (False,)),
            "4": ("注销", toggle_settings,),
            "5": ("退出", sys.exit)
        }
        print("====================")
        for k, v in funcs.items():
            print(f"{k}. {v[0]}")
        func_k = input("请选择: ")
        func = funcs[func_k]
        if len(func) > 2:
            func[1](*func[2])
        else:
            func[1]()


def run(use_settings=True):
    initialize_settings()
    settings = load_settings() if use_settings else None
    login_info = login(settings)
    main(login_info)


run()
