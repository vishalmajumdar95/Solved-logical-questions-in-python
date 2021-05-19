
a = int(input("Enter first no: "))
operator = input("choose what you want to do => +,-,*,/,**,//,%,:- ")
b = int(input("Enter second no: "))
if operator == "+":
    print(a,"+",b"=",a+b,"\n")
    print(("Thanks for using calculator"))
elif operator == "-":
    print(a,"_",b"=",a-b,"\n")
    print(("Thanks for using calculator"))
elif operator == "*":
    print(a,"*",b"=",a*b,"\n")
    print(("Thanks for using calculator"))
elif operator == "/":
    print(a,"/",b"=",a/b,"\n")
    print(("Thanks for using calculator"))
elif operator == "//":
    print(a,"//",b"=",a//b,"\n")
    print(("Thanks for using calculator"))
elif operator == "**":
    print(a,"**",b"=",a**b,"\n")
    print(("Thanks for using calculator"))
elif operator == "%":
    print(a,"%",b"=",a%b,"\n")
    print(("Thanks for using calculator"))
else:
    print("Wrong input")
    print(("Thanks for using calculator"))

# a = int(input("Enter a year: "))  
# if (a % 4) == 0:  
#    if (a % 100) == 0:  
#        if (a % 400) == 0:  
#            print("This is a leap year")  
#        else:  
#            print("This is not a leap year")  
#    else:  
#        print("This is a leap year")  
# else:  
#    print("This is not a leap year")

# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# c = int(input("Enter a number:"))

# # if a>b==0:
# # if b>c==0:
# # if c>a==0:
# # print("you find the maximum number")

# if (a >= b) and (a >= c):
#    largest = a
# elif (b >= a) and (b >= c):
#    largest = b
# else:
#    largest = c

# print("The largest number is", largest)



# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# c = int(input("Eznter a number:"))
# if (a > b)
# if (a > c)
# print(a)
# elif(b<c or b==a):
# print(c)
# else:
# print(b)



#list in Python

# name =["siddik","ranjan", "vishal", "suraj"]
# print(name[0])

# num = [12,13,14,15]
# print(num[0])
# print(num[0:1])

# value = ["siddik","ranjan"]
# num.append(12)
# print(value + num)

# value = ["siddik","ranjan"]
# value.insert(2, 11)
# print(value + num)

# value = ["siddik","ranjan"]
# num.insert(2, 11)
# print(value + num)

# value = ["siddik", 11,"ranjan"]
# value.remove(11)
# print(value)

# value = ["siddik","ranjan"]
# value.pop(1)
# print(value)

# if you not put pop has no value give the last value

# value = [12,13,14]
# value.extend([1,2,3])
# print(value)

# name="siddik"
# print(name[-3])

# tup=(1,2,3,4)
# print(tup[1])

# set={1,2,3,4}
# # print(set)

# list1 = ["siddik","ranjan","vishal","suraj"]
# for item in list1:
#     print(item)

# num=5
# print(num)
# print('thamans')

# a = input("Enter a number: ")
# a = int(a)
# # print(type(a))

# print("Welcome To The Guees Game")
# a = input("Enter a Guees number:")
# b = 12
# a = int(a)
# b = int(b)
# if a == b:
#     print("You Win, You Guees the right number")
# else:
#     print("wrong")
#     x = int(input("Enter A Second Guees number:"))
#     if b==x:
#         print("you win")
#     else:
#         print("wrong")
#         y = int(input("Enter A Third Guees number:"))
#         if y == b:
#             print("You Win")
#         else:
#             print("Better Luck Next time.")


# # 1st Question Done
# i = 1
# while i < 101:
# print (i)
# i = i + 1
# print("Done")

# End

# 2nd Question

# i = 1  
# while i < 51:
#     if i%2==0:
#         print("Even Number ",i)
#     else:
#         print("Odd Number ",i)
#     i = i+1
# print("Done")

# End

# 3rd Question
# i = 1  
# while i < 51:
#     if i%5==0:
#         print(i)
#     i = i+1
# print("Done")

#Done


#4th Question


# i = 1  
# while i < 51:
#     if  i%2==0 and i%5==0:
#         print("navgurukul", i)
#     elif  i%2==0:
#         print("Nav", i)
#     elif i%5==0:
#         print("Gurukul",i)
#     i = i+1
# print("Done")

#Done


# for i in range(1,51):
#     if i%2==0:
#         print("Even Number ",i)
#     else:
#         if i%1==0:
#           print("odd number", i)

# a =int(input("Enter a number: "))
# operator = input("+, -, /, * : ")
# b = int(input("Enter a second number: "))
# if operator == "+":
#     print(a+b)
# elif operator == "-":
#     print(a-b)
# elif operator == "*":
#     print(a*b)
# elif operator == "/":
#     print(a/b)

# string
# input
# list
# loop
# operator

# b=int(input('Enter The Number :'))
# sum=0
# for i in range(b):
#     a =int(input("Enter a Number: "))
#     sum+=a
# print(sum/b)




# for i in range(100,0,-1):
# print(i)

# a = input("Enter: ")
# if a.isdigit():
# print("int")
# elif a.isalpha():
# print("String")
# else:
# print("float")


# a.isalnum()x = txt.isnumeric()
# x = txt.isspace()


#x = txt.capitalize()
#x = txt.isalnum()

# password = input("Enter The Number:")

# Quesion 1

# l = int(input("Enter a length:"))
# b = int(input("Enter a breath:"))
# if l==b:
# print("This is a square")
# else:
# print("This is not a square")

# Question 2

# a = int(input("Enter a Number:"))
# b = int(input("Enter a Second Number:"))
# if a > b :
# print(a,"is greater than",b)
# else:
# print(b,"is greater than",a)

#Questiion 3

# a = int(input("Enter a quantity:"))
# if a > 999 and a/a*100:
# print((a-a/10),"You want to pay")
# else:
# print(" Sorry, There is no discout for you")

#Question 4

# salary = int(input("Enter a salary:"))
# service= int(input("Enter a service year:"))
# if service > 4:
# print(salary+(salary/100*5))
# else:
# print("No Bonus For You")

#Question 5

# a = 6
# b = 3
# if a==b:
# print("a")
# # if a > b:
# # print("so mach")
# else:
#     print("vishal")
# elif b==a:
# print("b")


# i = 1
# while i <=100:
# if i%3==0 and i%5==0:
# print(i,"vishal")
# elif i%3==0:
# print(i,"siddik")
# elif i%5==0:
# print(i,"ranjan")
# i+=1


# def x(y):
# if type(y)==list:
# for i in y:
# return x(i)
# else:
# return x+x(x)

