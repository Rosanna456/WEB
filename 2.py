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
# hotel_name = driver.find_element_by_xpath('//span[@class="info_cn"]').text  # 酒店名字
# hotel_price = driver.find_element_by_xpath('//span[@class="h_pri_num "]').text
# hotel_review = driver.find_element_by_xpath('//i[@class="t20 c37e"]').text
# print("酒店信息：",hotel_name,hotel_price,hotel_review)


# find_elements
# 列表 - 赋值、append方法/列表的遍历-for
# ===== 5、for循环获取当前页面的所有酒店的名字、价格、评价 =======
hotel_names = driver.find_elements_by_xpath('//span[@class="info_cn"]')  # 获取当前页面当中，所有匹配到的酒店名字。
hotel_prices = driver.find_elements_by_xpath('//span[@class="h_pri_num "]')
hotel_reviews = driver.find_elements_by_xpath('//i[@class="t20 c37e"]')

hotel_info = []  # 酒店列表
for index in range(len(hotel_names)): # 遍历匹配到的酒店
    print(hotel_names[index].text, hotel_prices[index].text,hotel_reviews[index].text)
    one_hotel = [hotel_names[index].text, hotel_prices[index].text,hotel_reviews[index].text]
    # ====== 将每一个酒店的信息，存入列表当中。
    hotel_info.append(one_hotel)

print(hotel_info)

# ==========  额外增加的一个：对列表里的元素，根据某一个值来排序  ========
hotel_info.sort(key=lambda s:int(s[1]),reverse=True)

# ======= 6、酒店信息如何写入到文件当中？ ============
fs = open("../酒店数据.txt", "w+", encoding="utf-8")  #在上一级文件夹中创建酒店数据.txt    w+: 打开一个文件用于读写
fs.write("酒店名称      价格  评分\n")
for item in hotel_info:
    fs.write("{}      {}  {}\n".format(*item))
fs.close()

#　===== 5、关闭浏览器，关闭本次会话 ======
time.sleep(10)
driver.quit()
