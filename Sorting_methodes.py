# # ################*******My Bubble sort method******#############

# # #####--My oun approach to the list ---#####
# # n=["vishal","vishu","suraj","v","s","z","Z"]
# n=[8,65,3,63,3,56,2,35,1]
# print("New list :>",n)
# n1=[]
# l=len(n)
# for j in range(l):
#     m=n[0]
#     for i in n:
#         if i< m:
#             m=i
#     n.remove(m)
#     n1.append(m)
# print("Bubble sort list :>",n1)

# #####---Second approach---#####

# arr=[120,66,65,54,47,32,21,20]
# print("New list:-",arr)
# l=len(arr)
# i=0
# for i in range(l):
#     for j in range(i+1,l):
#         if arr[i]>arr[j]:
#             n=arr[i]
#             arr[i],arr[j]=arr[j],n
# print("Bubble sort list :>",arr)



##########-------- Insertion sort ---------#############
# list=[12,54,67,3,4,58,34]
# print("New list:-",list)
# for i in range(len(list)):
#     r=list[i]
#     s=i
#     while s>0 and list[s-1]>r:
#         list[s]=list[s-1]
#         s=s-1
#     list[s]=r
# print("Insertion sort list :>",list)


# #########---Merge sort-----#############

# new=[12,54,67,3,4,58,34]
# print("New list: ",new)
# l=len(new)
# if l>1:
#     m=l//2
#     l=new[m:]
#     r=new[:m]
#     i=0
#     j=0
#     v=0
#     while i<len(l) and j<len(r):
#         if l[i]<r[j]:
#             new[v]=l[i]
#             i+=1
#         else:
#             new[v]=r[j]
#             j+=1
#         v+=1
#     while i<len(l):
#         new[v]=l[i]
#         i+=1
#         v+=1
#     while i<len(r):
#         new[v]=r[j]
#         j+=1
#         v+=1
# print("Merge List: ",new)

############---Bubble sort----############

# a=[2,5,8,6,10,7,1,4,9]
# for i in range(len(a)):
#     s=False
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#             s=True
#         j+=1
#     if s==False:
#         break
# print(a)

# y = [1,1,2,2,3,34,4,45]  
# n = 0
# u=len(y)
# while n!=u:  
# 	for i in range(0, len(y)-n-1): 
# 		if y[i] > y[i+1]: 
# 			y[i+1],y[i] = y[i],y[i+1] 
# 	n+=1
# n=0
# d=[]
# print(y)


############---Made Bubble sort code with one loop----############

# list1=[11,2,3,4,4,786,2,2,122,27]
# i=0
# while (i<len(list1)-1):
# 	if list1[i]>list1[i+1]:
# 		list1[i],list1[i+1]=list1[i+1],list1[i]
# 		i=0
# 	else:
# 		i+=1
# print(list1)