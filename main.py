import SystemClass

import pygame
import sys
from guppy import hpy

width = 1080
height = 720

screen = pygame.display.set_mode((width, height))

memoryTrackerObject = hpy()

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
				if not creating:
					pause = not pause
			elif event.key == pygame.K_RETURN:
				name = time.strftime("%H:%M:%S")
				f = open(name,'w')
				total = [ls,paths]
				pickle.dump(total,f)
			elif event.key == pygame.K_z:
				print len(paths)
				print h.heap()
			elif event.key == pygame.K_c: #clear screen
				del ls[:]
				del paths[:]
			elif event.key == pygame.K_x: #clear paths
				print len(paths)
				del paths[:]
			elif event.key == pygame.K_MINUS:
				particleClass.x += 1
				if particleClass.x > 8:
					particleClass.x =8
			elif event.key == pygame.K_EQUALS:
				particleClass.x -= 1
				if particleClass.x < 0:
					particleClass.x = 0

		if creating:
			if event.type == pygame.MOUSEBUTTONDOWN:
				pause = False
				creating = False
				xend, yend = event.pos
				h1 = math.sqrt(math.pow(xstart-xend,2)+math.pow(ystart-yend,2))
				h2 = h1 - math.sqrt(math.sqrt(mass))
				constant = h2/h1
				x2 = constant * (xstart-xend)
				y2 = constant * (ystart-yend)
				if h2 < 0:
					x2, y2 = 0,0
				a = particleClass.Particle(xstart-xoff, ystart-yoff, x2,y2)
				a.mass = mass
				a.active = creatingactive
				ls.append(a)
				mass = 0
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					creatingactive = not creatingactive
				if event.key == pygame.K_SPACE:
					pause = False
					creating = False
					a = particleClass.Particle(xstart-xoff, ystart-yoff, 0, 0)
					a.mass = mass
					a.active = creatingactive
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
		if creatingactive:
			color = (30,240,30)
		else:
			color = (240,30,30)
		if not size:
			radius = int(math.sqrt(math.pow(xstart-xpos,2)+math.pow(ystart-ypos,2)))
			pygame.draw.circle(screen, color, (xstart,ystart), radius, 0)
		else:
			radius = int(math.sqrt(math.pow(xstart-sizex,2)+math.pow(ystart-sizey,2)))
			pygame.draw.circle(screen, color, (xstart,ystart), radius, 0)
		

	pygame.display.flip()
	ls = [x for x in ls if not x.delete]
	if not pause:
		particleClass.update(ls)

pygame.quit()

