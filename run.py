import request
import time
import tesserocr
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver


def zhihulogin(username, password):
    # 获取页面
    driver = webdriver.Chrome()
    driver.get('https://www.zhihu.com/#signin')
    driver.find_element_by_xpath('//*[@class="SignContainer-switch"]/span').click()
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_class_name('SignFlow-submitButton').click()
    # 截取当前页面
    driver.save_screenshot("1.png")
    try:
        # 验证码所在的位置
        element = driver.find_element_by_class_name('Captcha-englishImg')
        location = element.location
        print(location)
        siz = element.size
        print(siz)

        # 计算出元素上下左右位置
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['y']
        bottom = element.location['y'] + element.size['height']

        im = Image.open('baidu.png')
        im = im.crop((left, top, right, bottom))
        im.save('baidu.png')
    except Exception as e:
        print(e)




if __name__ == '__main__':
    username = '18747161745'
    password = 'QWERTY0202'
    zhihulogin(username, password)