#return A,B
def test_return():
    return 1,True,2
x,y,z=test_return()#必须要全部一一对应
print(x,y,z)