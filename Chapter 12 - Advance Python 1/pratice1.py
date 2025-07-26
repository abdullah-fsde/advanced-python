try:
    a =int(input("enter a number:"))
    c=1/a
    print(c)
except ValueError as e:
    print("enter a valid input")
except ZeroDivisionError as e:
    print("you cant divide by 0")
print("code ends here")