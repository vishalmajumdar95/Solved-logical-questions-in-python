def x(h):
	if h in [1,0]:
		return 1
	else:
		return x(h-1)+x(h-2)
print(x(int(input())))

s,j=[],int(input())
for i in range(1,(j//2)+1):
	s.extend([i,13*i,7+(i-1)])
print(s[j-1])

x,c=list(map(int,input().split())),0
for i in x:
	x.pop(0)
	if i in x:
		c+=1
print(c)



x=[15,7,11,2]
y=11
b=0
for i in range(len(x)):			
	if b==1:
		break
	else:
		for u in range(len(x)):
			if i==u:
				continue
			if y==x[i]+x[u]:
				print(i,u)
				b=1



a=input()
a=list(a)
count=0
l=0
while a:
	a.remove(a[l])
	count+=1
print(count)

# ,"span",class_="secondaryInfo","span",class_="secondaryInfo","td",class_="ratingColumn imdbRating","strong",title="9.2 based on 2,320,529 user ratings"
# title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman"

import requests
from bs4 import BeautifulSoup
x="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
v=requests.get(x).text
with open("r.text","w") as h:
	h.write(v)
	h.close()
s=BeautifulSoup(v,"html.parser")
f=s.find('tbody',class_="lister-list").find_all('tr')
# q=f.find_all('tr')
print(f)

