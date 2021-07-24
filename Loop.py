###############################
nums=int(input())
i=0
sums=0
count=0
while (count<=nums):
    if (i%2==0):
        sums=sums+i
        count=count+1
    i=i+1
print("v",sums,count,i,nums)

 #################################################################################

i=int(input())
sums=0
while(i>0):
    sums=sums+i%10
    i=i//10
print(sums)

###########################################################################

n=int(input())
t=n
r=0
while (n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(t==r):
    print("P hai")
else:
    print("P nhi hai")    

##################################################################

# ######`frist_one`
i=int(input())
r=0
while (i>0):
    r=r+(i%10)*(i%10)
    i=i//10
print(r)

#########################################################################

# ###second_one
i=int(input())
r=0
while (i>0):
    r=r+(i%10)*(i%10)*(i%10)
    i=i//10
print(r)

########################################################################

# #####third_one
i=int(input())
s=0
while (i>0):
    i=i//10
    s+=1
print("no. of digits",s)

########################################################################

i=(input())
v=""
c=0
while i in v:
    i=i//str(10)
    c+=1
print("no. of digits",i,c)

###############################################################

##### forth_one

i=int(input())
r=i
s=0
while (i>0):
    r=r+(i%10)*(i%10)*(i%10)
    i=i//10
if (r==s):
    print("Armstrong hai")
else:
    print("Armstrong nhi hai")

#########################################################

i=int(input())
n=i
s=0
while (i>0):
    i=i//10
    s+=1
print("no. of digits",s)
s=0
n=i
while(i>0):
    d=i%10
    x=1
    p=1
    while (x<=s):
        p=p*d
        x+=1
    s=s+p
    i=i//10
if (s==i):
    print("Armstrong hai")
else:
    print("Armstrong nhi hai")

###############################################################

i=int(input())
s=0
while (i>0):
    i=i//10
    s+=1
print("no. of digits",s)
# i=int(input())
n=i
s=0
while (i>0):
    n=n+(i%10)*(i%10)*(i%10)
    i=i//10
if (n==s):
    print("Armstrong hai")
else:
    print("Armstrong nhi hai")

#########################################################

i=int(input())
pro=1
while (i>0):
    pro=pro*(i%10)
    i=i//10
print("no. of digits",pro)

############################################################

n=int(input())
rec=0
while (n>0):
    rec=(rec*0)+i%10
    n=n//10
print(rec)

###############################################################

a=["Vishal","suraj","23456"]
b=[]
for i in a:
    v=""
    for j in i:
        v=j+v
    b.append(v)
print(b)

#################################################################

a=list(input("enter your iteams:> "))
a=["vishal"]
b=[]
for n in a:
    v=""
    for j in n:
        v=j+v
    b.append(v)
print("this is your recverse list iteams:",b)

###################################################################

list1=list(input())
lit2=list(input())
for i in lit2:
    for j in list1:
        if (i==j):
            list1.remove(i)
print(list1)

#####################################################

i=0
while(i<=100):
    if i%7==0:
        print(i)
    i+=1


i=0
s=0
while(i<=100):
    s=s+i
    i+=1
print(s)


i=int(input("how many times"))
s=0
v=1
while(v<=i):
    n=int(input("enter yo no."))
    s=n+s
    v+=1
print(s)


i=1
while(i<=100):
    if(i%2==0):
        print(-i)
    else:
        print(i)
    i+=1



i = 556
while i < 644:
  z = i - 556
  if z % 7 == 0:
    print(z)
  i = i + 1 

x=int(input())
c=0
u=0
while x!=0:
    y=input()
    if y%2==0:
        c+=1
    else:
        u+=1
    x-=1
if c>u:
	print("ready for watel")
else:
	print("not")

# ############################################
x=int(input())
y=int(input())
m=[]
c=0
n=0
b=0
while c!=x:
	m.append([])
	while n!=y:
		v=input()
		if v >="a" and v<="z" or v>="A" and v<="Z":
			m[b].append(v)
		elif v in "1234567890":
			v=int(v)
			m[b].append(v)
		else:
			v=float(v)
			m[b].append(v)
		n+=1
	n=0
	b+=1
	c+=1
print(m)

# x=[1,2,3,[1,2,3],[1,1,"6"]]
# y=[]
# for i in x:
# 	if i in "1234567890":
# 		v=int(i)
# 		y.append(v)
# 	elif type(i)==[]:
#         print()

#########################################
V=1
y=2
c=4
while c!=0:
	if c%2==0:
		print(V,y,V,y)
	else:
		print(y,V,y,V)
	c-=1

################

x=int(input())
y=int(input())
c=0
while x!=0:
	x-=y
	c+=1
print(c)

x=int(input())
y=int(input())
m=[]
c=0
n=0
b=0
while c!=x:
	m.append([])
	while n!=y:
		v=input()
		if v in "1234567890":
			v=int(v)
			m[b].append(v)
		n+=1
	n=0
	b+=1
	c+=1
print(m)

# ########=======================================================================================================
# ####frist Q1:>

n=int(input())
for i  in range(1,n+1):
    for j in range(n,0,-1):
        if i>=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for v in range(0,i):
        print("*",end="")
    print()

#### Second Q2:>

n=input()
m=""
for i in n:
    m=i+m
if n==m:
    print("Yes! this is Palindrome")
else:
    print("No! this is not Palindrome")

##### Theird Q3:>
n=int(input())
for i in range(1,n+1):
    for x in range(1,10+1):
        print(i,"*",x,"=",i*x)
    print()

# ###forth Q4:>

n=int(input())
f=1
i=1
while i<=n:
    f=f*i
    i+=1
print(f)

n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)

