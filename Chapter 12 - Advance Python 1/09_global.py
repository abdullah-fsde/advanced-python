a = 50#global variable
def func1():
    a=5#local variable
    print(f"printing local variable a :{a}")
func1()
print(f"printing global variable a :{a}")
b = 55
def func2():
    global b
    print(f"prints global b: {b}")
    b=10#the global b is changed to 10 now
    print(f"prints global variable b : {b}")
func2()
print(f"the global b is : {b}")
