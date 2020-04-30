from selenium import webdriver  # 引入库
import time
driver = webdriver.Chrome()     #打开谷歌浏览器，与浏览器建立了会话。driver (变量) = 会话
driver.get("http://www.elong.com/") #（等待网页加载完才运行后面的代码）    要在这个会话的基础上，访问一个网站。功能库-提供了各种网页操作的API--方法。访问网页的方法 -- get（）
time.sleep(1)
ele = driver.find_element_by_xpath('//input[@data-bindid="city"]') #查找元素  ele = 找到的元素
ele.click()     #点击操作--点击城市输入框--弹出城市选择框
time.sleep(2)   #等待两秒，因为接下来的操作的元素是动态出现的。

#输入操作 ：ele.send_keys("输入的内容")
#获取它的属性；ele.get_attribute("属性名称")
#获取它的文本内容：ele.text()

driver.find_element_by_xpath('//li[@title="广州"]').click()    #选择热门城市当中的广州
time.sleep(1)
#选择入住日期
ele = driver.find_element_by_xpath('//input[@data-bindid="checkIn"]')
ele.clear()
ele.send_keys("2020-04-30")
time.sleep(1)
#把弹出的日期选择框关掉
driver.find_element_by_xpath('//div[@id="domesticDiv"] //dt[text()="目的地"]').click()
#选择退房日期
ele = driver.find_element_by_xpath('//input[@data-bindid="checkOut"]')
ele.clear()
ele.send_keys("2020-05-03")
time.sleep(1)
#把弹出的日期选择框关掉
driver.find_element_by_xpath('//div[@id="domesticDiv"] //dt[text()="目的地"]').click()
time.sleep(2)
#点击搜索按钮
driver.find_element_by_xpath('//span[@data-bindid="search"]').click()
#跳转到新的页面了，等待新的页面内容加载
time.sleep(7)
#获取酒店的名字、酒店的价格、酒店的评价  find_find_elements_by_xpath---获取匹配到的表达式的所有元素，eles得到的是个列表
#python用来存放多个数据--列表/字典/元组/集合
#文件操作--我的酒店数据.txt
#读写操作。创建一个文件，写入数据，然后关闭。
#open--文件操作
#打开文件时，指明写入方式，以及编码格式utf-8
fs = open("我的酒店数据.txt","w",encoding="utf-8")
#write- w 可写入模式，自动覆盖之前写的内容。文件不存在时会自动创建。若存在则直接写入。
#write 在写的时候不会自动换行。换行：\n
name = driver.find_elements_by_xpath('//span[@class="info_cn"]')      #所有酒店的名称元素
price = driver.find_elements_by_xpath('//span[@class="h_pri_num "]')  #所有酒店的价格元素
preview = driver.find_elements_by_xpath('//i[@class="t20 c37e"]')     #所有酒店的评分元素
#从三个列表当中，每个值都要取出来
#遍历从头到尾，每一个成员都要访问
for i in range(20) :
    print(name[i].text,price[i].text,preview[i].text)
    fs.write(name[i].text+"   "+price[i].text+"   "+preview[i].text+"\n")
    
"""
for 变量 in 列表 ： （在列表当中，取每一个成员，给到变量）
取到每一个成员，会去做的事情
取到每一个酒店，都要去拿酒店的名字、评分和价格。
"""
#关闭文件
fs.close()
#关闭浏览器，关闭本次会话
time.sleep(10)
driver.quit()






