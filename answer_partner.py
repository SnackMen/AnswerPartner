import os
import pytesseract
import time
from PIL import Image
from selenium import webdriver


def screen_shots():
    os.system('adb shell screencap -p /sdcard/autosearch.png')
    os.system('adb pull /sdcard/autosearch.png .')


def screen_pic():
    screen_shots()
    img = Image.open('autosearch.png')
    w, h = img.size
    # 依据图片尺寸定的截图区间
    im1 = img.crop((0, h // 10, w, h // 4))
    print(h // 3)
    im1.save('autosearch.png')


def query_sub():
    # screen_pic()
    image = Image.open('autosearch.png')
    code = pytesseract.image_to_string(image, lang='chi_sim')
    print('题目是：{}'.format(code.replace('\n', '').split('.')[1].strip(' ')))

    # 搜索网站的地址
    # url = 'https://www.google.com'
    url = 'http://www.baidu.com'
    # chromedriver.exe安装位置
    browser = webdriver.Chrome('E:\\soft\\chrome\\chromedriver.exe')
    # 输入url
    browser.get(url)
    # 休眠1s
    # time.sleep(1)
    # 谷歌搜索
    # browser.find_element_by_id('lst-ib').clear()
    # # 去除字符两边空格以及题目序号
    # browser.find_element_by_id('lst-ib').send_keys(code.replace('\n', '').split('.')[1].strip(' '))
    # browser.find_element_by_name('btnK').click()

    # 百度搜索
    browser.find_element_by_id('kw').clear()
    # 去除字符两边空格以及题目序号
    browser.find_element_by_id('kw').send_keys(code.replace('\n', '').split('.')[1].strip(' '))
    browser.find_element_by_id('su').click()
    print('搜索成功!')


if __name__ == '__main__':
    start = time.clock()
    query_sub()
    print(time.clock() - start)
    input()
