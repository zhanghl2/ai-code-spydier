from selenium import webdriver
from selenium.webdriver.common.by import By
# 这个是我自己调用百度接口的ocr
from vcode import getocrvalue
import time
# 输入用户名和密码
User_name = '2022036143307'
User_password = '123qweasd123'


def get_cookies():
    browser = webdriver.Edge()
    browser.get("http://www.di-code.com/#/login")
    # 隐式等待
    browser.implicitly_wait(10)
    time.sleep(3)
    code_img_ele=browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div/div/div[2]/div[3]/img")
    # 这里快耗费了一晚上了
    base64code = str(code_img_ele.get_attribute('src'))
    a = getocrvalue(base64code)
    a = str(a)
    element1 = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/input")
    element1.send_keys(User_name)
    element2 = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/input")
    element2.send_keys(User_password)
    element3 = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/input")
    element3.send_keys(a)
    element3 = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[1]")
    time.sleep(1)
    element3.click()
    time.sleep(6)
    cookies = browser.get_cookies()
    #print(cookies[0].get('value'))
    return cookies[0].get('value')




