"""
my_list=["黑马程序员","传智博客","黑马程序员","传智博客","itheima","itcast","itheima","itcast","best']

"""
my_list=["黑马程序员","传智博客","黑马程序员","传智博客","itheima","itcast","itheima","itcast","best"]
#定义一个空集合
set_empty=set()
#for循环遍历,将for循环中的列表元素添加到集合
for index in my_list:
    set_empty.add(index)
#打印输出
print(set_empty)