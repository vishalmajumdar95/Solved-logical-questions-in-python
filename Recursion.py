##################-----Recursion Number pattern serces----################
# def pattern(number):
#     if number == 1:
#         return 1
#     else:
#         return pattern(number-1) + 3
# for i in range(1,11):
#     print(pattern(i),end = ",")

##############################################################
##################-----Recursion Number pattern serces----################

# def pattern(number):
#     if number == 1:
#         return 10
#     elif number % 2 == 0:
#         return pattern(number - 1) + 1
#     else:
#         return pattern(number - 1) * 10 
#     print()
#     print(pattern(number - 1) + 1)
# for i in range(1,11):
#     print(pattern(i),end = ",")

#####################################################
##################-----Recursion Number factorial----################

# def factorial(number):
#     if number==1:
#         return 1
#     return number * factorial(number - 1)
# for i in range(1,10):
#     print(factorial(i))

##################################################
##################-----Recursion sum the list iteams----################
# def sum_list(lis):
#     if len(lis)==1:
#         return lis[0]
#     return lis[0] + sum_list(lis[1:])
# print(sum_list([1,4,7,17,12,24,43,10])) 



#####################################################################################
##################-----Recursion Fabancci pattern----################

# def fabancci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fabancci(n-1) + fabancci(n-2)
# for i in range(1,10):
#     print(fabancci(i),end="")
##################################################

# def sumDigits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sumDigits(int(n / 10))
# print(sumDigits(345))
# print(sumDigits(45))


# def ifPalindrome(string):
#     if string == "":  
#         return True
#     elif len(string) == 1:
#         return True
#     elif string[0] == string[len(string)-1]: 
#         return ifPalindrome(string[1:][:-1])
#     else:
#         return False
# print(ifPalindrome("vishal"))

##################################----Star_Pattern----#################################
# def StarPattern(n, i): 
#     if (n < 1): 
#         return
#     if (i <= n): 
#         print("* ", end = "") 
#         StarPattern(n, i + 1) 
#     else:      
#         print("")  
#         StarPattern(n-1, 1) 
# n = 5
# StarPattern(n, 1) 
  
# def print_space(space): 
#     if (space == 0): 
#         return; 
#     print(" ", end = "");  
#     print_space(space - 1); 
# def print_asterisk(asterisk): 
#     if(asterisk == 0): 
#         return; 
#     print("* ", end = "");  
#     print_asterisk(asterisk - 1);  
# def pattern(n, num):  
#     if (n == 0): 
#         return; 
#     print_space(n - 1); 
#     print_asterisk(num - n + 1); 
#     print("")
#     pattern(n - 1, num); 
# n = 5; 
# pattern(n, n); 


# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return (fibonacci(n - 1) + (fibonacci(n - 2)))
# print(fibonacci(10))


# def DecimalToBinary(num):     
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2,end="")
# d = int(input())
# DecimalToBinary(d)
# print()

        
# def count(n):
#     if n>0:
#         count(n-1)
#         print(n)
# count(10) 

# def count(n):
#     if n<=10:
#         count(n+1)
#         print(n)
# count(1)


# fabonacci_cache={}
# def fabancci(n):
#     if n in fabonacci_cache:
#         return fabonacci_cache[n]
#     if n==1:
#         value=1
#     elif n==2:
#         value=1
#     else:
#         value=fabancci(n-1) + fabancci(n-2)
#     fabonacci_cache[n]=value
#     return value
# for i in range(1,100):
#     print(fabancci(i))


# from functools import lru_cache
# @lru_cache(maxsize=1000)
# def fabancci(n):
#     if type(n)!=int:
#         raise TypeError("n must be a postive int")
#     if n<1:
#         raise ValueError("n must be a postive int")
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fabancci(n-1) + fabancci(n-2)
# for n in range(1,5000):
#     print(fabancci(n+1) / fabancci(n))


# def x(h):
# 	if h in [1,0]:
# 		return 1
# 	else:
# 		return x(h-1)+x(h-2)
# print(x(int(input())))

# s,j=[],int(input())
# for i in range(1,(j//2)+1):
# 	s.extend([i,13*i,7+(i-1)])
# print(s[j])
# print(s)

# x,c=list(map(int,input().split())),0
# for i in x:
# 	x.pop(0)
# 	if i in x:
# 		c+=1
# print(c)
