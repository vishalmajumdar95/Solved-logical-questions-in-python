
listto=[i for i in range(10)]
print(listto)

l=list(range(10))
print(l)

listto=[i for i in range(0,10,2)]
print(listto)

l=list(range(0,10,2))
print(l)

s="vishal,vishu,siddik,suraj"
spl=s.split(",")
print(spl)

s2="Python"
s3=list(s2)
print(s3)

n=1234678
into=[i for i in str(n)]
print(into)

my_dic={"v":1,"i":2,"s":3,"h":4,"a":5,"l":6,}
k_l=list(my_dic.keys())
print(k_l)

my_dic={"v":1,"i":2,"s":3,"h":4,"a":5,"l":6,}
k_l=list(my_dic.values())
print(k_l)

l=[1,7,5,3,9,12,8]
l.sort()
print(l)

l=[1,7,5,3,9,12,8]
l.sort(reverse=True)
print(l)

l=[1,2,3,4,5,6,7,8]
l.reverse()
print(l)

l=[1,7,5,3,9,12,8]
# l[1:6]=[]
# print(l)
# l[1:1]=[10,20]
# print(l)
l[1:3]=[30,40]
print(l)

l=[1,7,5,3,9,12,8]
for i in range(len(l)):
    print("index:",str(i),"| value:",l[i],"|","Negative_index:","-"+str(i))


students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
counter = 0
while counter < length:
    print (students[counter]+":-"+str(marks[counter]))
    counter+=1 

####count length of list#####
num=[50, 40, 23, 70, 56, 12, 5, 10, 7]
v=0
m=[]
while m!=num:
	c=num[v]
	m.append(c)
	v+=1
print(v)

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
c=0
for i in numbers:
    c+=1
print(c)

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
c=0
for i in numbers:
    if i>20 and i<40:
        c+=1
        print(i)
print(c)

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
c=0
l=len(numbers)
i=0
while i!=l:
    if numbers[i]>20 and numbers[i]<40:
        c+=1
        print(numbers[i])
    i+=1
print(c)

####################----First Max number in list----####################

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
m=0
for i in numbers:
    if i>m:
        m=i
print(m)


####################----Second Max number in list----####################

n = [50, 40, 23, 70, 56, 12, 5, 10, 7,62]
for i in range(2):
    m=0
    for i in n:
        if i>m:
            m=i
    n.remove(m)
print(m)

m=0
v=0
while v<2:
    i=0
    l=len(n)
    m=n[0]
    while i<l:
        if n[i]>m:
            m=n[i]
        i+=1
    n.remove(m)    
    v+=1
print(m)


####################----third Max number in list----####################

n = [50, 40, 23, 70, 56, 12, 5, 10, 7,62]
for i in range(3):
    m=0
    for i in n:
        if i>m:
            m=i
    n.remove(m)
print(m)

m=0
v=0
while v<3:
    i=0
    l=len(n)
    m=n[0]
    while i<l:
        if n[i]>m:
            m=n[i]
        i+=1
    n.remove(m)    
    v+=1
print(m)



####################----first Min number in list----####################

v=[1,2,2,8,6,4,8,3,2,9,4]
m=v[0]
for i in v:
    if m>i:
        m=i
print(m)

###################----Second Min number in list----####################

v=[1,2,2,8,6,4,8,3,2,9,4]
l=len(v)
for j in range(2):
    m=v[0]
    for i in v:
        if m>i:
            m=i
    v.remove(m)
print(m)

###################----third Min number in list----####################

v=[1,2,2,8,6,4,8,3,2,9,4]
l=len(v)
for j in range(3):
    m=v[0]
    for i in v:
        if m>i:
            m=i
    v.remove(m)
print(m)

####################################################################

student_marks = [23, 45, 89, 90, 56, 80] 
length = len(student_marks)
index = 0
total_marks = 0
while index < len(student_marks):
    total_marks = student_marks[index] + total_marks
    index = index + 1
print ("Total Marks: " + str(total_marks))

student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
list_length = len(student_marks)
index = 0
less_than50 = 0
more_than50 = 0
while index < list_length:
    marks = student_marks[index]
    if marks < 50:
        less_than50 = less_than50 + 1
    else:
        more_than50 = more_than50 + 1
    index = index + 1
print ("Marks more than 50: " + str(more_than50))
print ("Marks less than 50: " + str(less_than50))

##### Check the list is ascending or descending ###########

n=[9,8,7,6,5,4,2,1.9]
n=[1,2,3,4,5,6]
n=[2,89,54,3,3,9,7,1,8,98,5]
n=[98,4,4,5,67,90,8,7,63]
c=n.copy()
if n[-1]>n[0]:
    n1=[]
    l=len(n)
    for j in range(l):
        m=n[0]
        for i in n:
            if i< m:
                m=i
        n.remove(m)
        n1.append(m)
    if c==n1:
        print("Yes! it's is in ascending")
    else:
        print("No! it's is in ascending")
