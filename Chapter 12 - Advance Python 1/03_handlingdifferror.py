while(True):
    print("enter e to exit")
    a =input("enter a number:")
    if a == 'e':
        break
    try: 
        a=int(a) 
        c=1/a
        print(c)
    except ValueError as e:
        print("enter a valid input")
    except ZeroDivisionError as e:
        print("you cant divide by 0")
print("code ends here")