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
def open(x,y):
    if x<=8 and y<=8 and x>=0 and y>=0:
        zhuangtai[x][y]=1
        print(x,y)
        if gezi[x][y]==0:
            open(x+1,y+1)
            open(x+1,y)
            open(x+1,y-1)
            # open(x,y+1)
            # open(x,y-1)
            # open(x-1,y+1)
            # open(x-1,y)
            # open(x-1,y+1)

while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.MOUSEBUTTONUP:
            spot=event.pos
            x=spot[0]//32
            y=spot[1]//32
            open(x,y)
            pygame.display.update()        
    for x in range(len(gezi)):
        for y in range(len(gezi[x])):
            
            #打开点击格子

            if zhuangtai[y][x]==0:
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