else:
    n1=[]
    c=n.copy()
    l=len(n)
    for j in range(l):
        m=n[0]
        for i in n:
            if i>m:
                m=i
        n.remove(m)
        n1.append(m)
    if c==n1:
        print("Yes! it's is in descending")
    else:
        print("No! it's is in descending")

##### Same question do with another way #####

a=[120,66,65,54,47,32,21,20]
v=a.copy()
print(a)
if a[0]<a[-1]:
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if v[i]>v[j]:
                n=v[i]
                v[i]=v[j]
                v[j]=n
    if v==a:
        print("it is a sorted list:>",a)
    else:
        print("it is not a sorted list:>",a)
else:
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                v=a[i]
                a[i]=a[j]
                a[j]=v
    if v==a:
        print("it is a dis list:>",a)
    else:
        print("it is not a dis list:>",a)


######## Flettan list ###########

import itertools
o = [[2,4,3],[1,5,6], [9], [7,9,0]]
n = list(itertools.chain(*o))
print(n)


############# Accending the ist ############

a=[1,2,7,16,123,11,26,12]
b=[]
l=len(a)
for i in range(l):
    maxi=a[0]
    for j in a:
        if j>maxi:
            maxi=j
    a.remove(maxi)
    b.append(maxi)
print(b)


########################################################

a=[[1,2,3],[4,5,6],[1,2,3]]
i = 0
while i<len(a):
  j = 0
  while j < len(a[i]):
    print (a[i][j])
    j = j+1
  i = i+1

########*******Remove duplicate number in list----###########

a=[1,2,4,12,3,1,3,2,21]
t = []
for x in a:
    if x not in t:
        t.append(x)   
print(t)

######### Sum the list items ###########

a=[[12,2],[1,2],[21]]
s=0
for i in a:
    for j in i:
        s+=j
print(s)
################################

##########*****sum the list item in pairs and cross pairs and then find the three max number****#######

a=[9,6,7]
b=[8,4,5]
x=[]
y=len(a)
z=[]
for i in a:
    s=0
    for j in b:
        s=i+j
        x.append(s)
print(x)
for i in range(y):
    m=max(x)
    x.remove(m)
    z.append(m)
print(z)

#########################

#### sum the two list last value #####

n=[50, 60, 10,12] 
m=[10, 20, 15,10]
v=0
for x in n:
    for y in m:
        continue
    v=x+y
print(v)

#################################


### sum the list item in cross pairs ########

list1=[50, 60, 10] 
list2=[10, 20, 13]
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
resList = [x+y for x in list1 for y in list2]
print(resList)

list1=[50, 60, 10] 
list2=[10, 20, 13]
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
f=[]
for i in list1:
    for j in list2:
        v=i+j
        # print([v])
        f.append(v)
print(f)

#############################################

################# find the max list in main list ##############

num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(num, key=sum))

##########################################

nums = []
for i in range(3):
    nums.append([])
    for j in range(1, 4):
        nums[i].append(j)
print("3X3 grid with numbers:")
print(nums)


############# find the list items which is sec and un #######################

def my_sec_un(a,b):
    sec=[]
    un=[]
    for i in a:
        for j in b:
            if i==j:
                b.remove(j)
                sec.append(i)
        else:
            un.append(i)
    v=input()
    if v=="sec":
        print(sec)
    elif v=="un":
        print(un+b)
    else:
        print(sec,un+b)
a=[1,2,3,4,5,6,343,5465,565777]
b=[2,3,8,9,23,5]
my_sec_un(a,b)

def my_sec_un(a,b):
    sec=[]
    un=[]
    for i in a:
        if i not in b:
            un.append(i)
        else:
            sec.append(i)
            # b.remove(b[0])
    v=input("Do you want (sec or un): ")
    if v=="sec":
        print(sec)
    elif v=="un":
        print(un+b)
    else:
        print(sec,un+b)
a=[1,2,3,4,5,6,8]
print("List one:-",a)
b=[2,3,8,9,5]
print("List second:-",b)
my_sec_un(a,b)

###########################################################


####################---Cheak list Palindrome----################

String=input()
list1=list(String)
print(list1)
list2=list1[::-1]
print(list2)
if list1==list2:
    print("Yes it's Palindrome")
else:
    print("No it's Palindrome")

p=["n","i","t","i","n"]
v=[]
for i in range(len(p)):
    h=p[i-1]
    v.append(h)
for i in p[::-1]:
    v.append(i)
if p==v:
    print("Palindrome hai")
else:
    print("Palindrome nhi hai")

#########################################################

##################---reverse list---#########################

arr=[]
string=int(input("enter len of list:"))
for i in range(string):
    item=int(input("enter items of list:"))
    arr.append(item)
