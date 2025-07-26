try:
    a = int(input("enter a number :"))
    c = 1/a
    print(f"{a} divided by 1 is {c}")
except Exception as e:
    print(e)
    if e:
        print("we were not successful")
    exit()
finally:
    print("we are done")#this part will run even if the program is ended and even if the exception is raised or even if the try runs