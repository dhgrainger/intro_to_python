#global variable
x = 6

def example():
    #local variable
    z = 5
    print(z)

def example2():
    z = 7
    print(z)
    print(x)
#    Cant modify global variable    
#    x+=1
#    print(x)
#    You can set local variable

    y = x+1
    print(y)

def example3():
    global x
    x +=1
    print(x)
