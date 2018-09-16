import sys, pygame
pygame.init()

size = width, height = 400, 800
white = 255, 255, 255
clock = pygame.time.Clock();
screen = pygame.display.set_mode(size)
ball = pygame.image.load("flappy.png")
x, y = 60, (height - 56) 
y_change = 0
gravity = 4


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	sys.exit()
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_UP:
        		y_change += -18
       
        if event.type == pygame.KEYUP:
        	if event.key == pygame.K_UP:
        		y_change = 0


    y += y_change
    if y > height - 57:
    	y = height - 56
    elif y < 0:
    	y = 0
    else:
    	y += gravity



    screen.fill(white)
    screen.blit(ball, (x, y))
    pygame.display.update()
    clock.tick(60)
