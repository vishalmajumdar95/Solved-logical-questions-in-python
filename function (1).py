# def name():
#     print("Vishal")
# name()
# name()
# name()
# name()
# name()

# i=0
# while i<=100:
#     name()
#     print(i)
#     i+=1

# def my_max(a):
#     print(max(a))

# n=[3, 5, 7, 34, 2, 89, 2, 5]
# my_max(n)

# def my_max(m):


# def my_sum(a):
#     print(sum(a))

# v=[1, 2, 3, 4, 5]
# my_sum(v)


# def my_sort(a):
#     print(sorted(a))

# r=[6, 8, 4, 3, 9, 56, 0, 34, 7, 15] 
# my_sort(r)


# def reverse(a):
#     print(list(reversed(r)))

# r=["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# reverse(r)

# def my_min(m):
#     print(min(m))

# l = [8, 6, 4, 8, 4, 50, 2, 7] 
# my_min(l)

# Debug the code

# def sum():
#     print(12+13)
# sum()

# def welcome():
#     print("Welcome to function")
# welcome() 

# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number") 

# isEven()

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))

# a=[1,2,3,4,5,6]
# print(len(a))

# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif") 

# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)

# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev") 


# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")

# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh") 

# def greet(names):
#     for name in names:
#         print("Welcome", name)

# greet("Vishal")

# def info(name, age ="16" ):
#    print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18") 

# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","vishal") 

# def function_print_lines(name,work="Nil"):
#     print("Mera naam",name,"hai.")
#     print("Main NavGurukul ka",work,"hun.")

# function_print_lines("vishal","co-founder")
# function_print_lines("shubhadip","team member")

# def student(*st):
#     for name in st:
#         print("navgurukul",name)

# student("vishal","shub","tushar","ranjan")

# def isGreaterThen20(a,b=20):
#     if a>b:
#         print (a,"greater than")
#     else:
#         print(b,"greater than")

# isGreaterThen20(21)


# def add_num(num1,num2):
#     print(num1+num2)
# # add_num(25,95)

# def add_number(num1,num2):
#     for i,j in zip(num1,num2):
#         s = add_num(i,j)
#     return s
       
# add_number([50, 60, 10],[10, 20, 13])
        
# def check_numbers(num1,num2):
#     if num1%2==0 and num2%2==0:
#         return(num1,num2,"both are even")
#     # elif num1%2!=0:
#     #     print(num1,"odd")
#     else:
#         # print(num2,"odd")
#         return (num1,num2,"both are not even")

# # check_numbers(2,22)

# def check_numbers_list(a,b):
#     for i,j in zip(a,b):
#         s = check_numbers(i,j)
#         print(s)

# a=[2, 6, 18, 10, 3, 75] 
# b=[6, 19, 24, 12, 3, 87]
# check_numbers_list(a,b)
# check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])



######################################################################################################

# def binary(decimal) :
#     o = ""
#     while decimal != 0 :
#         o  =  str(decimal % 2) + o
#         decimal    //=  2
#     return o
# print (binary(10))

# def run(a):
#     j=a
#     k=a
#     p=1
#     for i in range(a+1):
#         print(" " * k," *" *  i)
#         k -=1
#     while j > 1:
#         j -= 1
#         print(" " * p," *" * j)
#         p +=1
# run(3)


# first Question 

# def my_max(a,b,c):
#     if a>b and a>c:
#         print(a,"max")
#     elif b>a and b>c:
#         print(b,"max")
#     elif a==b:
#         print(a,"max")
#     else:
#         print(c,"max")

# n1=int(input("check your number:>"))
# n2=int(input("check your number:>"))
# n3=int(input("check your number:>"))

# my_max(n1,n2,n3)

# second Question

# def sum_list(n):
#     s=0
#     for i in n:
#         s=s+i
#     print(s)

# v=[1,2,3,4,5,6,7,8,9]
# sum_list(v)

# Third Question

# def sum_list(n):
#     s=1
#     for i in n:
#         s=i*s
#     print(s)

# v=[1,2,3,4,5,6,7,8,9]
# sum_list(v)

# four Question

# def reverse_string(a):
#     v=""
#     for j in a:
#         v=j+v
#     print(v)

# v="vishal"
# reverse_string(v)
# 
# Fifth Question


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input())
# print(factorial(n))

#################################################################################################################

# 15th Question


# 16th Question

# def printValues(n):
# 	l = []
# 	for i in range(1,n+1):
# 		l.append(i**2)
# 	print(l)
		
# a=10
# printValues(a)

# 17th Question



# 19th Question

# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# def greater_2(a,b,c):
#     if greater(a,b)>c:
#         return greater(a,b)
#     else:
#         return c
        
        
        
# v=int(input())
# v=int(input())
#  =int(input())
# print(greater(12,9))
# print(greater_2(12,4,9))


