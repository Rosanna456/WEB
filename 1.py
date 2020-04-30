from selenium import webdriver
import time

# 打开谷歌浏览器，与浏览器建立了会话。
# driver变量 = 会话
driver = webdriver.Chrome()
driver.get("http://www.elong.com/")
time.sleep(1)

# 点击城市输入框，弹出城市选择
ele = driver.find_element_by_xpath('//input[@data-bindid="city"]')  # ele = 我找到的元素
ele.click()
time.sleep(2)

# 选择热门城市当中的，广州
driver.find_element_by_xpath('//li[@title="广州"]').click()
time.sleep(1)
# 选择入住日期
ele = driver.find_element_by_xpath('//input[@data-bindid="checkIn"]')
ele.clear()  # 清空输入框的内容
ele.send_keys("2020-04-30")
time.sleep(1)
# 把弹出的日期选择框，关掉。
driver.find_element_by_xpath('//div[@id="domesticDiv"]//dt[text()="目的地"]').click()

# ************************   作业需要完成部分  ***************************
#  ===== 1、选择退房日期 ======
ele = driver.find_element_by_xpath('//input[@data-bindid="checkOut"]')
ele.clear()  # 清空输入框的内容
ele.send_keys("2020-05-03")
time.sleep(1)
# 把弹出的日期选择框，关掉。
driver.find_element_by_xpath('//div[@id="domesticDiv"]//dt[text()="目的地"]').click()

#  ===== 2、点击搜索按钮 ======
time.sleep(0.5)
driver.find_element_by_xpath('//span[@data-bindid="search"]').click()

#  ===== 3、跳转到新的页面了，等待新的页面内容加载  ======
time.sleep(7)

#  ===== 4、获取酒店的名字、酒店的价格、酒店的评价 ======‘
hotel_name = driver.find_element_by_xpath('//span[@class="info_cn"]').text  # 酒店名字
hotel_price = driver.find_element_by_xpath('//span[@class="h_pri_num "]').text
hotel_review = driver.find_element_by_xpath('//i[@class="t20 c37e"]').text
print("酒店信息：",hotel_name,hotel_price,hotel_review)

#　===== 5、关闭浏览器，关闭本次会话 ======
time.sleep(10)
driver.quit()


