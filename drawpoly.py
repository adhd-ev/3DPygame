import pygame
from convertcol import *
def tri(screen,hex : str,coordsequence : tuple):
    """Draws a triangle based on hex code and coords."""
    col = hex2rgb(hex)
    coordsequence = (
        coordsequence[:2],
        coordsequence[2:4],
        coordsequence[4:6]
    )
    pygame.draw.polygon(screen,col,coordsequence)
