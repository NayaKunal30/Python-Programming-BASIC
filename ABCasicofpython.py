#First fucntion pritn fucntion.
print("hello world")
#string,float,integer,booleon- primitive datatypes in python
#TYPES OF VARIABLE IN PYTHON :
#string manipulation : 
name="work hard"
print("name")
print(name)
#int manupulation:
age="30"
print("age")
print(age)
#float:
age2="30.50"
print(age2)
#booleon:
is_adult="True"
is_adult="False"

#Q1.TAKE INPUT OF NAME AGE AND COMMENT ON THEM .
name1=input("enter your name:")
age3=int(input("enter your age"))
if(age3>40):
    print(name1,"is genius",)
else:
    print(name1,"is intelligent")
#CONCATNATION OF STRINGS IN PYTHON: 
print("hello"+name1)

#TYPE CONVERSION:
oldage=int(input("enter your old age"))
newage= int(oldage)+5 #typeconversion of string to integer
print(newage)

#Q2.PROGRAM TO CALCULATE SUM OF 2 NUMBERS:
firstnum=int(input("enter the first number")) #int used for type conversion.
secondnum=int(input("enter the second number"))
sum=firstnum+secondnum
print("THE SUM OF THE TWO NUMBERS IS =",sum)

#string manipulation : 
string=input("enter a string/name:")
print(string.upper()) #convert the characters of the string in upper case
print(string.lower()) #convert the characters of the string in lower case
print(string.find('k')) #To find particular character in a string - it returns the index of that particular character
#space is also an index in python
print("w" in string) #to check whether the character exist in string or not
print("hello" in string) #to check whether the string exist in string or not
print(string.find("work")) #To find particular string in a string 
# to replace string : print(string.replace("",""))
print(string)
#OPERATORS IN PYTHON :
x=int(input("enter the first number"))
y=int(input("enter the second number"))
sum1=print(x+y)
sub=print(x-y)
mul=print(x*y)
div=print(x/y)
rem=print(x%y)
power=print(x**y)

#shortcuts:
i=int(input("enter a number:"))
i=i+5
i+=5
i-=5
i*=5
i/=5
#operator precendence:
result=2+3*5
print(result)
#comparision operator:
print(3>2)
print(5<2)
print(3==2)
print(3!=2)
#Logical Operators in Python OR,AND,NOR:
print(2>3 or 5>1)
print(2>1 and 4>3)
print(2>1 and 1>3)
print(not 3>2)

#if-else statement in python :
#if condition :
#indentaton of 4 spaces after colon 
age4=int(input("enter your age"))
if age4>=18:
    print("you are eligible for voting")
elif age4<18 and age4>3:
    print("you are in school bachaaa")
else:
    print("you cant vote : tmkc :) ")
print("hello guyz chai pillo this is if else ke bahar ka statement")

#RANGE IN PYTHON - Range(5) - iska mtlb 0,1,2,3,4 last wala not inlcuded...
#range is a keyword

#Loops in Python :
#WHILE LOOP IN PYTHON -
i=1
while i<=1000:
    i=i+1 #agar yeh condition nahi hai then infinite loop!! agar condition hai toh terminate hogi 
    print(i)

#pattern using while loop 1:
i=1
while i<=1000:
    print(i*"#")
    i=i+1
#pattern using while loop 2:
i=5
while i>=0:
    print(i*"#")
    i=i-1
#for loop in python :
for i in range(5):
    print(i+1)

#LIST - MUTABLE    
#list is a complex datatypes - collection of primitive datatypes-
marks=[50,60,70,80,90]  #yeh hai ak list jisme kuch items datatypes present hai forexample marks of bache
print(marks[2]) #marks of marks jo 2nd index me hai 
print(marks[-1])
print(marks[1:4])
#in python positive and negetive index dono ho sakte
#list manupulations-
#marks.append(95.99) - galat hai ak sath do values add nahi kar sakte hamesha ak value add hogi ... and last se add hogi
marks.append(95)
#agar beech me kahin value add karni ho last me nahi then insert fucntion is used -
marks.insert(2,99)
print(99 in marks) #in keyword checks the values in list and retunn booleo value 
print(marks)
#length of list-
print(len(marks)) #len keyword is used

#using while loop to print list ke elements:
i=0
while i<len(marks):
    print(marks[i])
    i=i+1
#to delete entire list:
marks.clear()
print(marks)

#break and continue statements in python-
students=["rohit","rahul","raghav","ryan"]
for student in students:
    if student == "raghav":  #raghav tak saare students ka naame 
        break; #loop khatam karne ke lie used
    print(student)
#continue:
students=["rohit","rahul","raghav","ryan"]
for student in students:
    if student == "raghav":#for ke andar if statement
        continue; #humare loop ko ak aur baar run kardijiye abhi wala loop ko mat cheriye
    print(student)
    
#TUPLE- IMMUTABLE 
#modify,delete,append operation nahi hoga 
marks1=(90,95,97,98,97)
print(marks1.count(97)) #to count the number of time a value is there in a tuple
print(marks1.index(97))

#SETS: UNORDERED
marks2={90,95,97,98,97}
#set ke andar unique values store hoti hai ...
#set ke andar index does not exists
#loop hi chala sakte hai 
for i in marks2:
    print(i)
print(marks2)

#DICTIONARY - KEY VALUE PAIR STORED HOTA HAI -
marks3={"english":97,"maths":98,"physics":90,"chemistry":99}
print(marks3["chemistry"])
#to change existing value -
marks3["physics"]=95
print(marks3)

#modules in python-
#exmple math module :
import math
print(dir(math))

#for using particular function from math module -
from math import sqrt
print(sqrt(81))
#to use saare functions without mentioning ak particular fucntion
from math import * # (* mtlb all)
print(pow(3,2))

#USER DEFINED FUCNTIONS :
#sytax- def funtionname (parameters):
#//do something
firstnum= int(input("enter the first number")) #int used for type conversion.
secondnum=int(input("enter the second number"))
def sum(firstnum,secondnum):
    print(firstnum+secondnum)
sum(firstnum,secondnum)

print("abc", end="  ") 
print("end=" "this is used to give space to different attribute in output side")
print("abc\t","goodatm")
print("#\t-this is used to give 4 space indent to particular character")
print("abc\n","hello")
print("for new line \n is used")

print("end this world kalyug khatam")


    
    


 















