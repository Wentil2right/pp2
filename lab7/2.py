import pygame

#initialise
pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False