#### fifth Q5:>
n=int(input("print your fan seric:"))
a = 0
b = 1
i = 0
while i < n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1

n=int(input("print your fabancci seric:"))
a = 0
b = 1
for i in range(n):
    print(a,end=",")
    c=a+b
    a=b
    b=c
print()

n=int(input())
c=0
i=1
while i<=n:
    m=int(input())
    c=m+c
    i+=1
print(c)


list1=list(input())
lit2=list(input())
for i in lit2:
    for j in list1:
        if (i==j):
            list1.remove(i)
print(list1)




def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")
   
print(mytxt)

########### Nested List
x=int(input("HOW MANY LIST YOU WANT:>"))
m=[]
b=0
for i in x:
    y=int(input("HOW MANY ITEAMS YOU WANT PUT:>"))
    m.append([])
    for i in y:
        v=input()
        if v in ("1234567890"):
            v=int(v)
            m[b].append(v)
        elif (v >="a" and v<="z") or (v>="A" and v<="Z"):
            m[b].append(v)
        else:
            v=float(v)
            m[b].append(v)
	b+=1
	c+=1
print(m)

li=[i for i in range(100) if i%2==0]
print(li)


n=int(input())
# s=0
for s in range(1,n):
# while s!=1 and s!=4:
    # s=0
    for s in range(n):
    # while n>0:
        t=n%10
        s+=(t*t)
        n=n//10
    n=s
if s==1:
    print("happy")
else:
    print("not happy")


n=int(input())
i=2
while n>=i:     
    if n%i==0:
        print("No P")
        break
    i+=1
else:
    print("YES P")

n=int(input("check your number:> "))
i=2
while i<n:
    if n%i==0:
        print("Prime nhi hai ")
        break
    i+=1
else:
    print("Prime hai ")

