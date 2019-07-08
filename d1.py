import pygame
import sys
import math
import random as rnd

def choose_direction(current_x, current_y):
	direction = rnd.choice([0,1,2,3])
	if direction == 0:
		current_x += 1
	elif direction == 1:
		current_x -= 1
	elif direction == 2:
		current_y += 1
	elif direction == 3:
		current_y -= 1

	return current_x, current_y

pygame.init()

screen = pygame.display.set_mode((640, 640))

rect_size = 20

grid = [[1 for x in range(32)] for y in range(32)]

current_x = round(len(grid)/2)
current_y = round(len(grid[0])/2)

grid[current_x][current_y] = 0

x = 0
while x < len(grid)-1:
	y = 0
	while y < len(grid[x]):
		myrnd = rnd.choice([0,1,2])
		if myrnd == 1 or myrnd == 2:
			current_x, current_y = choose_direction(current_x, current_y)

			limit = 0
			while current_x > len(grid[x])-1 or current_y > len(grid)-1:
				current_x, current_y = choose_direction(current_x, current_y)
				if limit > 10:
					break
				limit += 1

			if limit > 10:
				continue

			grid[int(math.fabs(current_x))][int(math.fabs(current_y))] = 0
		y += 1
	x += 1


clock = pygame.time.Clock()
while True:
	clock.tick(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill((0, 0, 0))


	cell_x, cell_y = 0, 0
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] == 1:
				pygame.draw.rect(screen, (0,0,0), (cell_x, cell_y, rect_size, rect_size))
			elif grid[x][y] == 0:
				pygame.draw.rect(screen, (255,255,255), (cell_x, cell_y, rect_size, rect_size))
			cell_x += rect_size
		cell_y += rect_size
		cell_x = rect_size

		player = pygame.draw.rect(
			screen,
			(255, 0, 0),
			((len(grid)/2)*rect_size, (len(grid[0])/2)*rect_size, 10, 10)
		)

	pygame.display.flip()
