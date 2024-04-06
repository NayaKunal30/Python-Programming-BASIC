#FACTORIAL OF A GIVEN NUMBER :
sankhya=input("enter the sankhya to find its factorial =")
if sankhya!="" and sankhya.isdigit()==True:
    num=int(sankhya)
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial of the number",num,"is",fact)
else:
    print("INAVLID INPUT HAI BOSS ! integer value daalo")
    