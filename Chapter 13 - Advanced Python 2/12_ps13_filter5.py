func=lambda a: a%5==0
list1=[12,14,15,22,24,25,60,75,92,99,100]
print(list(filter(func,list1)))