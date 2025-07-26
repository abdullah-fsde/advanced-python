greater_than_10 = lambda a: True if a > 10 else False
#'''def func(num):
# if num>10:
# return True
# else:
# return False'''

list1=[1,2,3,4,5,15,84,9,3198,46,161]
print(list(filter(greater_than_10,list1)))
greater_than_40 = lambda a: a > 40
print(list(filter(greater_than_40,list1)))
