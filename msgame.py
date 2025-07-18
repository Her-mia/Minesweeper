from msdata import gezi
import pygame
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
while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
    for x in range(len(gezi)):
        for y in range(len(gezi[x])):
            if gezi[x][y]==-1:
                screen.blit(pic,(y*32,x*32))
            if gezi[x][y]==0:
                screen.blit(pic1,(y*32,x*32))
            if gezi[x][y]==1:
                screen.blit(pic2,(y*32,x*32))
            if gezi[x][y]==2:
                screen.blit(pic3,(y*32,x*32))
            if gezi[x][y]==3:
                screen.blit(pic4,(y*32,x*32))
            if gezi[x][y]==4:
                screen.blit(pic5,(y*32,x*32))
            if gezi[x][y]==5:
                screen.blit(pic6,(y*32,x*32))
            if gezi[x][y]==6:
                screen.blit(pic7,(y*32,x*32))
            if gezi[x][y]==7:
                screen.blit(pic8,(y*32,x*32))
            if gezi[x][y]==8:
                screen.blit(pic9,(y*32,x*32))
    pygame.display.update()
            
   
pygame.quit()



# print(x)
# print(y)

# r = len(gezi)


