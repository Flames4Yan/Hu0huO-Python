"""
序列指的是：内容连续、有序，可使用下标索引的一类数据容器
list tuple str都可视为序列
"""
#切片，取子序列

#语法： 序列[起始下标:结束下标:步长]
list=[1,2,3,4,5,6,7]

new_list=list[0:5:1]
print(new_list)
#步长为负数则反向取值