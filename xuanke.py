import time
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
import subprocess


def tryPick(className, driver):
    try:
        ele = driver.find_element_by_xpath(
            "//td[contains(.,'{0}')]".format(className))
    except selenium.common.exceptions.NoSuchElementException:
        try:
            ele = driver.find_element_by_link_text(className)
            ele = ele.find_element_by_xpath("./..")
        except selenium.common.exceptions.NoSuchElementException:
            print("Can't find class: " + className)
            time.sleep(3)
            return False

        # ele = driver.find_element_by_xpath(
            # "//td[contains(.,'{0}')]".format(className))
    pare = ele.find_element_by_xpath(".//..")

    try:
        # pare.find_element_by_xpath("//span[contains(.,'已满')]")
        ele = pare.find_element_by_link_text("选课")
        ele.click()
        ele = driver.find_element_by_xpath("//button[contains(.,'确定')]")
        ele.click()

    except Exception as e:
        print(className)
        print(e)
        return False
    print(className+" picked!")
    time.sleep(2)
    return True


# Start chrome
subprocess.Popen(["google-chrome-stable",
                  "--remote-debugging-port=9222",
                  "--user-data-dir=.config/google-chrome/",
                  "--disk-cache-dir=.cache/google-chrome/Default"],
                 stdout=subprocess.DEVNULL,
                 stderr=subprocess.DEVNULL)

# Connect to chrome
chrome_options = Options()

chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
chrome_driver = "chrome_driver"

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://yjsxk.fudan.edu.cn/wsxk/")
while input("If you finished entering you account, please press enter!"):
    pass

print(driver.title)
# ii=1
# while(ii):
#     driver.refresh()
#     time.sleep(2)
#     ii=ii-1
#     #学科专业课
#     ele = driver.find_element_by_link_text("学科专业课")
#     ele.click()
#     # ele = driver.find_element_by_tag_nam("专业选修课")
#     # ele.click()
#     ele = driver.find_element_by_link_text("微电子材料")
ii = 0
政治理论课 = []
第一外国语 = []
专业外语 = []

学位基础课 = []
学位专业课 = ["系统级可编程芯片设计2021202201INFO630047.01"]
专业选修课 = []
# 专业选修课 = ["计算微电子学2020202102INFO830033.01"]
while True:
    if ii % 20 == 0:
        driver.refresh()
        time.sleep(1)
    if ii % 100 == 0:
        time.sleep(3)
    try:
        # 学位公共课
        if 政治理论课 != [] or 第一外国语 != [] or 专业外语 != []:
            ele = driver.find_element_by_link_text("学位公共课")
            ele.click()
            time.sleep(1)
            for cls in 政治理论课:
                if tryPick(cls, driver):
                    政治理论课.remove(cls)

            if 第一外国语 != []:
                ele = driver.find_element_by_xpath("//li[contains(.,'第一外国语')]")
                ele.click()
                time.sleep(1)
                for cls in 第一外国语:
                    if tryPick(cls, driver):
                        第一外国语.remove(cls)

            if 专业外语 != []:
                ele = driver.find_element_by_xpath("//li[contains(.,'专业外语')]")
                ele.click()
                time.sleep(1)
                for cls in 专业外语:
                    if tryPick(cls, driver):
                        专业外语.remove(cls)


        # 专业课选课
        ele = driver.find_element_by_link_text("学科专业课")
        ele.click()
        time.sleep(1)
        for cls in 学位基础课:
            if tryPick(cls, driver):
                学位基础课.remove(cls)

        ele = driver.find_element_by_xpath("//li[contains(.,'学位专业课')]")
        ele.click()
        time.sleep(1)
        for cls in 学位专业课:
            if tryPick(cls, driver):
                学位专业课.remove(cls)

        ele = driver.find_element_by_xpath("//li[contains(.,'专业选修课')]")
        ele.click()
        time.sleep(1)
        for cls in 专业选修课:
            if tryPick(cls, driver):
                专业选修课.remove(cls)
    except selenium.common.exceptions.NoSuchElementException as e:
        print(e)
        ii = 0
        continue
    ii = ii+1


def isFull(className, driver):
    ele = driver.find_element_by_link_text(className)
    pare = ele.find_element_by_xpath("./..")
    try:
        # pare.find_element_by_xpath("//span[contains(.,'已满')]")
        ele = pare.find_element_by_link_text("选课")
    except Exception:
        return False
    time.sleep(1)
    return True
