"""
元组Tuple定义使用小括号（）来定义
元组Tuple在定义量后不可修改
"""
#定义一个元组my_tuple
my_tuple_type1=("Apple","banana")#空元组
my_tuple_type2=tuple("Orange")
#tuple支持index查询下标
print(my_tuple_type1.index("Apple"))#根据内容查找下标
#tuple支持len函数获取长度
print(len(my_tuple_type1))
#循环和list一致都可以使用for和while循环

#count方法也可以使用
print(my_tuple_type1.count("Apple"))
#元组内部内容不可修改，但是要是tuple里面有list可以对list更改
my_tuple_type3=(21,22,[12,2121])
print(my_tuple_type3)
my_tuple_type3[2][0]=20
print(my_tuple_type3)



