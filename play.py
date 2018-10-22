import pygame
pygame.init()
pygame.font.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
flag = font.render('Kuwait', True, (255,255,255))
flagrect = flag.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: import sys; sys.exit()

    flagrect = flagrect.move(speed)
    if flagrect.left < 0 or flagrect.right > width:
        speed[0] = -speed[0]
    if flagrect.top < 0 or flagrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(flag, flagrect)
    pygame.display.flip()
