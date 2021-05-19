# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# if a>b and a>c:
# 	print('a')
# elif b<a and b<c:
# 	print('b')
# else:
# 	print('c')
    	


# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# if a>b:
# 	if b>a:
# 		print(a)
# 	elif b<c:
# 		p=rint(b)
# else:
# 	print(c)


# a="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"
# b="q"or"w"or"e"or"r"or"t"or"y"or"u"or"i"or"o"or"p"or"a"or"s"or"d"or"f"or"g"or"h"or"j"or"k"or"l"or"z"or"x"or"c"or"v"or"b"or"n"
# c="Q"or"W"or"E"or"R"or"T"or"Y"or"U"or"I"or"O"or"P"or"A"or"S"or"D"or"F"or"G"or"H"or"J"or"K"or"L"or"Z"or"X"or"C"or"V"or"B"or"N"
# d="!"or"@"or"#"or"%"or"&"or"+"
# x=input("Enter a passwod ")
# if(len(x)==8):
# 	if "0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8" in x:
# 		if "q"or"w"or"e"or"r"or"t"or"y"or"u"or"i"or"o"or"p"or"a"or"s"or"d"or"f"or"g"or"h"or"j"or"k"or"l"or"z"or"x"or"c"or"v"or"b"or"n" in x:
# 			if "Q"or"W"or"E"or"R"or"T"or"Y"or"U"or"I"or"O"or"P"or"A"or"S"or"D"or"F"or"G"or"H"or"J"or"K"or"L"or"Z"or"X"or"C"or"V"or"B"or"N" in x:
# 				if  "!"or"@"or"#"or"%"or"&" in x:
# 					print("this is a strong password")
# else:
	# print("invaid password")

# x=int(input("Enter a number"))
# if x%2==0:
# 	print("it is not a prime number")
# else:
# 	print("it is a prime number ")




z={}
q={}
w={}
e={}
r={}
pp={}
o={}
l={}
a={}
b=[]
import random
r1={"room1":["Akhilesh","Bijendar","Tarique","Prabhakar","umash","Bhupander"]}
r6={"room6":["Chandan","Ranjan","Ramesh","Akash","Raj kumar"]}
r7={"room7":["Roshan","Baskar","Santosh","kartik","Rajeshwer"]}
r8={"room8":["yogi","Vishal","prakash","Subdip","Hemant"]}
r9={"room9":["tushar"]}
r10={"room10":["ajit","Riyaz","Siddik","Deepak","Dhruv","Paritosh"]}
r11={"room11":["baljeet","navid"]}
r12={"room12":["vivek","Shubam","Rohit","Sonu","Sampath"]}
x=["Akhilesh","Bijendar","Tarique","Prabhakar","umash","Bhupander","Chandan","Ranjan","Ramesh","Akash","Raj kumar","Roshan","Baskar","Santosh","kartik","Rajeshwer","tushar","yogi","Vishal","prakash","Subdip","Hemant","ajit","Riyaz","Siddik","Deepak","Dhruv","Paritosh","baljeet","navid","vivek","Shubam","Rohit","Sonu","Sampath"]
n=1
p6=0
p7=0
p8=0
p9=0
p10=0
p11=0
p12=0
p1=0
for v in x:
	t=random.randint(0,34)
	i=x[t]
	if i not in b: 
		if i not in r6["room6"] and p6<=9:
			a[n]=i
			z["room6"]=a
			b.append(i)
			n+=1
			p6+=1
		elif i not in r7["room7"] and p7<=7:
			a[n]=i
			w["room7"]=a
			n+=1
			b.append(i)
			p7+=1
		elif i not in r8["room8"] and p8<=5:
			a[n]=i
			r["room8"]=a
			n+=1
			b.append(i)
			p8+=1
		elif i not in r9["room9"] and p9<=2:
			a[n]=i
			pp["room9"]=a
			n+=1
			b.append(i)
			p9+=1
		elif i not in r10["room10"] and p10<=7:
			a[n]=i
			q["room10"]=a
			n+=1
			b.append(i)
			p10+=1
		elif i not in r11["room11"] and p11<=3:
			a[n]=i
			o["room11"]=a
			n+=1
			b.append(i)
			p11+=1
		elif i not in r1["room1"] and p1<=7:
			a[n]=i
			l["room1"]=a
			n+=1
			b.append(i)
			p1+=1
		else:
			if i not in r12["room12"] and p12<=9:
				a[n]=i
				e["room12"]=a
				n+=1
				b.append(i)
				p12+=1
print(z)
print(e)
print(r)
print(q)
print(l)
print(o)
print(pp)
print(w)

