#LEAP YEAR OR NOT - LEAP YEAR JO MULTIPLE OF 4 HOTA HAI 
saal=input("enter the year/saal to check : ")
if saal!="" and saal.isdigit()==True:
    year=int(saal)
    if year%4==0: #if remainder is 0 then multiple of 4 
        print(year,"is a leap year/saal")
    else:
        print(year,"is not a leap year/saal")
else:
    print("Inavlid input hai boss... integer value daalo")