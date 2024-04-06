#CHECK WHEATHER A NUMBER IS A ODD NUMBER OR A EVEN NUMBER - 
sankhya=input("enter the sankhya to check =")
if sankhya!="" and sankhya.isdigit()==True:
    num=int(sankhya)
    if num%2==0:
        print(sankhya,"is a even number")
    else:
        print(sankhya,"is a odd number")
else:
    print("invalid input hai boss....integer value daalo")