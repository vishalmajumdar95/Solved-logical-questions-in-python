##################--R pattern with star---###############
# n=int(input("Enter you number:"))
# d=""    
# for r in range(0,n):    
#     for c in range(0,n):     
#         if (c == 1 or ((r == 0 or r == 3) and c > 1 and c < 5) or (c == 5 and r != 0 and r < 3) or (c == r - 1 and r > 2)):  
#             d=d+"*"    
#         else:      
#             d=d+" "    
#     d=d+"\n"    
# print(d)

# n=int(input("Enter you number:"))
# d=""    
# for r in range(0,n):    
#     for c in range(0,n):     
#         if (c == 1 or ((r == 0 or r == 3) and c > 1 and c < 5) or (c == 5 and r != 0 and r < 3) or (c == r - 1 and r > 2)):  
#             d=d+"*"    
#         else:      
#             d=d+" "    
#     d=d+"\n"    
# print(d)
##################--X pattern with star---###############
# n=int(input("enter your number: "))
# for i in range(n):
#     for j in range(n+1):
#         if j == i or j == n-i:
#             print('*',end = '')
#         print(' ',end = '')
#         if j > (n/2)+1 and i>(n/2)+1:
#             print(' ', end='')
#     print()

##################--Y pattern with star---###############
# n=int(input("Enter number: "))
# for i in range(n):
#     for j in range(n+1):
#         if j == i or j == n-i:
#             print('*',end = '')
#             if i > n/2:
#                 break
#         print(' ',end = '')
#         if j > (n/2)+1 and i>(n/2)+1:
#             print(' ', end='')
#     print()

##################--Triangle pattern with star---###############
# n=int(input("Enter your Number:"))
# b=bool(int(input("Enter your number( 1 or 0): ")))
# if b==True:
#     for i in range(n+1):
#         print("* "*i)
# else:
#     for i in range(n+1):
#         print("* "*n)
#         n-=1


#############----- Number Sanke pattern-------#############
# n=int(input("enter number: "))
# a=1
# for i in range(n+1):
#     b=n*n+1
#     for j in range (n-1,-n,-2):
#         if b==a:
#             break
#         print(a+j*(i%2),end=" ")
#         a+=1
#     print()

##################--Triangle pattern with star---###############
# n=int(input("Enter your number: "))
# for i  in range(1,n+1):
#     for j in range(n,0,-1):
#         if i>=j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# num=int(input("enter the number:>"))
# i=0
# while i<num:
#     v=i+1
#     while v>0:
#         print("*",end="")
#         v=v-1
#     i=i+1
    # print()


# n = int(input("Enter the number:> "))
# i = 1
# while i<=n:
#     j = 1
#     while j<=i:
#         print("*", end=" ")
#         j+=1
#     print()
#     i+=1
############-----> table <------#############

# num=int(input("How many table you want: "))
# for i in range(1,num+1):
#     for x in range(1,10+1):
#             print(i,"*",x,"=",i*x)
#     print()


# a=int(input("enter the number:>"))
# for i in range(a):
#   for v in range(i+1):
#       print("*",end="")

#   print()

# for i in range(4):
#     for v in range(4-i):
#         print("#",end="")
#     print()



##################--Number Triangle pattern with digits---###############

# a=int(input("enter the number:>"))
# for i in range(1,a+1):
#     if i%2==0:
#         for j in range(1,i+2):
#             if j==1:
#                 pass
#             else:
#                 print (j,end=" ")
#     else:
#         for j in range(1,i+1):
#             print (j,end=" ")
#     print ()

# ##printing pattern using for loop
# for i in range(4):
#     for j in range(4):
#         print ("&",end=" ")
#     print()



# printing pyramid using for loop
# a=int(input("Enter the number of rows: "))
# for i in range(a):
#     for j in range(a-i-1):
#         print (end=" ")
#     for j in range(i+1):
#         print ("@",end=' ')
#     print ()



# printing pattern using while loop
# a=int(input("Enter the number of rows: "))
# rows=0
# while rows<a:
#     star=rows+1
#     while star>0:
#         print ("*",end="")
#         star-=1
#     rows+=1
#     print ()



# #########------printing python 
# a=input("enter the input: ")
# length=len(a)
# for i in range(length):
#     for j in range(i+1):
#         print (a[j],end=" ")    
#     print ()


# printing pattern like pyramid
# a=input("enter the input: ")
# length=len(a)
# for i in range(length):
#     for j in range(len(a)-i-1):
#         print (end="  ")
#     for j in range(i+1):
#         print (a[j],end='   ')
#     print ()


#####----printing python 
# n=int(input("Enter the number: "))
# for i in range(n):
#     count=0
#     for j in range(n-i-1):
#         print (end=' ')
#     for j in range(i+1):
#         print ("*",end="")
#         if count<i:
#             print("A",end="")
#         count+=1
#     print ()

######################################################################
############--------Heart Patten with star------####################
# for i in range(6):
#     for j in range(7):
#         if i==0 and j%3!=0:
#             print("*",end="")
#         elif i==1 and j%3==0:
#            print("*",end="")
#         elif i-j==2:
#             print("*",end="")
#         elif i+j==8:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()