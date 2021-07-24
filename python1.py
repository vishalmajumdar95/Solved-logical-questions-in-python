# ........Calcutor............

inp = input("enter : ")
a = []
num = ""

for i in inp:
    if i.isdigit():
        num+=i
    else:
        a.append(num)
        a.append(i)
        num=''
a.append(num)
print(a)


#This code for Division
while "/" in a :
    n = a.index("/")
    b = float(a[n-1]) / float(a[n+1])
    a[n-1:n+2]=[b]
    print(b,"step 1")


#This code for Multiplication
while "*" in a:
    n = a.index("*")
    b = float(a[n-1]) * float(a[n+1])
    a[n-1:n+2]=[b]
    print(b,"step 2")


#This code for Addition
while "+" in a :
    n = a.index("+")
    b = float(a[n-1]) + float(a[n+1])
    a[n-1:n+2]=[b]
    print(b,"step 3")


#This code for Substraction
while "-" in a :
    n = a.index("-")
    b = float(a[n-1]) - float(a[n+1])
    a[n-1:n+2]=[b]
    print(b,"step 4")

print(b)

#######################################################################################################################################

# <<<<<<.............KBC..............>>>>>>>>>>

from playsound import playsound
print('''
.....# Welcome To you in KBC #..... 
''')
questions=[
    " 1.How many continents in the world?",
    " 2.Which day is observed as the world standard day?",
    " 3.what is the national food of Navgurukul?",
    " 4.Who is the author of the epic 'Magdoot'?",
    " 5.September 27 is celebrated every year as?",
    " 6.How many planets are there in our solar system?",
    " 7.Who is the president of America?",
    " 8.Where is the Navgurukul's girls campus in India?",
    " 9.Who's that person name who said that 'Me madharchood hu jo yaha aaya'",
    " 10.Who is Binod?",
    " 11.How many stairs steps are in our campus?"

]
options=[
    ["1","5","4","7","50:50"],
    ["June 26","Oct 14","Nov 15","Dec 2","50:50"],
    ["Rice","Fried","Fried Rice","Dal","50:50"],
    ["Vamlmiki","Banabhata","Kalidas","Vishal","50:50"],
    ["Teacher,s Day","Natinal Integretion Day","World Tourism Day","International Day","50:50"],
    ["5","8","9","6","50:50"],
    ["Joe Biden","Donald Trump","Emmanuel Macron","Barack Obama","50:50"],
    ["Pune","Banglore","Delhi","Gurugram","50:50"],
    ["Baloon Wala","Parachute Wala","Ship Wala","Circus Wala","50:50"],
    ["Riyaz","Peter","Abhi Pata nhi hai","Deepak","50:50"],
    ["16","15","13","14","50:50"]
    ]
solutions=[4,2,3,3,3,2,1,2,2,3,1]
sol=[
    [2,4],
    [2,3],
    [2,3],
    [3,1],
    [4,1],
    [2,4],
    [4,1],
    [2,4],
    [2,3],
    [2,1],
    [4,3]
] 
n1=0  
n=0

k=1
d=0
for i in questions:      
    print(i)
    if n1==0:
        print('''     Here Is Your Options...''')
    for i in options[n]:
        if k==6:
            k=1
        print(" "+str(k),':', i)
        k+=1
    inp=int(input('''
 Choose Your Answer:'''))
    
    if inp==solutions[n]:
        print('''
 Congratulation! You Won
        ''')
    elif inp==5:
        if d==1:
            print('''
 Sorry!! You Already Choosed This 50:50 option
            ''')
        else:
            for i in range(1):
                print(''' Choose Your 50:50 Answer:''', sol[n])
            inp=int(input(''' Choose Your Answer:'''))
            if inp==solutions[n]:
                print(''' Congratulation! You Won Again
                ''')
                d+=1
            else:
                print('''Your Answer Is Wrong.''')
                
    else:
        print('''
        Your Answer Is Wrong.''')
        break
    n+=1
    n1+=1


# <<<<<<..........Pratice Question............>>>>>>>>>
#

lis1=["Who was the first Indian woman in Space?",
"Who was the first Man to Climb Mount Everest Without Oxygen?"
"Who built the Jama Masjid?"
"Who wrote the Indian National Anthem?"
"ho was the first Indian Scientist to win a Nobel Prize?8."
" Who was the first Indian woman to win the Miss World Title?"
]
list2=[]

print("\U0001F600")

from playsound import playsound
print('''Welcome To you in KBC, 
Lets Start The Game...
''')


print("\U0001F600","\U0001F600","\U0001F600","\U0001F600","\U0001F600","\U0001F600","\U0001F600","\U0001F600","\U0001F600","\U0001F600","\U0001F600")


w="vishal"
a=6
g=[]
d=False
while not d:
    for i in w:
        if i.lower() in g:
            print(i,end=" ")
        else:
            print("_",end=" ")
    print("")
    
    guess=input("next guess:>")
    g.append(guess.lower())
    if guess.lower() not in w.lower():
        a-=1
        if a==0:
            break

    d=True
    if i in w:
        if i.lower() not in g:
            d=False
if d:
    print(".....You win this game......")
else:
    print("You Game over!")
