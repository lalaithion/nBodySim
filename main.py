import SystemClass
import ParticleClass
import BlackHoleClass
import TempParticleSubclass as temp


import pygame
import math
import sys
from guppy import hpy
import argparse

width = 1080
height = 720
backGroundColor = (57,52,61)
screen = pygame.display.set_mode((width, height))

memoryTrackerObject = hpy()

mainSystem = SystemClass.System.initRandom(30,30)
#mainSystem = SystemClass.System.initFromFile("19:37:23")
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key   == pygame.K_a:			#Move Screen left
				mainSystem.offset[0] += (150 / mainSystem.zoom)
			elif event.key == pygame.K_d:			#Move Screen right
				mainSystem.offset[0] -= (150 / mainSystem.zoom)
			elif event.key == pygame.K_w:			#Move Screen up
				mainSystem.offset[1] += (150 / mainSystem.zoom)		
			elif event.key == pygame.K_s:			#Move Screen down
				mainSystem.offset[1] -= (150 / mainSystem.zoom)
			elif event.key == pygame.K_z:			#Print Memory
				print memoryTrackerObject.heap()
			elif event.key == pygame.K_RETURN:		#Save Current system
				print "Game Saved"
				mainSystem.saveSystem("savefile")
			elif event.key == pygame.K_c: 			#Clear screen
				del mainSystem.particleList[:]
				x = BlackHoleClass.Blackhole((0,0),(0,0),10)
				mainSystem.addParticle(x)
			elif event.key == pygame.K_x: 			#Clear paths
				for particle in mainSystem.particleList:
					del particle.path[:]
			elif event.key == pygame.K_SPACE:		#Pause Simulation
				if mainSystem.pause   == 1:
					mainSystem.pause = 0
				elif mainSystem.pause == 0:
					mainSystem.pause = 1
			elif event.key == pygame.K_MINUS:		#Decrease timestep, slow down
				if mainSystem.timestep > 0.00125:
					mainSystem.timestep = mainSystem.timestep/2
			elif event.key == pygame.K_EQUALS:
				if mainSystem.timestep<0.08:		#Increase timestep, speed up
					mainSystem.timestep = mainSystem.timestep*2
			elif event.key == pygame.K_0:
				mainSystem.timestep = .01
			elif event.key == pygame.K_LEFTBRACKET:	#Zoom out
				if mainSystem.zoom >0.25:
					mainSystem.zoom = mainSystem.zoom/2
			elif event.key == pygame.K_RIGHTBRACKET:#Zoom in
				if mainSystem.zoom < 4:
					mainSystem.zoom = mainSystem.zoom*2
			elif event.key == pygame.K_p:			#reset offset and zoom
				mainSystem.offset = [0,0]
				mainSystem.zoom = 1.0
			elif event.key == pygame.K_q:
					creating.updateStatic()

		elif event.type == pygame.MOUSEBUTTONDOWN and not mainSystem.pause == 2:
			print "mouse down"
			creating = temp.Temp((event.pos[0] - mainSystem.offset[0], event.pos[1] - mainSystem.offset[1]), mainSystem.zoom)
			mainSystem.pause = 2

		if mainSystem.pause == 2:
			if event.type == pygame.MOUSEBUTTONDOWN and mainSystem.size:
				print "mouse down 2"
				mainSystem.pause = 0
				mainSystem.size = False
				creating.updateVelocity(event.pos, mainSystem.offset, mainSystem.zoom)
				newParticle = creating.createRealParticle()
				mainSystem.addParticle(newParticle)
			elif event.type == pygame.MOUSEBUTTONUP:
				print 'mouse up'
				mainSystem.size = True
				if not creating.static:
					creating.color = (0,255,0,0)

	if mainSystem.pause == 2:				   #check for drawing new object
		if not mainSystem.size:
			creating.updateRadius(pygame.mouse.get_pos(), mainSystem.offset, mainSystem.zoom)
		creating.draw(screen, mainSystem.offset, mainSystem.zoom)

	mainSystem.update(screen)
	pygame.display.flip()
	screen.fill(backGroundColor)




pygame.quit()
