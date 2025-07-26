while(True):
    print("Press q to exit")
    a=input("enetr a number:")
    if a == 'q':
        break
    try:
        print("trying...")
        a=int(a)
        if a>6:
            print("you entered a number greater than 6")
    except Exception as e:
        print(f"there was an error = {e}")
print("its over")