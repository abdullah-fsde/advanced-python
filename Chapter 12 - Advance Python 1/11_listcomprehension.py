list1 = [1,2,3,4,5,6,7,8,9,10]
b=[]
for item in list1:
    if item%2==0:
        b.append(item)
print(b)
#other method for the same using list comprehension method
c=[item for item in list1 if item%2!=0]
print(c)
