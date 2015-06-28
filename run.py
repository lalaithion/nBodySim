import pygame
import time
import particleClass
import random
import numpy
import math
import pickle

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

xoff, yoff = 0, 0
mass = 0
pause = False
creating = False

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
				name = string(time.strftime("%H:%M:%S"))
				f = open(name,'w')
				pickle.dump(ls,name)
		if creating:
			if event.type == pygame.MOUSEBUTTONDOWN:
				pause = False
				creating = False
				xend, yend = event.pos
				a = particleClass.Particle(xstart-xoff, ystart-yoff, xstart-xend, ystart-yend)
				print "3 ",
				print mass
				a.active = True
				ls.append(a)
				mass = 0
				print "4 ",
				print mass
				print "done"
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print "new"
			xstart, ystart = event.pos
			pause = True
			creating = True
			mass = 1
		if event.type == pygame.MOUSEBUTTONUP:
			sizex, sizey, = event.pos
			distance = math.sqrt(math.pow(sizex-xstart,2) + math.pow(sizey-ystart,2))
			print "1 ",
			print mass
			mass = math.pow(distance,2)
			print "2 ",
			print mass
	if not pause:
		screen.fill((0,0,0))
		for b in paths:
			pygame.draw.circle(screen, b.color, (int(b.position[0])+xoff,int(b.position[1])+yoff), 0, 0)
		for a in ls:
			pygame.draw.circle(screen, a.color, (int(a.position[0])+xoff,int(a.position[1])+yoff), int(math.sqrt(math.sqrt(a.mass))), 0)
			b = PathItem((int(a.position[0]),int(a.position[1])), a.color)
			paths.append(b)
		ls = [x for x in ls if not x.delete]
		pygame.display.flip()
		particleClass.update(ls)
		
pygame.quit()


