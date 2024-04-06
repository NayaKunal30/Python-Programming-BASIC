firstnum1=input("enter the first number=")
secondnum2=input("enter the second number =")
operator=input("enter the operation you want to perform (+,-,*,/,%) =")
if firstnum1!="" and firstnum1.isdigit()==True:
    if secondnum2!="" and secondnum2.isdigit()==True:
        firstnum=int(firstnum1)
        secondnum=int(secondnum2)
        if operator == "+":
            print(firstnum+secondnum)
        elif operator == "-":
            print(firstnum-secondnum)
        elif operator == "*":
            print(firstnum*secondnum)
        elif operator == "/":
            print(firstnum/secondnum)
        elif operator == "%":
            print(firstnum%secondnum)
        else:
            print("INVALID OPERATION CHOOSE FROM ABOVE 5 OPERATIONS! :)")
else:
    print("invalid input hai boss.. integer value daalo")