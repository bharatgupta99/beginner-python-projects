import sys, pygame
pygame.init()

size = width, height = 800, 800
white = 255, 255, 255
clock = pygame.time.Clock();
screen = pygame.display.set_mode(size)
ball = pygame.image.load("intro_ball.png")
x, y = (width - 56) / 2, (height - 56) / 2  
x_change = 0
y_change = 0


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	sys.exit()
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_UP:
        		y_change += -5
        	if event.key == pygame.K_DOWN:
        		y_change += 5
        	if event.key == pygame.K_RIGHT:
        		x_change += 5
        	if event.key == pygame.K_LEFT:
        		x_change += -5
        if event.type == pygame.KEYUP:
        	if event.key == pygame.K_RIGHT:
        		x_change += -5
        	if event.key == pygame.K_LEFT:
        		x_change += 5
        	if event.key == pygame.K_UP:
        		y_change += 5
        	if event.key == pygame.K_DOWN:
        		y_change += -5


    x += x_change
    y += y_change
    print(x_change, end = " ")
    print(y_change)
   
    screen.fill(white)
    screen.blit(ball, (x, y))
    pygame.display.update()
    clock.tick(60)
