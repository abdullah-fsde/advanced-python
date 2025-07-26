name = input("enter your name :")
def increment(num):
    try:
        print("Trying to increment your input")
        return int(num)+1
    except:
        raise ValueError(f"This is not the right thing to enter plzz enter a number {name}")
num = input("enter a number to increment with one :")
a = increment(num)
print(a)