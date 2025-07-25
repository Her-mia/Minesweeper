from msdata import gezi
from msdata import zhuangtai
import pygame
a=0
pygame.init()
screen=pygame.display.set_mode([288,288])
keep_going=True
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
def open(x,y):
    if x<=8 and y<=8 and x>=0 and y>=0:
        print(x,y)
        if gezi[x][y] != 0:
            zhuangtai[x][y] = 1
        if gezi[x][y]==0:
            a=0
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

while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.MOUSEBUTTONUP:
            if event.button == 1:
                spot=event.pos
                x=spot[0]//32
                y=spot[1]//32
                open(x,y)
            # if event.button == 3:
            #     screen.blit(pic12,(y*32,x*32))
            pygame.display.update()        
    for x in range(len(gezi)):
        for y in range(len(gezi[x])):
            
            #打开点击格子

            if zhuangtai[y][x]==1:
                if gezi[y][x]==-1:
                    screen.blit(pic11,(y*32,x*32))
                if gezi[y][x]==0:
                    screen.blit(pic1,(y*32,x*32))
                if gezi[y][x]==1:
                    screen.blit(pic2,(y*32,x*32))
                if gezi[y][x]==2:
                    screen.blit(pic3,(y*32,x*32))
                if gezi[y][x]==3:
                    screen.blit(pic4,(y*32,x*32))
                if gezi[y][x]==4:
                    screen.blit(pic5,(y*32,x*32))
                if gezi[y][x]==5:
                    screen.blit(pic6,(y*32,x*32))
                if gezi[y][x]==6:
                    screen.blit(pic7,(y*32,x*32))
                if gezi[y][x]==7:
                    screen.blit(pic8,(y*32,x*32))
                if gezi[y][x]==8:
                    screen.blit(pic9,(y*32,x*32))
            else:
                screen.blit(pic10,(y*32,x*32))
    pygame.display.update()
pygame.quit()