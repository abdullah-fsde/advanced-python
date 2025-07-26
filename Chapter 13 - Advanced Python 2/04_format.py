name = "abdullah"
age = 22
role = "FSDE"
line = f"The man named {name} is {age} age and aspiring to be a {role}"
print(line)
line2 = "The man named {} is {} age and aspiring to be a {}".format(name , age , role)
print(line2)
line3 = "The man named {} is {} age and aspiring to be a {}".format(age,role,name)
print(line3)
line4 = "The man named {2} is {1} age and aspiring to be a {0}".format(name,age,role)
print(line4)
line5 = "The man named {1} is {1} age and aspiring to be a {2}".format(name,age,role)
print(line5)