import ssl
import os
import sys
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
ssl._create_default_https_context = ssl._create_unverified_context

searchKey = input('Search Keyword : ')

# 절대경로로 저장할 시, txt 파일에 주소를 저장 먼저 하기. (주소를 숨기기 위해서)
filename = "path.txt"
if os.path.exists(filename):
    f = open(filename, 'r')
    line = f.read()
    path = f"{line}/{searchKey}/images"
else:
    # 상대경로
    print("Ther is no path file. Save in this project.")
    path = f"./imgs/{searchKey}/images"


try:
    # 중복되는 폴더 명이 없다면 생성
    if not os.path.exists(path):
        os.makedirs(path)
    # 중복된다면 문구 출력 후 프로그램 종료
    else:
        print('이전에 같은 [검색어, 이미지 수]로 다운로드한 폴더가 존재합니다.')
        sys.exit(0)
except OSError:
    print ('os error')
    sys.exit(0)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element("name", "q")

elem.send_keys(searchKey)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    selector = ".mye4qd"
    selector = ""
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, selector).send_keys(Keys.ENTER)
        except:
            break
    last_height = new_height

# 이건 구글 작은 사진들 모으는거고 클래쓰 두개 뛰어쓰면 안된다!
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
print(images)

count = 1
for image in images:
    try:
        print(count)
        image.click()
        time.sleep(0.5)
        # 크롤링이 안될시 xpath를 한번 수정해봐라
        xpath = r'//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]'
        imgUrl = driver.find_element(
            By.XPATH,
            xpath
        ).get_attribute("src")
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')
        ]
        urllib.request.install_opener(opener)
        if searchKey == "눈사람": # snowman 노래 및 연예인도 있어서 한글로 검색 후 영어로 저장.
            urllib.request.urlretrieve(imgUrl, f'{path}/{searchKey}/snowman{str(count)}.jpg')
        else:
            urllib.request.urlretrieve(imgUrl, f'{path}/{searchKey}{str(count)}.jpg')
        count = count + 1
        if count > 500:
            break
    except Exception as e:
        #print('e : ', e)
        pass

driver.close()