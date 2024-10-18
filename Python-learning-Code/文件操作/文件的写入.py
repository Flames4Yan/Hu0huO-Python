#打开文件
f=open('D:/PythonhSoftware/文件写入.md','w')#不存在文件的时候会创建,存在会清空
#文件写入
f.write("hello worldssss")#覆盖了
#内容刷新
f.flush()
f.close()#内置flush功能
"""
调用write并没有写入,要刷新才能真正写入内容
但是不要重复调用flush会降低效率
一般是写完所有内容再刷新
"""