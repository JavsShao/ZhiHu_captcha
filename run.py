import time
import tesserocr
from PIL import Image
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
    time.sleep(3)
    try:
        # 验证码所在的位置
        element = driver.find_element_by_class_name('Captcha-englishImg')
        location = element.location
        print(location)
        size = element.size
        print(size)

        # 计算出元素上下左右位置
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']

        im = Image.open('1.png')
        im = im.crop((left, top, right, bottom))
        im.save('2.png')

        # 打开图片
        image = Image.open('2.png')
        image = image.convert('L')
        threshod = 127
        table = []
        for i in range(256):
            if i < threshod:
                table.append(0)
            else:
                table.append(1)
        image = image.point(table, '1')
        result = tesserocr.image_to_text(image)
        print('验证码是：', result)
        driver.find_element_by_class_name('SignFlowInput-errorMask').send_keys(result)
        driver.find_element_by_class_name('SignFlow-submitButton').click()
        time.sleep(10)


    except Exception as e:
        print('出现错误了～')
        print(e)




if __name__ == '__main__':
    username = '18747161745'
    password = 'QWERTY0202'
    zhihulogin(username, password)