import pygame, sys
from pygame.locals import *
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (225, 225, 225)

ilosc = int(input("ile pol(max,10x10):"))
pygame.init()
if(ilosc<=10):
    DISPLAY_SURFACE = pygame.display.set_mode((ilosc*80,ilosc*60))
    DISPLAY_SURFACE.fill(GRAY)
    for i in range (0,ilosc):
        pygame.draw.line(DISPLAY_SURFACE, BLACK, (0, i*60), (800, i*60), 2) # pozioma
        pygame.draw.line(DISPLAY_SURFACE, BLACK, (i*80, 0), (i*80, 600), 2) # pionowa
    pygame.display.set_caption("PROJEKT DSZI")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
else:
    print("za duzy rozmiar")






