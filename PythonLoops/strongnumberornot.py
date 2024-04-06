#WAP TO CHECK WHETHER A GIVEN NUMBER IS A STRONG NUMBER OR NOT :
print("STRONG NUMBER - EX: 145=1!+4!+5! a special number whose sum of the factorial of digits is equal to the original number.\n")
sankhya=input("ENTER YOUR INPUT TO CHECK WHEATHER IT IS A STRONG NUMBER ->>")
if sankhya!="" and sankhya.isdigit()==True:
    a=int(sankhya)
    temp=int(sankhya)
    flag = 0
    while(temp>0):
        rem = temp % 10
        fact = 1
        while(rem>0):
            fact = rem * fact
            rem -= 1
        flag = flag + fact
        temp = temp // 10
    if(a==flag):
        print(a,"IS A STRONG NUMBER")
    else:
        print(a,"IS NOT A STRONG NUMBER")
else:
    print("invalid input... integer value daalo")
        
        
        
        
        
        