
########------Perfect numbers range-----#############
# n=int(input("Enter the :"))
# for j in range(1,n+1):
#     s=0    
#     i=1
#     for i in range(1,j):
#         if j%i==0:
#             s=s+i
#     if s==j:
#         print("Yes it is Perfect Number",s)
#     else:
#         print("No it is perfect Number",j)


########------Perfect numbers -----#############

# n=int(input("Cheak you number:- "))
# s=0
# for i in range(1,n):
#     if n%i==0:
#         s=s+i
# if s==n:
#     print("it's Perfect")
# else:
#     print("it's not Perfect")

########------Sipce numbers -----#############

# num=int(input("Cheak your number: "))
# b=0
# c=1
# while num>0:
#     d=num%10
#     b=b+d
#     c=c*d
#     num=num//10
# if b==c:
#     print("Yes! it's Sipce number")
# else:
#     print("No! it's Spice number")

########------Prime number -----#############
### first approach
# n=int(input("check your prime number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("No! its not a prime")
#         break
# else:
#     print("Yes! its Prime")

### second approach

# num=int(input("check your number:> "))
# c=0
# x=2
# while x<=num/2:
#     if num%x==0:
#         c=1
#         break
#     x+=1
# if c==0:
#     print("No! its not a prime")
# else:
#     print("Yes! its Prime")

##############################################

#############------Multiply the two numbers with out using multiply operator-----------###########

# num1=int(input("Enter your first number: "))
# num2=int(input("Enter your second number: "))
# n=0
# n1=0
# while n<num2:
#     n1=n1+num1
#     n+=1
# print(num1,"*",num2,"=",n1)

#############------Triangle pattern -----------###########
####--without used inbuild function:-| end="" |
# def tri_patten(a):
#     i=1
#     c=0
#     s=" "
#     while i!=a+1:
#         c+=i
#         t=str(c)
#         s=s+" "+t
#         i+=1
#     print(s)
# x=int(input("enter your number: "))
# tri_patten(x)

#####--> print pattern with used ( end="" )
# def tri_patten(a):
#     for i in range(1,a+1):
#         n=(i*(i+1))//2
#         print(" "+str(n),end="")
#     print()
# h=int(input("enter your number: "))
# tri_patten(h)

#####--> print pattern with used list
# def tri_patten(a):
#     i=1
#     c=0
#     s=[]
#     while i!=a+1:
#         c+=i
#         s.append(c)
#         i+=1
#     print(s)
# x=int(input("enter your number: "))
# tri_patten(x)

#####-->Armstrong number<---##########
# num = int(input("Enter your number: "))
# n = num
# s=0
# while (num>0):
#     n = n + (num%10) * (num%10) * (num%10)
#     num=num//10
# if (n==s):
#     print("Yes! its Armstrong number=>",n)
# else:
#     print("No! its not Armstrong number=>",n)

###########-----> Fabancci seric <-----###########
# n=int(input("print your fabancci seric:"))
# a = 0
# b = 1
# for i in range(n):
#     print(a,end=",")
#     c=a+b
#     a=b
#     b=c
# print()


#####-->Happy number<---##########
# num=int(input("Enter your number: "))
# s=0
# while s!=1 and s!=4:
#     s=0
#     while num>0:
#         v=num%10
#         s+=(v*v)
#         num=num//10
#     num=s
# if s==1:
#     print("Yes! its Happy number=>",num)
# else:
#     print("No! its not Happy number=>",num)
