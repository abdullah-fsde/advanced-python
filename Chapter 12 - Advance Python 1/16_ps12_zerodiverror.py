def divide(a,b):
    try:
        print("trying the number division")
        c=int(a)/int(b)
        print(c)
    except ZeroDivisionError as e:
        print("the denominator cannot be zero")
a = input("enter the numerator :")
b = input("enter the denominator :")
d=divide(a,b)
