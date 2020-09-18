import time
from selenium import webdriver
import selenium 
from selenium.webdriver.chrome.options import Options

def tryPick(className,driver):
    try:
        # ele = driver.find_element_by_link_text(className)
        ele = driver.find_element_by_xpath("//td[contains(.,'{}')]".format(className))

    except selenium.common.exceptions.NoSuchElementException as e:
        print("Can't find class: "+ className)
        time.sleep(3)
        ele = driver.find_element_by_link_text(className)
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

chrome_options = Options()

chrome_options.add_experimental_option("debuggerAddress","localhost:9222")
chrome_driver = "chrome_driver"

driver = webdriver.Chrome(chrome_options=chrome_options)
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
ii=0
# xwjck=["现代集成电路分析方法"]
xwjck=[]
xwzyk=["数字信号处理VLSI设计"]
# zyxxk=["射频微波通信电路设计基础","微电子系统封装","半导体测试技术"]
# zyxxk=["射频微波通信电路设计基础"]

zyxxk=[]
while True:
    if ii %20 ==0:
        driver.refresh()
        time.sleep(1)
    if ii% 100 == 0:
        time.sleep(3)
    try:
        ele = driver.find_element_by_link_text("学科专业课")
        ele.click()
        time.sleep(1)
        for cls in xwjck:
            if tryPick(cls,driver):
                wxjck.remove(cls)

        ele = driver.find_element_by_xpath("//li[contains(.,'学位专业课')]")
        ele.click()
        time.sleep(1)
        for cls in xwzyk:
            if tryPick(cls,driver):
                xwzyk.remove(cls)

        ele = driver.find_element_by_xpath("//li[contains(.,'专业选修课')]")
        ele.click()
        time.sleep(1)
        for cls in zyxxk:
            if tryPick(cls,driver):
                zyxxk.remove(cls)
    except selenium.common.exceptions.NoSuchElementException as e:
        print(e)
        ii = 0
        continue
    ii = ii+1

def isFull(className,driver):
    ele = driver.find_element_by_link_text(className)
    pare = ele.find_element_by_xpath("./..")
    try:
        # pare.find_element_by_xpath("//span[contains(.,'已满')]")
        ele = pare.find_element_by_link_text("选课")
    except Exception:
        return False
    time.sleep(1)
    return True     

