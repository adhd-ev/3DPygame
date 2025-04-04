#init
import pygame, shape
from math import sin, cos, tan, pi, asin, acos
from drawpoly import *
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
running = True
#endinit

face_colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
]

cube = shape.Cube([0, 0, 150], face_colors)

cube.vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]]
cube.edges = [
    [0, 1],[1, 2],
    [2, 3],[3, 0],
    [4, 5],[5, 6],
    [6, 7],[7, 4],
    [0, 4],[1, 5],
    [2, 6],[3, 7]]
cube.faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 5, 4],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [3, 0, 4, 7]]

vel = 1
TICKS = 0


while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN: print(pygame.key.name(event.key))
    pygame.draw.rect(screen,hex2rgb("000000"),(0,0,1000,1000))
    cube.draw(screen)
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    cube.pos = [
        cube.pos[0]+(keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]) * vel,
        cube.pos[1]+(keys[pygame.K_LSHIFT] - keys[pygame.K_LCTRL]) * vel,
        cube.pos[2]+(keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
    ]
    TICKS+=1
pygame.quit()