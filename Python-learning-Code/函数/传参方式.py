
def function1(name,age,gender):
    print(f"{name},{age},{gender}")
    return True
#位置参数:属性和定义的参数个数必须一致
function1(1,2,3)
#关键字传参:可以和位置传参混用,但是位置参数要放在关键词参数的前面
function1(name=1,gender=3,age=2)
#缺省参数
def user_info(name,age,gender="男"):#默认参数要放在最后面!!!!!
    print(f"{name},{age},gender:{gender}")
    return  True
user_info(1,2)#不传参数

#不定长参数

#-位置传递
def function2(*args):#将args设定为以元组(tuple)
   print(type(args),args)
   return True
#-关键字传递
def function(**kwargs):#传的字典进去以kv进去
    print(type(kwargs),kwargs)
    return True










