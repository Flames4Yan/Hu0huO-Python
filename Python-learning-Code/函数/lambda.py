#lambda关键字可以定义没有名字的函数,一次性使用的lambda匿名函数
def test_func(compute):
    result=compute(1,2)
    print(result)

test_func(lambda x,y:x+y)#函数参数:函数体(一行代码)
