import random
keep_going=True
# 0 表示游戏进行中，1表示游戏成功，2表示游戏失败
game_status = 2
b=0
def makegezi():
    global game_status
    gezi=[]
    gezi1=[]

    #初始化gezi列表
    for i in range(9):
        gezi.append([])
        for j in range(9):
            gezi[i].append(0)
    a=0
    #gezi列表设置雷
    while a<10:
        c=random.randint(0,80)
        e=c//9
        f=c%9
        if not gezi[e][f]:
            gezi[e][f]=-1
            a=a+1
    #算出格子旁边有多少雷
    for i in range(len(gezi)+2):
        gezi1.append([])
        for j in range(len(gezi)+2):
            gezi1[i].append(0)
            if i==0 or i==len(gezi)+1:
                gezi1[i][j]=0
            elif j==0 or j==len(gezi)+2:
                gezi1[i][j]=0
            elif i<10 and j<10:
                gezi1[i][j]=gezi[i-1][j-1]
    for x in range(1,len(gezi)+1):
        for y in range(1,len(gezi)+1):
            lei=0
            if gezi1[x][y]==-1:
                continue
            if gezi1[x-1][y-1]==-1:
                lei+=1
            if gezi1[x-1][y]==-1:
                lei+=1
            if gezi1[x-1][y+1]==-1:
                lei+=1
            if gezi1[x][y-1]==-1:
                lei+=1
            if gezi1[x][y+1]==-1:
                lei+=1
            if gezi1[x+1][y-1]==-1:
                lei+=1
            if gezi1[x+1][y]==-1:
                lei+=1
            if gezi1[x+1][y+1]==-1:
                lei+=1
            gezi[x-1][y-1]=lei 
    game_status=0
    return gezi
def makezhuangtai():
    zhuangtai=[]
    #zhuangtai列表设置
    for i in range(9):
        zhuangtai.append([])
        for j in range(9):
            zhuangtai[i].append(0)
    return zhuangtai
gezi=makegezi()
zhuangtai=makezhuangtai()