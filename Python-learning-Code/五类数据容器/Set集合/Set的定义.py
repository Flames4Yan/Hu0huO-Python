"""
集合的相关定义和相关操作
"""

my_set={"HUO","HUO",1,2,3}#无序，不重复
print(my_set)
set_empty=set()#空集合的定义

#因为是无序的所以不能用下标去访问
#集合不属于序列，但允许修改
my_set.add("Python")
print(my_set)
#移除元素
my_set.remove(1)
print(my_set)
#随机取出元素
print(my_set.pop())
#集合清空
my_set.clear()#全部清空


#取两个集合的差集A-B
#A集合不变，B集合不变
set_a={1,2,3}
set_b={2,3,4}
set_c=set_a.difference(set_b)#A有B没有
print(set_c)
#消除差集A减去和B相同的元素
#A变化，B不变
set_a.difference_update(set_b)
print(set_a)
#求并集
#A集合不变，B集合不变
set_c=set_a.union(set_b)
print(set_c)
#len函数求集合长度


#集合的遍历，不能用while循环去遍历
#只能用for循环
for element in set_c:
    print(element,end=" ")

