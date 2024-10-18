#打开,关闭,读,写
#open()函数:open(name,mode,encoding)
"""
name:文件名的字符串,可以包含文件的具体路径
mode:打开模式:只读r,写入w,追加a
encoding:编码格式(UTF-8)
"""
import time

f=open('D:/PythonhSoftware/test.txt','r',encoding="UTF-8")#f是实例化的对象
print(type(f))
#读取函数-read(num),num-读取的字节,无参表示读取所有数据
#readlines()是读取所有行的数据,返回的是一个list

print(f"{f.read(10)}")#连续两次的read会断点,下一次读取会继续去读
print(f"{f.read()}")#读文件相当于有个小指针
print('*********************')
print(f.readlines())
#reline()读一行
print('*********************')
f_1=open('D:/PythonhSoftware/test.txt','r',encoding="UTF-8")#f是实例化的对象

print(f_1.readline())
#用for循环也可以读取,一次读一行
print('*********************')
for line in open("D:/PythonhSoftware/test.txt",'r'):
    print(line,end='')
print()
#文件的关闭
#time.sleep(200000)#程序到此断点,休眠多少时间
f.close()
f_1.close()
#with open() as f操作
with open('D:/PythonhSoftware/test.txt','r',encoding='UTF-8') as f:#一键赋值,在下面的块操作,会主动关闭文件
    for line in f:
        print(line,end='')


