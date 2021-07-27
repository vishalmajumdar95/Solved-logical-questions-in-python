
# import json

# k ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }


# x=open("r.json","w")
# json.dump(k,x,indent=21)
# x.close(	)	

# import json
# x={"fghj":8}
# y=json.dumps(x)
# print(y)



# import json
# x={"Name":"Ram", 
#   "Class":"IV", 
#   "Age":9 }
# h=open("if.py","a")
# y=json.dump(x)
# h.write(y)
# h.close()



# import json
# x={
# 	"name": "David",
# 	"class":"I",
# 	"age": 6  
#   }
# h=open("r.json","a")
# j=json.dump(x,h,indent=4)
# h.close()



# import json
# x={}
# h=open("r.json","a")
# json.dump(x,h,indent=4)
# h.close()

# import json
# x= {
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# y=open("r.json","a")
# json.dump(x,y,indent=4)
# y.close()

# x={
#  "a": 1,
#  "a": 2,
#  "a": 3, 
#  "a": 4,   
#  "b": 1, 
#  "b": 2
#  }
# y={}
# y["a"]=x["a"]
# y["b"]=x["b"]
# print(y)


# import json
# y=open("r.text")
# z=y.readlines()
# c={}
# f=""
# for i in z:
# 	x=i.split(" ")
# 	h=x[1:]
# 	for i in h:
# 		f=f+i+" "
# 	c[x[0]]=f
# 	f=""
# b=open("r.json","a")
# json.dump(c,b,indent=4)
# y.close()





# import json
# x=[["neelam","programer","24","2400"],
#    ["komal","trainer","24","20000"],
#    ["anuradha","HR","25","4000"],
#    ["Abhishek","manager","29","63000"]]
# y=["name","designation","age","salary"]
# z=["emp1","emp2","emp3","emp4"]
# c={}
# g=0
# a={}
# v=0
# for i in x:
# 	while g!=len(x):
# 		c[y[g]]=i[g]
# 		g+=1
# 	a[z[v]]=c
# 	v+=1
# 	g=0
# 	c={}
# x=open("r.json","a")
# json.dump(a,x,indent=4)
# x.close()


# import json
# x={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }
# y=open("n.json","w")
# json.dump(x,y,indent=2)
# y=open("n.json")
# m=json.load(y)
# l=input("type what you want:	")
# y=int(input("type number of items:	"))
# f=int(x["shopping_list"][l])-y
# x["shopping_list"][l]=str(f)
# y=open("n.json","w")
# json.dump(x,y,indent=2)

# import json
# def signup(e,p):
# 	x=open("n.json")		
# 	y=json.load(x)
# 	m={}
# 	m["email"]=e
# 	m["passward"]=p
# 	m["todo"]={"0":"aganda"}
# 	y.append(m)
# 	a=open("n.json","w")
# 	json.dump(y,a,indent=4)
# 	print("signup is sucesfull")
# def login(e,p,):
# 	x=open("n.json")
# 	y=json.load(x)
# 	f=[]
# 	for i in y:
# 		for u in i:
# 			f.append(u)
# 	for o in f: 	
# 		if i[o]==e and i[o]==p:
# 			print("susfull login")
# 			q=input("you want to read your ageanda or wright (r or w):	")
# 			if "r" in q:
# 				print(i["todo"])
# 				break 
# 			else:
# 				print(i["todo"])
# 				z=input("type your aggeda:	")
# 				h=i["todo"]
# 				for c in h:
# 					c=c
# 				u=int(c)
# 				pp=i["todo"]
# 				pp[str(u+1)]=z
# 				q=open("n.json","w")
# 				json.dump(y,q,indent=4)
# 				break
# 		else:
# 			print("your email id is wrong")
# x=input("what you want (login,signup):	")
# if "l" in x:
# 	x=input("type your email id")
# 	y=input("type your email id passward")
# 	login(x,y)
# else:
# 	x=input("type your email id")
# 	y=input("type your email id passward")
# 	signup(x,y)


# import json
# ######## """load""""#

# with open("data_file.json", "r") as read_content:
#     print(json.load(read_content))

# ####### """loads"""
# data = """{ 
#     "Name": "Jennifer Smith", 
#     "Contact Number": 7867567898, 
#     "Email": "jen123@gmail.com", 
#     "Hobbies":["Reading", "Sketching", "Horse Riding"] 
#     }"""

# ######## """dump"""  
# data = {
#     "name": "Satyam kumar",
#     "place": "patna",
#     "skills": [
#         "Raspberry pi",
#         "Machine Learning",
#         "Web Development"
#     ],
#     "email": "xyz@gmail.com",
#     "projects": [
#         "Python Data Mining",
#         "Python Data Science"
#     ]
# }
# with open( "data_file.json" , "w" ) as write:
#     json.dump( data , write )

# person_dict = {"name": "Bob",
# "languages": ["English", "Fench"],
# "married": True,
# "age": 32
# }

# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)
# """dumps"""

# person_dict = {'name': 'Vishal',
# 'age': 17,
# 'job': None
# }
# person_json = json.dumps(person_dict)
# print(person_json)



# import turtle
# colors=["red",'white',"blue","green","orange","yellow","purple","gold"]
# t=turtle.Pen()
# t.speed(40)
# turtle.bgcolor("black")
# for x in range(0,360):
#     t.pencolor(colors[x%8])
#     t.width(x/1001)
#     t.forward(x+21)
#     t.left(140)



















