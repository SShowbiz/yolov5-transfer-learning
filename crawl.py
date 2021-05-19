import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

keyword = input("검색할 키워드를 입력하세요 : ")
num = int(input("개수 : "))

driver = webdriver.Chrome('./chromedriver')
driver.get('http://www.google.co.kr/imghp?hl=ko')

# Search word
search_box = driver.find_element_by_name("q")
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)


# Search setting
detail_setting_box = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div/div")
detail_setting_box.click()
time.sleep(1)
time_setting = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[2]/c-wiz[1]/div/div/div[1]/div/div[4]/div/div[1]")
time_setting.click()
time.sleep(1)
time_setting_selection = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[2]/c-wiz[1]/div/div/div[3]/div/a[1]/div/span")
time_setting_selection.click()

# Get all images
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

count = 0
for image in images:
    try:
        print('covy')
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div/div/div/div[2]/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "./crawling-images/" + keyword + str(count) + ".jpg")
        count += 1
        print(count)
        if count == num:
            break
    except:
        pass
driver.close()
