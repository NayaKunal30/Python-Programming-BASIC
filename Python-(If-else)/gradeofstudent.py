#WAP THAT GIVES GRADES OF STUDENT WHEN THEIR MARKS IS GIVEN AS INPUT-
print("GRADE-A : 90 SE ZYDA HAI\nGRADE- B : 80 SE ZYDA HAI\nGRADE-C:70 SE ZYDA HAI\nGRADE-D: 60 SE ZYDA HAI\nGRADE-E: FAIL HAI BACHA CHAMDA KA BELT READY RAKHO PAPA")
marks1=input("enter the marks obtained / bacche ke marks bata=")
if marks1!="" and marks1.isdigit()==True:
    marks=int(marks1)
    if (marks>90):
        print("GRADE-A")
    elif(marks>80 and marks<90):
        print("GRADE-B")
    elif(marks>70 and marks<80):
        print("GRADE-C")
    elif(marks>60 and marks<70):
        print("GRADE-D")
    else:
        print("\nGRADE E - FAIL HAI BACHA BAUJI BELT SE MAARO ISKO")
    print("le chal gaya tera code mauj kar jaake ice cream khale ... gift hai tere lie")
else:
    print("Invalid input..Integer value daalo :)")
        
    