import concurrent.futures
import requests
import random
import string
import allure
from consts.consts import PressureTest

REGISTER_API_URL = 'http://weixin.c-lap.cn/lms/public//index/rbbw/test'


@allure.story(PressureTest)
# title 设置的小标题，功能标题
@allure.title("用户注册-预期成功啦啦啦")
# 描述功能
@allure.description("该用例是针对 注册-查看 场景的测试")
# 点击链接标题跳转
@allure.issue(
    "http://localhost:63342/test/.build/allure-report/index.html?_ijt=fnbfmf4p6u6f3im4d27c4htqok&_ij_reload=RELOAD_ON_SAVE#behaviors/968fefd8e520e1d220d6503040c7c1c4/8e75f107e8acf5c6/",
    name="点击，跳转到对应BUG的链接地址")
@allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
# 生成随机用户名和密码的函数
def generate_credentials(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(length))), ''.join(
        (random.choice(letters_and_digits) for i in range(length)))


# 模拟注册的函数
def simulate_registration(session, username):
    # payload = {'username': username, 'password': password}
    payload = {"arr": username}
    response = session.post(REGISTER_API_URL, json=payload)
    if response.status_code == 200:
        print(f"User {username} registered successfully.")
    else:
        print(f"Failed to register user {username}. Status code: {response.status_code}")


# 主函数
def test_run():
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        with requests.Session() as session:
            # 提交30个注册任务
            futures = []
            for _ in range(30):
                # username, password = generate_credentials()
                username = generate_credentials()
                # futures.append(executor.submit(simulate_registration, session, username, password))
                futures.append(executor.submit(simulate_registration, session, username))
            # 等待所有任务完成
            concurrent.futures.wait(futures)


#
if __name__ == '__main__':
    test_run()
