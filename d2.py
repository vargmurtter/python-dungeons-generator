import pygame
import sys
import math
import random as rnd


pygame.init()

screen = pygame.display.set_mode((700, 700))

clock = pygame.time.Clock()
while True:
	clock.tick(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill((255, 255, 255))

	# someday...

	pygame.display.flip()
