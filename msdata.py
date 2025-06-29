import random
gezi=[]
b=0
for i in range(9):
    gezi.append([])
    for j in range(9):
       gezi[i].append(0)
a=0
while a<10:
    c=random.randint(0,80)
    e=c//9
    f=c%9
    if not gezi[e][f]:
        gezi[e][f]=-1
        a=a+1
print(gezi) 
