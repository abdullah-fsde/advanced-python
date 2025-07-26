try:
    a = int(input("enter a number :"))
    c = 1/a
    print(f"{a} divided by 1 is {c}")
except Exception as e:
    print(e)
    if e:
        print("we were not successful")
else:
    print("we were successful buddy")