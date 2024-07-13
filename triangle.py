import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Draw Rectangle in Pygame')

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
# Set the background color
screen.fill(WHITE)

point1 = (400, 100)  # Top point
point2 = (300, 300)  # Bottom left point
point3 = (500, 300)  # Bottom right point
points = [point1, point2, point3]

# Draw the triangle
# Arguments: surface, color, points
pygame.draw.polygon(screen, GREEN, points)

# applying translation
pygame.draw.polygon(screen, BLUE, [(x + 80, y + 80) for x, y in points])

# rotate triangle in 30 degree
angle = 30
# convert angle to radian
angle_to_radian = angle * 3.14 / 180
# rotate the triangle
rotated_points = []
for x, y in points:
    x1 = x * math.cos(angle_to_radian) - y * math.sin(angle_to_radian)
    y1 = x * math.sin(angle_to_radian) + y * math.cos(angle_to_radian)
    rotated_points.append((x1, y1))

pygame.draw.polygon(screen, RED, rotated_points)

# Update the display
pygame.display.flip()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
