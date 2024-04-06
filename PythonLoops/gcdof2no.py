#GRETEST INTEGER DIVISOR OF TWO NUMBERS-
sankhya1=input("PEHLI SANKHYA KO LIKHE=")
sankhya2=input("DUSRI SANKHYA KO LIKHE=")
if sankhya1!="" and sankhya1.isdigit()==True:
    if sankhya2!="" and sankhya2.isdigit()==True:
        t1=int(sankhya1)
        t2=int(sankhya2)
        rem=1
        minval=min(t1,t2)
        maxval=max(t1,t2)
        while rem>0 and minval>0:
            rem=int(maxval%minval)
            div=int(maxval/minval)
            maxval=rem
            minval=div
        print(minval,"is the GCD OF",sankhya1,"and",sankhya2)
        print("le chal gaya tera code mauj kar jaake ice cream khale ... gift hai tere lie") 
else:
    print("Invalid input hai boss !! integer value dalo")