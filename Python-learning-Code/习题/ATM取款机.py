acount=0
name="Hu0huO"
choose=0
def atm_get_acount():
    print("---------------查询余额---------------")
    global acount
    print(f"{name},您好，您的余额剩余：{acount}")

def deposit():
    global acount
    print("-----------------存款----------------")
    in_money=int(input("您存款的金额为："))
    acount=acount+in_money
    print(f"{name},您好，您的余额剩余：{acount}")


def atm_withdraw():
    global acount
    print("-----------------取款----------------")
    out_money=int(input("您取款的金额为："))
    if acount>=out_money:
        acount = acount - out_money
    else:
        print("很抱歉，您的余额不足")
    print(f"{name},您好，您的余额剩余：{acount}")


def atm_menu():
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
        which_function = int(input("请输入你的选择："))
        if which_function == 1:
            atm_get_acount()
        elif which_function == 2:
            deposit()
        elif which_function == 3:
            atm_withdraw()
        elif which_function == 4:
            return None
    while True:


#菜单运行
atm_menu()