n=int(input("check your number:> "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime hai")
else:
    print("Prime nhi hai")

n=int(input("check your number:> "))
c=0
x=2
while x<=n/2:
    if n%x==0:
        c=1
        break
    x+=1
if c==0:
    print("Prime hai")
else:
    print("Prime nhi hai")
###################################----If-else ATM machince project------#############################

print("\n\t*********--Welcome to the My_Bank--************\n\n")
pin=int(input("\t--Enter your 4 digit pin----\n\t===> "))
if pin==2021:
    print("\t==> 1.withdraw")
    print("\t==> 2.balance enquiry")
    print("\t==> 3.deposit")
    print("\t==> 4.exit")
    a=int(input("\n\t===>Enter your requird\n\t==> "))        
    if a==1:
        print("\t===>Enter your amount ")
        amount=int(input("\t==>"))
        print("\n\t<----transaction successful---->")
        print(f"\n\t<---your remaining amount is--->))>> $",1000-amount,"<<((")
    elif a==2:
        print(f"\n\t>>>>> Your balance {1000} <<<<<")
    elif a==3:
        print("\n\t===> Enter your deposit amount")
        amount=int(input("\t==>"))
        print("\n\t<---your currently amount is--->))>> $",1000+amount,"<<((")
    elif a==4:
        print("\n\t>>>>> thank you <<<<<")
    else:
        print("\n\t>>>>> cash is not in the ATM <<<<<")
else:
    print("\n\t>>>>> wrong pin <<<<<")

##############################################################################
#########----if-else stone,paper, scisser game---##########
player1=input("Player1! choose any one ->(stone, paper, scisser): ")
player2=input("Player@! choose any one ->(stone, paper, scisser): ")
if player1=="stone" and player2=="paper":
    print("player2 won the game")
elif player1=="stone" and player2=="scissor":
    print("player1 won the game")
elif player1=="paper" and player2=="stone":
    print("player1 won the game")
elif player1=="paper" and player2=="scissor":
    print("player2 won the game")
elif player1=="scissor" and player2=="stone":
    print("player2 won the game")
elif player1=="scissor" and player2=="paper":
    print("player1 won the game")
else:
    print("draw the game")
#####################################################
###############----If-else guess game-----##############
a=20
b=int(input("enter the number"))    
if a==b:
    print("you won the game")
else:
    print("try again")
    c=int(input("enter the number"))
    if a==c:
        print("you won the game")
    else:
        print("try again")
        d=int(input("enter the number"))
        if a==d:
            print("you won the game")
        else:
            print("you lost the game try to next time")
#############################################################

#########----Guess game in loop-----###########
a=20
t=0
for i in range(3):
    b=int(input("enter the number"))
    if a==b:
        print("you won the game")
        break
    elif b<a:
        print("try again")
        t+=1
    else:
        print("try again")
        t+=1
if t>2:
    print("you lose the game")

################### Even and Odd ##################
for i in range(201):
    if i<=100:
        if i%2==0:
            print("odd",i)
    else:
        if i%2!=0:
            print("even",i-100)

i=0
while i<=200:
    if i<=100:
        if i%2==0:
            print("Even:>",i)
    else:
        if i%2!=0:
            print("Odd:>",i-100)
    i+=1

a=1
while a<=100:
    if a%2==0:
        print(a)
    else:
        print(a)
        if a==99:
            a-=97
    a+=2

###############################################################

n=int(input("enter a number"))
i=0
b=0
while (i<=n):
    b=i-1
    print(i,b)
    i+=2


##################################################################################################################
# ______12/03/2021_____#

nu=int(input("Enter your:"))
while True:
    tum=nu
    r=0
    while nu>0:
        d=nu%10
        r=r*10+d
        nu=nu//10
    if r==tum:
        print("Yes",tum,r)
        break
    else:
        print("No",tum,r)
        nu=tum+r

#####__________LCM____________##########

n1=int(input("Enter your:"))
n2=int(input("Enter your:"))
m=n1
m=n2
while True:
    if m%n1==0 and m%n2==0:
        print("LCM is",m)
        break
    m=m+1

################-- Sum three number make one -----###########
n1=int(input("Enter your which number you want make: "))
n2=int(input("Enter your number range: "))
for i in range(1,n2+1):
    v=i
    for j in range(1,n2+1):
        m=j
        for a in range(1,n2+1):
            x=a
            if v+m+x==n1:
                print(v,m,x,"=",v+m+x)
            else:
                continue 

############--- Convert decimal into binary----################### 
decimal = int(input("Enter number which you want to convert: "))
num = ""
while decimal != 0:
    num = str(decimal % 2) + num
    decimal //= 2
print(num)
############################@@@@@@@@@@@@@@@@@@@
##################################
#############################
v=int(input("Guess your number between 1 to 100:"))
winner=20
g=0
game=False
while g<5:
    if winner==v:
        print(f"You win! and guess is correct {g}")
        break
    else:
        if winner>v:
            print("Your gess is to low")
            g+=1
            v=int(input("gues again:"))
        else:
            print("Your gess is to high")
            g+=1
            v=int(input("gues again:"))
    if g==5:
        n=input("Do you want play again [Y/N]:").lower()
        if n=="y":
            g=0
            continue
        else:
            break
#############################################
##############################
###############################################

#######---String implement----################
def str_implement(a,b):
    c=0
    for i in a:
        for j in b:
            if i==j:
                c+=1#len(b)
        if b not in a:
            print(-1)
            break 
    print(c)
x=input()
y=input()
str_implement(x,y)


pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

base_1 = 5
base_2 = 6
height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)
 
############---------LCM AND HCF---------##################
y,x=int(input()),int(input())
for i in range(1,(min(x,y)+1)):
	if x%i==0 and y%i==0:
		d=i
print((x*y)//d,"LCM","\n",d,"HCF")


###################-------count length of same itams----------#####################

a=input("enter the number")
c=0
z=""
for p in a:
    if p in z:
        continue
    else:
        for i in a:
            if p in i and i in p:
                c+=1
                z+=i
                o=i
        print(o,c)
    c=0


a=input("enter the name:> ")
c=0
tc=0
for i in a:
    if (i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='U' or  i=='u' or i=='O' or i=='o'):
        c+=1
        tc=tc-c
print("number of consents",tc)
print("number of vowels",c)


# Python Program to Reverse a Number using While loop    
     
Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10  
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = ",Reverse)