"""
#映射的关系,根据某个值去找对应的值
#查询的意思
"""

#定义,键值对
my_dict={
    "huohuo":21,
    "age":18,
    "height":21
}
#定义空字典
my_dict_empty=dict()

my_dict_empty_else={}

#字典不能重复,跟集合一致

print(my_dict)#打印字典

#字典更新和新增

my_dict_empty["huohuo"]=18
print(my_dict_empty)

#删除元素用pop方法

my_dict.pop("huohuo")
print(my_dict)
#清空函数用clear方法

#获取全部key,keys()
keys=my_dict.keys()
print(keys)
#方式1
for key in keys:
    print(f"key:{key}")
    print(f"value{my_dict[key]}")
#方式2
for key in my_dict:
    print(f"key:{key}")
    print(f"value{my_dict[key]}")
#不使用while循环来遍历
#获取长度用len()函数
print(len(my_dict))
"""
#容纳多个数据
#可以容纳多个数据
#key不可重复
#可修改
"""














