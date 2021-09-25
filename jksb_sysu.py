import os, time
from selenium import webdriver
from util import get_img, wx_send
from retrying import retry

options = webdriver.FirefoxOptions()
options.add_argument("--headless") #设置火狐为headless无界面模式
options.add_argument("--disable-gpu")
driver = webdriver.Firefox(executable_path=f'{os.getcwd()}/geckodriver', options=options)
print("初始化selenium driver完成")

wxsend_key = os.environ['SEND_KEY']

# 失败后随机 3-5s 后重试，最多 6 次
# @retry(wait_random_min=3000, wait_random_max=5000, stop_max_attempt_number=6)
# def login():
#     print("访问登录页面")
#     driver.get("https://cas.sysu.edu.cn/cas/login")
#     time.sleep(4)

#     print("读取用户名密码")
#     netid = os.environ['NETID']
#     password = os.environ['PASSWORD']

#     print("输入用户名密码")
#     driver.find_element_by_xpath('//*[@id="username"]').send_keys(netid)
#     driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

#     print("识别验证码")
#     code = get_img(driver, os.environ['RECURL'])
#     print("输入验证码")
#     driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)

#     # 点击登录按钮
#     print("登录信息门户")
#     driver.find_element_by_xpath('//*[@id="fm1"]/section[2]/input[4]').click()
#     try:
#         print(driver.find_element_by_xpath('//*[@id="cas"]/div/div[1]/div/div/h2').text)
#     except:
#         print(driver.find_element_by_xpath('//*[@id="fm1"]/div[1]/span').text)
#         raise Exception('登陆失败')
@retry(wait_fixed=30000,stop_max_attempt_number=3) #延迟200s 每次重试
def jksb():
    
    # 记录步骤执行状态
    step = 0

    login_page = driver.get("https://cas.sysu.edu.cn/cas/login?service=https://portal.sysu.edu.cn/shiro-cas")
    time.sleep(5)

    netid = os.environ['NETID']
    password = os.environ['PASSWORD']

    step = 1 #读取用户名密码成功
    log.get_logger().info("输入用户名密码")
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(netid)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

    step = 2 #输入用户名密码成功
    
    code = get_img(driver, os.environ['RECURL'])
    step = 3 #识别验证码成功

    driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
    step = 4 #输入验证码成功

    # 点击登录按钮
    driver.find_element_by_xpath('//*[@id="fm1"]/section[2]/input[4]').click()

    time.sleep(5)

    
    # 进入健康申报
    log.get_logger().info("进入健康申报页面")
    driver.get("http://jksb.sysu.edu.cn/infoplus/form/XNYQSB/start")
    time.sleep(5)
    try:
        number = driver.find_element_by_xpath('//*[@id="title_description"]').text
        print(number)
    except:
        raise Exception('打开健康申报失败')
    # 点击下一步
    driver.find_element_by_xpath('//*[@id="form_command_bar"]/li[1]').click()
    step=5 #进入健康申报页面


    time.sleep(5)
    # 点击提交
    driver.find_element_by_xpath('//*[@id="form_command_bar"]/li[1]').click()
    step=6 #点击提交按钮成功

    time.sleep(5)
    result = driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/div[2]').text
    step=7 #健康申报完成

    return result
# 失败后随机 3-5s 后重试，最多 6 次
# @retry(wait_random_min=3000, wait_random_max=5000, stop_max_attempt_number=6)
#def jksb():
#    print('访问健康申报页面')
#    driver.get("http://jksb.sysu.edu.cn/infoplus/form/XNYQSB/start")
#    time.sleep(10)
#    try:
#        number = driver.find_element_by_xpath('//*[@id="title_description"]').text
#        print(number)
#    except:
#        raise Exception('打开健康申报失败')
#
#    print("点击下一步")
#    driver.find_element_by_xpath('//*[@id="form_command_bar"]/li[1]').click()
#    time.sleep(10)
#
#    print("提交健康申报")
#    driver.find_element_by_xpath('//*[@id="form_command_bar"]/li[1]').click()
#    time.sleep(10)
#    result = driver.find_element_by_xpath('//div[8]/div/div[1]/div[2]').text
#    print("完成健康申报")
#    return result

if __name__ == "__main__":
#     login()
    try:
        wx_send(wxsend_key, jksb())
        driver.quit()
    except:
        print('健康申报失败')
        wx_send(wxsend_key, '健康申报失败')
        driver.quit()

