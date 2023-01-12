import numpy as np
import pygame
import sys


BG_COLOR = (102, 204 ,153)
WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
ball_color = (48, 28 ,53)
LINE_COLOR = (66, 66, 66)


# setting up pygame window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ulams Spiral')
screen.fill(BG_COLOR)


def ulam_Spiral():
    size = 61 #size of the array(row and col)
    max_num = size*size
    array = np.zeros((size, size))
    pos = np.array([size, size]) // 2
    step = 1
    num = 2

    for i in range(size*size):

        for j in range(i):
            if num == max_num:
                break
            # replacing the 0 in the array with num 
            array[pos[1], pos[0]] = num 
            start = (pos[0]*((WIDTH//2)//(size//2)))
            num += 1
            pos[0] -= step 
            x = (pos[0]*((WIDTH//2)//(size//2)))   # X position
            y = (pos[1]*((WIDTH//2)//(size//2))) # Y position
            pygame.draw.line(screen, LINE_COLOR, (start,y),(x,y),5)
            if is_prime(num):
                pygame.draw.circle(screen, ball_color,(start, y),(5),5 )
            
            
        for j in range(i):
            if num == max_num:
                break
            # replacing the 0 in the array with num
            array[pos[1], pos[0]] = num
            end = (pos[1]*((WIDTH//2)//(size//2))) # Y position
            num += 1
            pos[1] += step
            x = (pos[0]*((WIDTH//2)//(size//2)))   # X position
            y = (pos[1]*((WIDTH//2)//(size//2))) # Y position
            pygame.draw.line(screen, LINE_COLOR,(x,end),(x,y),5)
            if is_prime(num):
                pygame.draw.circle(screen, ball_color,(x, end),(5),5 )
            
        step *= -1
def is_prime(num):
    if num < 2 or num % 2 == 0:
        return False
    if num == 2:
        return True
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ulam_Spiral()
    
    pygame.display.update()