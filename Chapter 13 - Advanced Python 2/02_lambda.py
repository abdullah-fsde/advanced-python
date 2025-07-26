def func(a):
    return a + 10
a = 40
print(func(a))
print("easy aternate method\n")
func = lambda a: a+10
square = lambda a: a*a
sum = lambda a,b,c: a+b+c
a=5
print(func(a))
print(square(a))
print(sum(a,2,3))