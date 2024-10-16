"""
字符串无法修改
"""
#定义
my_str="huohuo"
valeue=my_str[2]#访问某个下标

#查找特定字的下标
print(my_str.index('o'))

#.replace(字符串1,字符串2)
new_my_str=my_str.replace("huo","HUO")#把子串全部替换了
print(new_my_str)
#split方法,根据某个字符，将所有该字符处分割
my_str_else="hello python"

my_str_else_list=my_str_else.split(" ")#输出的是列表list
print(my_str_else_list)
#strip方法,产生新的字符串,不带参数去掉首尾空格,带参数去掉正反字符串只能是,首尾出现的字符串
my_str_1="ok lhhell00 lohl ko"
new_my_str_1=my_str_1.strip("ko")#传入字符串的串也要被去除
print(new_my_str_1)
#len函数和.count一样适用

for index in my_str_1:
    print(index)













