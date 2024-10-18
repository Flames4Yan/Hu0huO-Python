"""
给定一个字符串“itheima itcast boxuegu”
-统计有字符串内有多少个“it”字符
-将字符串内的空格，全部替换为字符:"|"
-并按照“|”进行字符串分割，得到列表
"""
my_str="ithema itcast boxuegu"
print(my_str.count("it"))

change_my_str=my_str.replace(" ","|")
print(change_my_str)

my_list=change_my_str.split("|")

print(my_list)
