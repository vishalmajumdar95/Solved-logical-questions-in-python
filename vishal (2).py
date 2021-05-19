# a=[]
# for i in range(3):
#     b=[]
#     for j in range(3):
#         j=int(input("Enter you namber:>"))
#         b.append(j)
#     a.append(b)
# print("Matrix is ....")
# for i in range(3):
#     for j in range(3):
#         print(a[i][j],end=" ")
#     print()
# s1=0
# s2=0
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             s1=s1+a[i][j]
#         if i+j==3-1:
#             s2=s2+a[i][j]
# if s1!=s2:
#     f=1
# else:
#     for i in range(3):
#         s3=0
#         s4=0
#         for j in range(3):
#             s3=s3+a[i][j]
#             s4=s4+a[j][i]
#         if s3!=s4:
#             f=1
#         elif s4!=s1:
#             f=1
#         else:
#             f=0
# if f==0:
#     print("Marrix is Magic square")
# else:
#     print("Marrix is not Magic square")



# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# v=0
# v1=0
# v2=0

# for i in magic_square:
#     v=sum(magic_square[0])
#     v1=sum(magic_square[2])
#     v2=sum(magic_square[3])
#     for j in i[0]:
#         v=i[j]+v
#         print("yes magic_square hai")
        # for x in i[1]:
        #     v1=i[x]+v1

#             # print("yes magic_square hai")


# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]

# # print (type(magic_square))
# # print (sum(magic_square[0]))
# # print (sum(magic_square[1]))

# v=(sum(magic_square[0]))
# v1=(sum(magic_square[1]))
# v2=(sum(magic_square[2])) 
# if v==v1:
#     if v1==v2:
#         if v2==v:
#             print("yes magic_square hai")
# else:
#     print("no magic_square nhi hai")




# print('''.......welcome to the  game of  HANGMAN.....''')
# name=input("please enter your name :>")
# print("Welcome in the Game!\n","......",name,"let's play the game .........")
# w="Vishal"
# n=("_")
# while True:
#     t=len(w)
#     a=0
#     for i in range(t):
#         b=0
#         for i in w:
#             if i in n:
#                 print(i,end="")
#             else:
#                 print(" _ ",end="")
#                 b+=1
#         if b==0:
#             print("...Congrats",name,"you won the game....")
#             break
#         print("put your guess")
#         guess=input("choose a character :>")
#         n+=guess
#         if guess not in w:
#             print(H1[a])
#             t-=1
#             a+=1
#             print("you have",t,"more chance")
#             if t==0:
#                 print("you are lose")
#     print("do you want to playaaa: y/n ")
#     play=input()
#     if play =="y":
#         print("thank you")
#         continue
#     else:
#         print("good bye")
#         break 


# m={"vishal":17,"rajeshwer":18,"siddik":19,"suraj":20,"t":21,"x":22,"z":23}
# print("New dic:>",m)
# n1={}
# l=len(m)
# for i in range(l):
#     n=0
#     for i in m.values():
#         if i>n:
#             n=i
# print(n)


# print("+++++")
# print("+   +")
# print("+   +")
# print("+++++")
# print("+  +")
# print("+   +")
# print("+    +")

# i=0
# while i>0:


# def list_sum(num):
#         i=num.pop(0)
#         if len(num)==0:
#             return i
#         else:
#             return i + list_sum(num)
# print(list_sum([1,3,5,7,9]))


# num=int(input("Enter any number"))
# ld=num%10
# if ld%3==0:
#     print("Last digit of number is divisible by 3 ")
# else:
#     print("Last digit of number is not divisible by 3 ")





###########...............KBC...................##########
# print('''
# ..... Welcome To you in KBC ..... 
# ''')
# questions=[
#     " 1.How many continents in the world?",
#     " 2.Which day is observed as the world standard day?",
#     " 3.what is the national food of Navgurukul?",
#     " 4.Who is the author of the epic 'Magdoot'?",
#     " 5.September 27 is celebrated every year as?",
#     " 6.How many planets are there in our solar system?",
#     " 7.Who is the president of America?",
#     " 8.Where is the Navgurukul's girls campus in India?",
#     " 9.Who's that person name who said that 'Me madharchood hu jo yaha aaya'",
#     " 10.Who is Binod?",
#     " 11.How many stairs steps are in our campus?"

# ]
# options=[
#     ["1","5","4","7","50:50"],
#     ["June 26","Oct 14","Nov 15","Dec 2","50:50"],
#     ["Rice","Fried","Fried Rice","Dal","50:50"],
#     ["Vamlmiki","Banabhata","Kalidas","Vishal","50:50"],
#     ["Teacher,s Day","Natinal Integretion Day","World Tourism Day","International Day","50:50"],
#     ["5","8","9","6","50:50"],
#     ["Joe Biden","Donald Trump","Emmanuel Macron","Barack Obama","50:50"],
#     ["Pune","Banglore","Delhi","Gurugram","50:50"],
#     ["Baloon Wala","Parachute Wala","Ship Wala","Circus Wala","50:50"],
#     ["Riyaz","Peter","Abhi Pata nhi hai","Deepak","50:50"],
#     ["16","15","13","14","50:50"]
#     ]
# solutions=[4,2,3,3,3,2,1,2,2,3,1]
# sol=[
#     [2,4],
#     [2,3],
#     [2,3],
#     [3,1],
#     [4,1],
#     [2,4],
#     [4,1],
#     [2,4],
#     [2,3],
#     [2,1],
#     [4,3]
# ] 
# n1=0  
# n=0

# k=1
# d=0
# for i in questions:      
#     print(i)
#     if n1==0:
#         print('''     Here Is Your Options...''')
#     for i in options[n]:
#         if k==6:
#             k=1
#         print(" "+str(k),':', i)
#         k+=1
#     inp=int(input('''
#  Choose Your Answer:'''))
    
#     if inp==solutions[n]:
#         print('''
#  Congratulation! You Won
#         ''')
#     elif inp==5:
#         if d==1:
#             print('''
#  Sorry!! You Already Choosed This 50:50 option
#             ''')
#         else:
#             for i in range(1):
#                 print(''' Choose Your 50:50 Answer:''', sol[n])
#             inp=int(input(''' Choose Your Answer:'''))
#             if inp==solutions[n]:
#                 print(''' Congratulation! You Won Again
#                 ''')
#                 d+=1
#             else:
#                 print('''Your Answer Is Wrong.''')
                
#     else:
#         print('''
#         Your Answer Is Wrong.''')
#         break
#     n+=1
#     n1+=1


# n=[1,2,6,12,23,7,3,9]
# l=len(n)
# for j in range(l):
#     for i in range(l):
#         if n[i]>n[j]:
#             m=n[i]
#             n[i]=n[j]
#             n[i]=m
# print(n)

# a=[12,66,55,88,45,47,64,81,20]
# l=len(a)
# i=0
# for i in range(l):
#     for j in range(i+1,l):
#         if a[i]>a[j]:
#             v=a[i]
#             a[i]=a[j]
#             a[j]=v
# print(a)