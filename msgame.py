from msdata import gezi
import pygame
pygame.init()
screen=pygame.display.set_mode([288,288])
keep_going=True
pic=pygame.image.load("png/mine.png")
while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
    for x in range(len(gezi)):
        for y in range(len(gezi[x])):
            if gezi[x][y]:
                screen.blit(pic,(y*32,x*32))
    pygame.display.update()
            
   
pygame.quit()


print(gezi)
# print(x)
# print(y)

# r = len(gezi)


