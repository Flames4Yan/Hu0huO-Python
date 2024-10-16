# 定义一个列表
my_list=[21,25,21,23,22,20]
#追加一个数字31，到列表尾部
my_list.append(31)
#追加一个新列表[29,33,30],到列表尾部
my_list.extend([29,33,30])
#取出第一个元素
print(my_list[0])
#取出最后一个元素
print(my_list[-1])
#查找元素31，在列表中的下标位置
print(my_list.index(31))
#获得长度
len(my_list)
#列表清除
my_list.clear()
#元素个数
print(my_list.count(31))#用.count一定要被使用，否则会报错
#插入
my_list.insert(0,12)
#查找并返回坐标
print(my_list.index(12))
#删除元素
del my_list[0]
my_list.pop(1)
my_list.remove(12)#指定元素删除，从前到后的删除

