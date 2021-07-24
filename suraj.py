i=0
a=[]
while i<3:
    b=[]
    for j in range(3):
        j=int(input("Enter you namber:>"))
        b.append(j)
    a.append(b)
    i+=1

print()
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    # i+=1
    print()
    
s1=0
s2=0
for i in range(3):
    for j in range(3):
        if i==j:
            s1=s1+a[i][j]
        if i+j==3-1:
            s2=s2+a[i][j]
if s1!=s2:
    f=2
else:
    for i in range(3):
        s3=0
        s4=0
        for j in range(3):
            s3=s3+a[i][j]
            s4=s4+a[j][i]
        if s3!=s4:
            f=2
        elif s4!=s1:
            f=2
        else:
            f=1
if f==1:
    print("It is Magic square")
else:
    print("It is not Magic square")

v="vishalsvishal"
v1=""
a=int(len(v)/2)
for i in range(a):
    v1=i+v1
           
print(v1)

import time
p1=time.time()
n=[8,65,3,63,3,56,2,35,1]
n1=[]
l=len(n)
while n:
    m=n[0]
    for i in n:
        if i< m:
            m=i
    n.remove(m)
    n1.append(m)
p2=time.time()
print(n1)
print(p2-p1)

n=[8,65,3,63,3,56,2,35,1,324,45,1241,54515,5,3]
n1=[]
l=len(n)
for j in range(l):
    m=n[0]
    for i in n:
        if i< m:
            m=i
    n.remove(m)
    n1.append(m)
print(n1)

# ...first Max number in list......

n=[8,65,3,63,34,56,2,35,1]
maxi=n[0]
for i in n:
    if i> maxi:
        maxi=i
print(maxi)

# ...Second Max number in list......

n=[8,65,3,63,34,56,2,35,1]
for j in range(2):
    maxi=n[0]
    for i in n:
        if i> maxi:
            maxi=i
    n.remove(maxi)
print(maxi)

# ...their Max number in list......

n=[8,65,3,63,34,56,2,35,1]
for j in range(3):
    maxi=n[0]
    for i in n:
        if i> maxi:
            maxi=i
    n.remove(maxi)
print(maxi)

# ...first Min number in list......

n=[8,65,3,63,34,56,2,35,1]
mini=n[0]
for i in n:
    if i< mini:
        mini=i
print(mini)
# ...Second Min number in list......

n=[8,65,3,63,34,56,2,35,1]
for j in range(2):
    mini=n[0]
    for i in n:
        if i< mini:
            mini=i
    n.remove(mini)
print(mini)
# ...thrid Min number in list......

n=[8,65,3,63,34,56,2,35,1]
for j in range(3):
    mini=n[0]
    for i in n:
        if i< mini:
            mini=i
    n.remove(mini)
print(mini)

###############################################################



y=[[1,2,3],[1,2,3],[1,2,3]]
h=0
for x in y:
	for c in x:
		h+=c
print(h)


x=input("type your name:  ")
b={}
for y in x:
	if y not in b:
		b[y]=1
	else:
		b[y]+=1
print(b)



x=[1,2,3,5,1,9,7,6,8,8,6]
# x=list(input())
v=0
m=[]
while m!=x:
	c=x[v]
	m.append(c)
	v+=1
print(v)

r=input("enter your string:>")
v=input("remove your want:>")
n=input("put you want")
for i in r:
	if i==v:
		a = r.replace(v,n)
print(a)


m = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
a=0
b=0
c=0
d=0
v=len(m)
for i in range(v):
    for j in range(v):
        if i==j:
            a=a+m[i][j]
        elif i+j==3-1:
            b=b+m[i][j]
if a!=b:
    x=1
else:
    for i in m:
        c=0
        d=0
        for j in i:
            c=c+m[i][j]
            d=d+m[j][i]
        if d!=c:
            x=1
        elif d!=a:
            x=1
        else:
            x=0
if x==0:
    print("it is Magic Square")
else:
    print("it is not Magice Square")

