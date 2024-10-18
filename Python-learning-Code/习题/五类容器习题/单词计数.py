#得到元组是会有\n在末尾的
count=0
with open('D:/PythonhSoftware/word.txt','r',encoding='UTF-8') as f:
    f_1=f.readlines()
    print(f_1)
    for line in f_1:
        line=line.strip()
        print(line)
        count+=line.count("itheima")
print(count)