i=0
j=string-1
while i<j:
    t=arr[i]
    arr[i],arr[j]=arr[j],t
    i+=1
    j-=1
print("list after reverse=>")
for i in range(string):
    print(arr[i])

############ Solve that question with another way ##########

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
print(places)
l=len(places)
f=[]
i=0
while i!=l:
    f.append(places[i-1])
    i+=1
print(f)

###################################

a=[[1,2,3],[4,5,6]]
i = 0
while i<len(a):
  j = 0
  while j < len(a[i]):
    print (a[i][j])
    j = j+1
  i = i+1

###########----Find the list which items are not aviable in another----########### 

a = [1,2,3,4,5,6]
b = [2,3,1,0,6,7] 
k=[]
for i in a:
    if i not in b:
        k.append(i)
print(k)

#######---Sum the list all items---#########

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
s=0
for i in marks:
    for j in i:
        s=s+j
print(s)


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
] 
s=0
for i in marks:
    for j in i:
        s=s+j
print(s)


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
] 
s=0
for i in marks:
    for j in i:
        s=s+j
print(s)

#########################

a=int(input())
b=[]
c=[]
for i in range (a):
    d=int(input())
    b.append(d)
for j in b:
    if j not in c:
        c.append(j)
print(c)


###########-----Find the Target in this list----#############

def target_indexing(a,target):
    for i in range (len(a)):
        if a[i]==target:
            print(a.index(target))
            break
        else:
            a.insert(i,target)
            a.sort()
            print(a.index(target))
            break
list1=[4,6,7,8,9,10]
print("This list:-",list1)
target=int(input("Target the item in this list:- "))
target_indexing(list1,target)

#####################################################

ni=int(input("how many times you want to added:> "))
new_list=[]
i=0
while i<ni:
    n=int(input("number of times:> "))
    new_list.append(n)
    i+=1
print(new_list)

sm = [23, 45, 89, 90, 56, 80] 
l = len(sm)
i = 0
tm = 0 
# for i in sm:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
while i < len(sm):
    tm = sm[i] + tm
    i = i + 1
print ("Total Marks: " + str(tm))



#############len function code:>

v=["vishal",24,7,9,5]
v="123456734567"
c=0
for i in v:
    c+=1
print(c)

v1="123456734567"
print(sum(1 for ch in v1))

##############################################

v = [23, 45, 89, 29, 56, 80]
for i in v:
    if i>20 and i<40:
        print("index:-",v.index(i),"item:-",i)

##############################################


#Fallten list
l1=[[1,2,3,4,4,4,9],[9,8,6,],[4,2,6,8,5]]
l2=[]
for i in l1:
    for j in i:
        l2.append(j)
print(l2)

l1=[1,2,3,4,[1,2,3,4,4,4,9],1,2,3]
l2=[]
for i in l1:
    l2.append(i)
    if type(i)==list:
        for j in i:
            l2.append(j)
        else:
            l2.remove(i)
print(l2)

#################################################


#######frist question

a = [1,2,3,4,5,6,7,8]
b = [a[-1]]+a[:-1]
print("old list:",a)
a = (b)
print("new list:",a)

########## second question

v=int(input("How many number want to add: "))
i=0
a=[]
while i<v:
    print("Enter number")
    num = int(input("Enter your: "))
    a.append(num)
    i = i+1
n = input("check your number\n")
if n in a:
    print("Yes! it is there")
else:
    print("No! it is not there")

############----->Reverse the list items<-------##############

list=["Vishal","suraj","23456"]
print("New list1: ",list)
list1=[]
for i in list:
    string=""
    for j in i:
        string=j+string
    list1.append(v)
print("this is your recverse list iteams:",list1)

############--->Remove list2 items from list1<---#########
list1=[1,1,2,2,23]
list2=[1,2]
for i in list2:
    for j in list1:
        if (i==j):
            list1.remove(i)
print(list1)

#############-----> Nested list question<-------############### 

x=int(input("How many list you want: "))
y=int(input("How many items you want to add in list: "))
m,b,=[],0
for i in range(y):
    m.append([])
    for j in range(y):
    # while n!=y:
        v=input("Enter your items: ")
        if v >="a" and v<="z" or v>="A" and v<="Z":
            m[b].append(v)
        elif v in "1234567890":
            v=int(v)
            m[b].append(v)
        else:
            v=float(v)
            m[b].append(v)
    b+=1
print(m)

########################################

list1=list(input())
lit2=list(input())
for i in lit2:
    for j in list1:
        if (i==j):
            list1.remove(i)
print(list1)

############################
li=[i for i in range(100) if i%2==0]
print(li)


a = [1,2,3,4,5,6,7,8]
b = [a[-1]]+a[:-1]
print("old list:",a)
a = (b)
print("new list:",a)


#####################################################
def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 29, 75, 123, 62, 9]
num=num_list.copy()
num_list_sub_20 = numbers_less_than_twenty(num)
print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)

