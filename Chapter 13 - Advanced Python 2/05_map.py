square = lambda a: a*a
list1 = [2,3,4]
print("Method 1 ")
list2=[]
for item in list1:
    list2.append(square(item))
print(list2)
print("\n")
print("Method 2")
print(list(map(square,list1)))
print('\n')
print("just for fun")
print(tuple(map(square,list1)))
