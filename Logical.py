
# circle_name_per_round_by_player
# dic={}
# for i in range(3):
#     Team_name=input("Enter Your Team Name:")
#     player_name=input("Enter your Team Members Name:")
#     dic[Team_name]=player_name.split()
#     print(dic)
# new=[]
# first=[]
# li=[]
# Round=1
# while Round<=5:
#     print(f"Round {Round}")
#     indivisual_player=[]
#     for i in range(1):
#         for k in dic.values():
#             A=5
#             B=4
#             C=3
#             D=2
#             E=1
#             F=0
#         if Round==2:
#             A=5+1
#             B=4+1
#             C=3+1
#             D=2+1
#             E=1+1

#         elif Round==3:
#             A=5+2
#             B=4+2
#             C=3+2
#             D=2+2
#             E=1+2
        
#         elif Round==4:
#             A=5+3
#             B=4+3
#             C=3+3
#             D=2+3
#             E=1+3
            
#         elif Round==5:
#             A=5+4
#             B=4+4
#             C=3+4
#             D=2+4
#             E=1+4
    
#             for j in range(1):
#                 inp=input(f"Enter Target:A,B,C,D,E,F:{k[0]} ")
#                 sec_inp=input(f"Enter Target:A,B,C,D,E,F:{k[1]} ")
#                 if inp=="A" and sec_inp== "B" or inp == "B" and sec_inp == "A": ## FOR  A B
#                     li.append(A+B)
#                     indivisual_player.append(A)
#                     indivisual_player.append(B)
#                 if sec_inp=="A" and inp==sec_inp : ## FOR A A
#                     A=A+A+2
#                     li.append(A)
#                     indivisual_player.append(A)
#                 if inp=="A" and sec_inp == "C" or inp =="C" and sec_inp == "A": ## FOR A C
#                     li.append(A+C)
#                     indivisual_player.append(A)
#                     indivisual_player.append(C)
#                 if sec_inp =="B" and inp == sec_inp: ## FOR B B
#                     B=B+B+2
#                     li.append(B)
#                     indivisual_player.append(B)
#                 if inp=="A" and sec_inp == "D" or inp =="D" and sec_inp == "A": ## FOR A D
#                     li.append(A+D)
#                     indivisual_player.append(A)
#                     indivisual_player.append(D)
#                 if sec_inp=="C" and inp == sec_inp: ## FOR C C
#                     C=C+C+2
#                     li.append(C)
#                     indivisual_player.append(C)
#                 if inp=="A" and sec_inp == "E" or inp =="E" and sec_inp == "E": ## FOR A E
#                     li.append(A+E)
#                     indivisual_player.append(A)
#                     indivisual_player.append(E)
#                 if sec_inp=="D" and inp == sec_inp: ## FOR D D
#                     D=D+D+2                         
#                     li.append(D)
#                     indivisual_player.append(D)
#                 if inp=="A" and sec_inp == "F" or inp=="F" and sec_inp == "A": ## FOR A F
#                     li.append(A+F)
#                     indivisual_player.append(A)
#                     indivisual_player.append(F)
#                 if sec_inp=="E" and inp == sec_inp: ## FOR E E
#                     E=E+E+2
#                     li.append(E)
#                     indivisual_player.append(E)
#                 if inp=="B" and sec_inp == "C" or inp=="C" and sec_inp == "B": ## FOR B C 
#                     li.append(B+C)
#                     indivisual_player.append(B)
#                     indivisual_player.append(C)
#                 if sec_inp=="F" and inp == sec_inp: ## FOR F F
#                     F=F+F+F
#                     li.append(F)
#                     indivisual_player.append(F)
#                 if inp=="B" and sec_inp == "D" or inp=="D" and sec_inp == "B": ## FOR B D
#                     li.append(B+D)
#                     indivisual_player.append(B)
#                     indivisual_player.append(D)
#                 if  inp=="B" and sec_inp == "E" or inp=="E" and sec_inp == "B" : ## FOR B E
#                     li.append(B+E)
#                     indivisual_player.append(B)
#                     indivisual_player.append(E)
#                 if inp=="B" and sec_inp == "F" or inp=="F" and sec_inp == "B": ## FOR B F
#                     li.append(B+F)
#                     indivisual_player.append(B)
#                     indivisual_player.append(F)
#                 if inp=="C" and sec_inp == "D" or inp=="D" and sec_inp == "C" : ## FOR C D
#                     li.append(C+D)
#                     indivisual_player.append(C)
#                     indivisual_player.append(D)
#                 if inp=="C" and sec_inp == "E" or inp=="E" and sec_inp == "C": ## FOR C E
#                     li.append(C+E)
#                     indivisual_player.append(C)
#                     indivisual_player.append(E)
#                 if inp=="C" and sec_inp == "F" or inp=="F" and sec_inp == "C": ## FOR C F
#                     li.append(C+F)
#                     indivisual_player.append(C)
#                     indivisual_player.append(F)
#                 if inp=="D" and sec_inp == "E" or inp=="E" and sec_inp == "D": ## FOR D E
#                     li.append(D+E)
#                     indivisual_player.append(D)
#                     indivisual_player.append(E)
#                 if inp=="D" and sec_inp == "F" or inp=="F" and sec_inp == "D": ## FOR D F
#                     li.append(D+F)
#                     indivisual_player.append(D)
#                     indivisual_player.append(F)
#                 if inp=="E" and sec_inp == "F" or inp=="F" and sec_inp == "E": ## FOR E F
#                     li.append(E+F)
#                     indivisual_player.append(E)
#                     indivisual_player.append(F) 
#     for k in li:
#         new.append(li[0:3])
#         li.clear()
#     print("SCORE BOARD :",new)
#     Round+=1
#     first.append(indivisual_player)
#     print("Indivisual Score:",first)
# sum_of_first_team=0
# for i in new:
#     sum_of_first_team+=i[0]
# # print(sum_of_first_team)
# sum_of_second_team=0
# for j in new:
#     sum_of_second_team+=j[1]
# # print(sum_of_second_team)
# sum_of_third_team=0
# for N in new:
#     sum_of_third_team+=N[2]
# # print(sum_of_third_team)
# if sum_of_first_team>=60:
#     print("First team wins","Total Score:",sum_of_first_team)
# else:
#     print("First team lose","Total Score:",sum_of_first_team)
# if sum_of_second_team>=60:
#     print("second team wins","Total Score:",sum_of_second_team)
# else:
#     print("second team lose","Total Score:",sum_of_second_team)
# if sum_of_third_team>=60:
#     print("third team lose","Total Score:",sum_of_third_team)
# else:
#     print("third team lose","Total Score:",sum_of_third_team)
# # f=open("score_board.txt","w+")
# # f.write(new)
# # f.write(indivisual_player)
