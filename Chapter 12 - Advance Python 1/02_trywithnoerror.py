try:
    a = int(input("enter a number:"))
    print(1/a)
except Exception as e:#you need not write exception as e too for some cases 
    print('error occured')
    # print(e)   this will only print whats the error but its not really necessary