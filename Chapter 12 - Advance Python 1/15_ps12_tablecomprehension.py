n=int(input("enter a number for table to generate :"))
list=[f"{n}x{i}={n*i}" for i in range (1,11)]
print(list)