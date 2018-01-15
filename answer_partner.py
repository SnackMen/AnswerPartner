import os
import pytesseract
import time
import requests

from PIL import Image
from bs4 import BeautifulSoup


def screen_shots():
    time1 = time.clock()
    os.system('adb shell screencap -p /sdcard/autosearch.png')
    os.system('adb pull /sdcard/autosearch.png .')
    print('截图：' + str(time.clock() - time1))


def screen_pic():
    # screen_shots()
    time1 = time.clock()
    img = Image.open('autosearch.png')
    w, h = img.size
    # 依据图片尺寸定的截图区间
    im1 = img.crop((0, h // 10, w, h // 3 * 2))
    im1.save('autosearch.png')
    print('裁剪：' + str(time.clock() - time1))


def query_sub():
    screen_pic()
    image = Image.open('autosearch.png')
    code = pytesseract.image_to_string(image, lang='chi_sim')
    code = code.replace(' ', '').split('\n\n')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    url = 'http://www.baidu.com/s'
    question = code[0].replace('\n', '').split('.')[1]
    print(question)
    for ans in code[1:]:
        payload = question + '  ' + ans
        payload = {'wd': payload}
        result = requests.get(url=url, params=payload, headers=headers)
        soup = BeautifulSoup(result.text, 'html.parser')
        tags = str(soup.find_all('div', class_='nums')[0])
        res = list(filter(str.isdigit, tags))
        print('{}:[{}]'.format(ans, ''.join(res)))


if __name__ == '__main__':
    start = time.clock()
    query_sub()
    print(time.clock() - start)
    input()
