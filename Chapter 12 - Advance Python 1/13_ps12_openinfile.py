while True:
    a = input("enter e to exit or something else to run the code:")
    if a == 'e':
        break
    try:
        print("trying to print file1")
        with open("file1.txt", 'r') as f:
            b = f.read()
            print(f"{b}\n")  
    except Exception as e:
        print(f"there was an error due to this file was not created ever:{e}")     
    try:
        print("trying to print file2")
        with open("file2.txt", 'r') as f:
            c = f.read()
            print(f"{c}\n")
    except Exception as e:
        print(f"there was an error due to this file was not created ever:{e}")
    try:
        print("trying to print file3")
        with open("file3.txt", 'r') as f:
            d = f.read()
            print(f"{d}\n")
    except Exception as e:
        print(f"there was an error due to this file was not created ever:{e}")
print("Done , Ready for next execution")