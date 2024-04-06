#write a Program that receive input from the user to calculate the Area of Triangle,Square,rectangle-
choice=input("kiska area nikalna hai 1.rectangle\n 2.triangle\n 3.sqaure \n =")
if choice!="" and choice.isdigit()==True:
    tempc=int(choice)
    if tempc==1:
        length=input("ENTER THE LENGTH OF THE RECTANGLE=")
        bredth=input("ENTER THE BREDTH OF THE RECTANGLE=")
        if length!="" and length.isdigit()==True:
            if bredth!="" and bredth.isdigit()==True:
                lt=int(length)
                bt=int(bredth)
                areaofrectangle=(int(lt*bt))
                print("The Area Of Rectangle is = ",areaofrectangle)
                print("LE MAUJ KAR AB AREA KA FORMULA BHULEGA NAHI !! :)")
        else:
            print("Inavlid Input")
    elif tempc==2:
        height=input("ENTER THE HEIGHT OF THE TRIANGLE=")
        base=input("ENTER THE BASE OF THE TRIANGLE=")
        if height!="" and height.isdigit()==True:
            if base!="" and base.isdigit()==True :
                h=int(height)
                b=int(base)
                areaoftriangle=(int(1/2*h*b))
                print("The Area Of Triangle is = ",areaoftriangle)
                print("LE MAUJ KAR AB AREA KA FORMULA BHULEGA NAHI !! :)")
        else:
            print("Inavlid Input")
    else:
        side=input("ENTER THE SIDE LENGTH OF THE SQUARE=")
        if side!="" and side.isdigit()==True:
            s=int(side)
            areaofsqaure=(int(s*s))
            print("The Area Of Square is = ",areaofsqaure)
            print("LE MAUJ KAR AB AREA KA FORMULA BHULEGA NAHI !! :)")
        else:
            print("Inavlid Input")   
else:
    print("Inavlid Input")



 