table=lambda a,i:a*i
a=7
list1=[]
for i in range(1,11):
    b = f"{a} x {i} = {table(a,i)}"
    list1.append(b)
print(list1)
c = "\n".join(list1)
print(c)