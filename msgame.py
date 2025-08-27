from msdata import gezi
from msdata import zhuangtai
from msdata import game_status
from msdata import makegezi
from msdata import makezhuangtai
import tkinter as tk
from tkinter import messagebox
import pygame
leishu=10
leishu2=10
pygame.init()
screen=pygame.display.set_mode([288,360])
screen.fill((200,200,200))
root = tk.Tk()
root.withdraw()
keep_going=True

starttime=pygame.time.get_ticks()
time=0
time2=0
s=0
pic=pygame.image.load("png/mine.png")
pic1=pygame.image.load("png/empty.png")
pic2=pygame.image.load("png/grid1.png")
pic3=pygame.image.load("png/grid2.png")
pic4=pygame.image.load("png/grid3.png")
pic5=pygame.image.load("png/grid4.png")
pic6=pygame.image.load("png/grid5.png")
pic7=pygame.image.load("png/grid6.png")
pic8=pygame.image.load("png/grid7.png")
pic9=pygame.image.load("png/grid8.png")
pic10=pygame.image.load("png/grid.png")
pic11=pygame.image.load("png/mineClicked.png")
pic12=pygame.image.load("png/flag.png")
pic13=pygame.image.load("png/smiley.png")
pic14=pygame.image.load("png/sad.png")
a=72
def open(x,y):
    if x<=8 and y<=8 and x>=0 and y>=0:
        if gezi[x][y] != 0:
            zhuangtai[x][y] = 1
        if gezi[x][y]==0:
            chuli=[]
            chuli.append((x,y))
            while len(chuli)>0:
                weizhi=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,-1]]
                c=chuli.pop(0)
                zhuangtai[c[0]][c[1]]=1
                for i in weizhi:
                    if c[0]+i[0]<=8 and c[0]+i[0]>=0 and c[1]+i[1]<=8 and c[1]+i[1]>=0 and (c[0]+i[0], c[1]+i[1]) not in chuli and zhuangtai[c[0]+i[0]][c[1]+i[1]]!=1:
                        if gezi[c[0]+i[0]][c[1]+i[1]]==0:
                            chuli.append((c[0]+i[0],c[1]+i[1]))
                        else:
                            zhuangtai[c[0]+i[0]][c[1]+i[1]]=1

def drawHead():
    global time
    global game_status
    global s
    leishu1=str(leishu)
    font=pygame.font.SysFont(None,48)
    text1=font.render(leishu1,True,(255,0,0))
    screen.blit(text1,(0,0))
    if game_status!=2:
        screen.blit(pic13,(110,0))
    else:
        screen.blit(pic14,(110,0))
    kaishishijian=pygame.time.get_ticks()//1000-time2
    if kaishishijian>time and game_status==0:
        rect = pygame.Rect(s,0,64,64)
        screen.fill((200,200,200), rect)
        pygame.display.update(rect)
        time=kaishishijian
        time3=time
        a=1
        d=0
        if time3!=0:
            while time3!=0:
                z=time3%(a*10)
                time3=(time3-z)//10
                d=d+1
                a=a*10
        else:
            d=1
        s=288-d*30
        time1=str(time)
        font1=pygame.font.SysFont(None,48)
        text2=font1.render(time1,True,(255,0,0))
        screen.blit(text2,(s,0))


def drawshuzi():
    rect = pygame.Rect(0,0,48,48)
    screen.fill((200,200,200), rect)
    pygame.display.update(rect)


def drawGame():
    global game_status
    for x in range(len(gezi)):
        for y in range(len(gezi[x])):
            #打开点击格子
            if zhuangtai[y][x]==1:
                if gezi[y][x]==-1:
                    screen.blit(pic11,(y*32,x*32+a))
                    game_status=2
                    messagebox.showinfo("提示", "您失败了")
                if gezi[y][x]==0:
                    screen.blit(pic1,(y*32,x*32+a))
                if gezi[y][x]==1:
                    screen.blit(pic2,(y*32,x*32+a))
                if gezi[y][x]==2:
                    screen.blit(pic3,(y*32,x*32+a))
                if gezi[y][x]==3:
                    screen.blit(pic4,(y*32,x*32+a))
                if gezi[y][x]==4:
                    screen.blit(pic5,(y*32,x*32+a))
                if gezi[y][x]==5:
                    screen.blit(pic6,(y*32,x*32+a))
                if gezi[y][x]==6:
                    screen.blit(pic7,(y*32,x*32+a))
                if gezi[y][x]==7:
                    screen.blit(pic8,(y*32,x*32+a))
                if gezi[y][x]==8:
                    screen.blit(pic9,(y*32,x*32+a))
            elif zhuangtai[y][x]!=1 and zhuangtai[y][x]!=2:
                screen.blit(pic10,(y*32,x*32+a))
            elif zhuangtai[y][x]!=1:
                screen.blit(pic12,(y*32,x*32+a))



while keep_going:
    if game_status!=0:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN or event.type==pygame.QUIT:
                if event.type==pygame.QUIT:
                    keep_going=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    spot=event.pos
                    if (110+64)>=spot[0] and spot[0]>=110 and 64>=spot[1] and spot[1]>=0:
                        time2=time+time2
                        gezi=makegezi()
                        zhuangtai=makezhuangtai()
                        game_status=0
                        time=0
                        leishu=10
                        leishu2=10
                        rect = pygame.Rect(0,0,48,48)
                        screen.fill((200,200,200), rect)
                        pygame.display.update(rect)

    while keep_going and game_status==0:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                keep_going=False
            if event.type==pygame.MOUSEBUTTONUP:
                if event.button == 1 :
                    spot=event.pos
                    x=spot[0]//32
                    y=spot[1]//32-a//32
                    open(x,y)
                if event.button == 3 and leishu!=-1:
                    spot=event.pos
                    x=spot[0]//32
                    y=spot[1]//32-a//32
                    zhuangtai[x][y]=2 
                    leishu-=1

        drawGame()
        drawHead()
        if leishu==leishu2-1:
            drawshuzi()
            leishu2-=1
        h=0
        for i in range(len(gezi)):
            for j in range(len(gezi)):
                jieguo=zhuangtai[i][j]!=0 and zhuangtai[i][j]!=2
                if gezi[i][j]!=-1 and jieguo:
                    h=h+1
        if h==(81-10):
            messagebox.showinfo("提示", "您赢了")
            game_status=1
        pygame.display.update()
pygame.quit()