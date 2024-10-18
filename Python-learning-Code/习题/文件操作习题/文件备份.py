f=open("D:/PythonhSoftware/bill.txt",'r',encoding='UTF-8')
file=f.readlines()
copyf=open("D:/PythonhSoftware/billcopy.txt",'w',encoding='UTF-8')#还是要记得把编码方式写进去,不然要乱码
#copyf.write(str(file))#如果直接转换成str形式去输入,就没有\n的转换了就把元组内容输入进去了
for line in file:
    copyf.write(line)#一行一行以元组的形式进去,可以吧缩进也copy进去
copyf.close()
f.close()


