my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str="adcdefg"
my_set={1,2,3,4,5}
my_dict={'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
#len求元素个数
#max最大元素
#前面的三类不用讲
#set和dict比较大小

#类型转换:容器转换列表
#-list(容器)
print(list(my_dict))#需要注意的
print(list(my_str))#需要注意到

#类型转换:容器转元组
#同理list转换

#类型转换:容器转换字符串
print(str(my_list))
print(str(my_tuple))
print(str(my_str))
print(str(my_set))
print(str(my_dict))
#类型转换:容器转集合
print(set(my_str))#需要注意的无序
print(set(my_dict))#不保留value
#没办法转换成dict,因为字典要求的内容是键值对
#sorted函数
#sorted(容器,[reverse=False])









