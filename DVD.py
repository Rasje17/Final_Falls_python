import sys, pygame, time
from Ball import Ball
from random import randrange
pygame.init()

size = width, height = 800, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball1 = Ball()

ball2 = Ball(speed = [3, 3])
ball2.rect.left = 320
ball2.rect.top = 240

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ball1.rect = ball1.rect.move(ball1.speed)
    ball2.rect = ball2.rect.move(ball2.speed)
    if ball1.rect.left < 0 or ball1.rect.right > width:
        ball1.speed[0] = -ball1.speed[0]
    if ball1.rect.top < 0 or ball1.rect.bottom > height:
        ball1.speed[1] = -ball1.speed[1]
    if ball2.rect.left < 0 or ball2.rect.right > width:
        ball2.speed[0] = -ball2.speed[0]
    if ball2.rect.top < 0 or ball2.rect.bottom > height:
        ball2.speed[1] = -ball2.speed[1]
    if ball1.rect.colliderect(ball2.rect):
        val1 = randrange(101)
        val2 = randrange(101)
        print(val1, ', ', val2)
        #ball1.tint(val1)
        #ball2.tint(val2)
        ball1.image.set_alpha(val1)
        ball2.image.set_alpha(val2)
        ball1.speed = [-ball1.speed[0], -ball1.speed[1]]
        ball2.speed = [-ball2.speed[0], -ball2.speed[1]]

    time.sleep(0.01)
    screen.fill(black)
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    pygame.display.flip()

