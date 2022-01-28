import pygame

pygame.init()

screen = pygame.display.set_mode((1920,1080))

button = pygame.image.load('button.png')
wscreen = pygame.image.load('whitescreen.png')
titlescreenimg = pygame.image.load('titlescreen.png')
pygame.display.set_caption("osu knockoff")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

tsX=200
tsY=-100
sfade = 255
startseq = False

screen.fill((0,0,0))
keys = pygame.key.get_pressed()
running = True

while running:
    screen.fill((0,0,0))
    screen.blit(titlescreenimg,(tsX,tsY))

    if not (tsY == 200) and startseq == False:
        tsY += 2

    if tsY == 200:
        screen.fill((255,100,100))
        screen.blit(titlescreenimg,(tsX,tsY))
        screen.blit(button,(680,tsY+500))
        screen.blit(wscreen,(0,0))
        wscreen.set_alpha(sfade)
        if not (sfade == 0): 
            sfade -= 3

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False
    