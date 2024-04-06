sankhya=input("enter the sankhya to find its multiplication table =")
if sankhya!="" and sankhya.isdigit()==True:
    num=int(sankhya)
    i=1
n=input("enter the limit u want the multiplication table=")
if n!="" and n.isdigit()==True:
    num1=int(n)
    print("the multiplication table of",num,"is-")
    while i<=num1:
        mul=(num*i)
        print(num,"x",i,"=",mul)
        i+=1       
else:
    print("Invalid input hai boss ! integer value daalo...")  
