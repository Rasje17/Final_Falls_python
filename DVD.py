import sys, pygame, time, Ball
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball1 = Ball
ball2 = Ball

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    ball1.rect = ball1.rect.move(ball1.speed)
    if ball1.rect.left < 0 or ball1.rect.right > width:
        ball1.speed[0] = -ball1.speed[0]
    if ball1.rect.top < 0 or ball1.rect.bottom > height:
        ball1.speed[1] = -ball1.speed[1]

    time.sleep(0.01)
    screen.fill(black)
    screen.blit(ball1, ball1.rect)
    pygame.display.flip()

