#函数作为参数传递的例子


def test_func(compute):#compute可以是其他的东西,不一定是compute
    result=compute(1,2)
    print(type(compute))
    print(result)
def multe(x,y):
    return x*y
def compute(x,y):#匿名函数,在外部作用域不显示
    return x+y
#传递的是逻辑,而非数据的传递

test_func(multe)
