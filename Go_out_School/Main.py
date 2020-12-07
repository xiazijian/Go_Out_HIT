import time
import os
from selenium import webdriver
import selenium.webdriver.support.ui as ui

def init_webdriver(executable_path):
    driver = webdriver.Chrome(executable_path=executable_path)
    return driver

def login(driver,id,password):
    driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/button[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[1]/input").send_keys(
        id)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[2]/input[1]").send_keys(
        password)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[5]/button").click()


# 不想做日期判断，此处简化为输入想出校的第一天-最后想出去的天
def run(begin_date,end_date,season,driver):
    #date_string = "2020年12月" + str(i) + "日"
    date_ = "2020-12-"
    # 出入校申请
    driver.find_element_by_xpath("/html/body/div[1]/div[5]/a[3]").click()
    for i in range(begin_date,end_date+1):
        wait = ui.WebDriverWait(driver, 5)
        wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div[2]/a/div"))
        driver.find_element_by_xpath("/html/body/div[2]/a/div").click()# 新增
        date = date_+str(i)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[9]/div/label[1]").click()  # 勾选临时出校
        js = "document.getElementById('rq').removeAttribute('readonly')"
        driver.execute_script(js)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[13]/input").send_keys(date)  # 填写日期
        driver.find_element_by_xpath("/html/body/div[1]/div/div[15]/textarea").send_keys(season)  # 出校理由
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/input").click()  # 勾选一堆东西
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[3]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[5]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[6]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[7]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[8]/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[9]/input").click()
        driver.find_element_by_xpath("/html/body/div[6]").click()  # 提交
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[10]/div[3]/a[2]").click()
        print(date+"申请成功")


if __name__ == '__main__':
    # 换成自己的路径
    executable_path = r"D:\chromeDownload\chromeDriver\chromedriver.exe"
    driver = init_webdriver(executable_path)
    login(driver,"学号","密码")
    run(28,31,"吃吃",driver)


