#ARMSTRONG NUMBER OR NOT ?
sankhya=input("enter a number to check =")
if sankhya!="" and sankhya.isdigit()==True:
    sum=0
    a=int(sankhya)
    temp=int(sankhya)
    while temp>0:
        digit=temp%10
        sum=sum+(digit**3)
        temp//=10
    if a==sum:
        print(a,"is a armstrong number!!")
        print("le chal gaya tera code mauj kar jaake ice cream khale ... gift hai tere lie") 
    else:
        print(a,"is not an armtrong number")
        print("le chal gaya tera code mauj kar jaake ice cream khale ... gift hai tere lie") 
    
else:
    print("Inavlid Input hai boss... Integer value daalo ")
