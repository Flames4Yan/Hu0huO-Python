

#捕获第二类异常
"""
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""
#例子
try:
    f=open("D:/PythonhSoftware/abc.txt",'r',encoding='UTF-8')
except:
    print("出现错误")
    f=open("D:/PythonhSoftware/abc.txt",'w',encoding='UTF-8')
#捕获指定异常
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')
#捕获多个异常
try:
    print(1/0)
except(NameError,ZeroDivisionError) as e:
    print('出现变量未定义或者除以0异常错误')
#捕获所有异常的第二种法
try:
    print(1/0)
except Exception as e:
    print('出现异常')
#异常else
try:
    print(1)
except:
    print(e)
else:#无异常的输出
    print('没有异常')
#异常finally表示的是无论是否出现异常都要执行的代码
try:
    f=open('D:/123.txt','r','UTF-8')
except:
    print('异常')
else:
    print('没有异常')
finally:
    print('Finnally')
    f.close()