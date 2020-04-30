# stuDictList = [
#     {"name": "张飞", "power": 96, "tellegent": 30},
#     {"name": "诸葛亮", "power": 140, "tellegent": 199},
#     {"name": "周瑜", "power": 79, "tellegent": 93},
#     {"name": "赵云", "power": 97, "tellegent": 86},
# ]

# print("原始的数据\n{}".format(stuDictList))

# print("开始按照武力排序,由小到大")
# stuDictList.sort(key=lambda stu: stu["power"])
# print("排好序后新数据\n{}".format(stuDictList))

# print("开始按照智力值排序,由大到小")

# def func(ele):
#     return ele["tellegent"]

# new_list = sorted(stuDictList,key = func, reverse=True)
# print("排序结果{}".format(new_list))

# tuples = [("john", "A", 15),("jane", "B", 12),("dave", "B", 10)]
# new_tuples = sorted(tuples, key=lambda x: x[2])                  #sorted函数能对所有可迭代的对象（是列表、元祖、字典等可迭代对象）进行排序操作，sorted()函数不会改变原来的对象，而是会返回一个新的已经排序好的对象。
# print(new_tuples) 
# print(tuples)

# tuples.sort()                                                    #sort是在直接原来的列表上排序改变顺序，修改list本身，不会创建新的list，也不会返回新的list,没有返回值。sort方法只能用于列表，不能对字典、元祖等其他可迭代对象进行排序。
# print(tuples)



# names = ['皮卡丘']
# dic = {'name': '妙蛙花'}
# skills = ('十万伏特', '飞叶快刀')
# text = ('我是{0[0]}，我会{2[0]}。我是{1[name]},我会{2[1]}。'.format(names,dic,skills))
# print(text)



