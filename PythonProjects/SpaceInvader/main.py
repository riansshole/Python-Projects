import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images

RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.bmp"))

GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.bmp"))

BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.bmp"))

# PLAYER SHIP
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.bmp"))

# Lasers
RED_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_red.bmp"))
GREEN_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_green.bmp"))
BLUE_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_blue.bmp"))
YELLOW_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.bmp"))

# Background
BG = pygame.image.load(os.path.join("assets", "background-black.bmp"))
