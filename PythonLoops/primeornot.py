#WAP THAT CHECK WHETHER A NUMBER IS PRIME OR NOT-
sankhya=input("sankhya ko likhiyeee =")
if sankhya!="" and sankhya.isdigit()==True:
    count=0
    num=int(sankhya)
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(num,"EK PRIME Number HAI BHAI") 
    else:
        print(num,"PRIME Number NAHI HAI BHAI:(")
    print("le chal gaya tera code mauj kar jaake ice cream khale ... gift hai tere lie")  
else:
    print("Invalid input hai boss ... integer value daalo..")      
        