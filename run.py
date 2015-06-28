import pygame
import time
import particleClass
import random
import numpy
import math
import pickle
from guppy import hpy

width = 1080
height = 720

screen = pygame.display.set_mode((width, height))

ls = [] 

for i in range(40):
	color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
	a = particleClass.Particle(random.randrange(100,980), random.randrange(100,620), random.randrange(3,25),random.randrange(3,25))
	a.active = True
	ls.append(a)

class PathItem:
	def __init__(self,pos,color):
		self.position = numpy.array([pos[0],pos[1]],int)
		self.color = color

paths = []

running = True
size = True
xstart, ystart = 0, 0
sizex, sizey = 0, 0
xoff, yoff = 0, 0
mass = 0
pause = False
creating = False
h = hpy()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				xoff += 100
			elif event.key == pygame.K_d:
				xoff -= 100
			elif event.key == pygame.K_w:
				yoff += 100
			elif event.key == pygame.K_s:
				yoff -= 100
			elif event.key == pygame.K_SPACE:
				pause = not pause
			elif event.key == pygame.K_RETURN:
				name = time.strftime("%H:%M:%S")
				f = open(name,'w')
				pickle.dump(ls,f)
			elif event.key == pygame.K_m:
				print h.heap()

		if creating:
			if event.type == pygame.MOUSEBUTTONDOWN:
				pause = False
				creating = False
				xend, yend = event.pos
				a = particleClass.Particle(xstart-xoff, ystart-yoff, 2*(xstart-xend), 2*(ystart-yend))
				a.mass = mass
				a.active = True
				ls.append(a)
				mass = 0
		elif event.type == pygame.MOUSEBUTTONDOWN:
			size = False
			xstart, ystart = event.pos
			pause = True
			creating = True
			mass = 1
		if event.type == pygame.MOUSEBUTTONUP:
			size = True
			sizex, sizey, = event.pos
			distance = math.sqrt(math.pow(sizex-xstart,2) + math.pow(sizey-ystart,2))
			mass = math.pow(distance,4)

	screen.fill((0,0,0))
	for b in paths:
		pygame.draw.circle(screen, b.color, (int(b.position[0])+xoff,int(b.position[1])+yoff), 0, 0)
	for a in ls:
		pygame.draw.circle(screen, a.color, (int(a.position[0])+xoff,int(a.position[1])+yoff), int(math.sqrt(math.sqrt(a.mass))), 0)
		if not pause:
			b = PathItem((int(a.position[0]),int(a.position[1])), a.color)
			paths.append(b)
	if creating:
		xpos, ypos = pygame.mouse.get_pos()
		if not size:
			radius = int(math.sqrt(math.pow(xstart-xpos,2)+math.pow(ystart-ypos,2)))
			pygame.draw.circle(screen, (254,254,200), (xstart+xoff,ystart+yoff), radius, 0)
		else:
			radius = int(math.sqrt(math.pow(xstart-sizex,2)+math.pow(ystart-sizey,2)))
			pygame.draw.circle(screen, (254,254,200), (xstart+xoff,ystart+yoff), radius, 0)
	pygame.display.flip()
	ls = [x for x in ls if not x.delete]
	if not pause:
		particleClass.update(ls)

pygame.quit()


