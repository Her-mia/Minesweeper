import random
gezi = []
for i in range(9):
    gezi.append([])
    for j in range(9):
       gezi[i].append(False)
d=82
for g in range(10):
    c=random.randint(0,81)
    if c==d:
        c=random.randint(0,81)
    elif c==d:
        c=random.randint(0,81)
    elif c==d:
        c=random.randint(0,81)
    elif c==d:
        c=random.randint(0,81)
    else:
        e=c//9
        if e==9:
            e=e-1
        f=c%9
        gezi[e][f]=True
        d=e
print(gezi)