acount=0
name="Hu0huO"
choose=0
def getAcount():
    print("---------------查询余额---------------")
    global acount
    print(f"{name},您好，您的余额剩余：{acount}")

def deposit():
    global acount
    print("-----------------存款----------------")
    inMoney=int(input("您存款的金额为："))
    acount=acount+inMoney
    print(f"{name},您好，您的余额剩余：{acount}")


def withdraw():
    global acount
    print("-----------------取款----------------")
    outMoney=int(input("您取款的金额为："))
    if acount>=outMoney:
       acount=acount-outMoney
    else:
        print("很抱歉，您的余额不足")
    print(f"{name},您好，您的余额剩余：{acount}")


def menuFunction():
    """


    """
    while True:
      print()
      print("---------------主菜单---------------")
      print(f"{name}，您好，欢迎来到ATM，请选择操作")
      print("查询余额\t[输入1]")
      print("存款   \t[输入2]")
      print("取款   \t[输入3]")
      print("退出   \t[输入4]")
      choose=int(input("请输入你的选择："))
      if choose==1:
         getAcount()
      elif choose==2:
         deposit()
      elif choose==3:
         withdraw()
      elif choose==4:
          return None
#菜单运行
menuFunction()
