import numpy as np
import pygame
import sys

WIDTH = 800
HEIGHT = 800

# setting up pygame window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ulams Spiral')

def ulam_Spiral():
    size = 201 #size of the array(row and col)
    max_num = size*size
    array = np.zeros((size, size))
    pos = np.array([size, size]) // 2
    step = -1
    num = 1

    for i in range(1,size*size):

        for j in range(i):
            if num == max_num:
                break
            # replacing the 0 in the array with num 
            array[pos[1], pos[0]] = num 
            
            if is_prime(num):
                start = (pos[1]*((WIDTH//2)//(size//2))) # X position
                end = (pos[0]*((WIDTH//2)//(size//2)))   # Y position
                # drawing the rectangle 
                rectangle = pygame.Rect(start, end, 5,5)
                pygame.draw.rect(screen, (255,255,255), rectangle)
            
            num += 1
            pos[0] -= step 
        
        for j in range(i):
            if num == max_num:
                break
            # replacing the 0 in the array with num
            array[pos[1], pos[0]] = num
            
            if is_prime(num):
                start = (pos[1]*((WIDTH//2)//(size//2)))# X position
                end = (pos[0]*((WIDTH//2)//(size//2)))  # X position
                # drawing the rectangle 
                rectangle = pygame.Rect(start, end, 5,5)
                pygame.draw.rect(screen, (255,255,255), rectangle)
            num += 1
            pos[1] += step
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
