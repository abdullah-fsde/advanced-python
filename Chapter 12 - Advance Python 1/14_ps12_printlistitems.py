list1=[11,12,13,14,15,16,17,18,19,20]
for index,item in enumerate(list1):
    if index == 2 or index==4 or index==6:
        print(f"index {index+1} is {item}")