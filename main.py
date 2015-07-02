import LevelClass
import SystemClass
import ParticleClass
import BlackHoleClass
import PlayerClass
import TempParticleSubclass as temp


import pygame
import math
import sys
from guppy import hpy
import argparse
import random

width = 1080
height = 720
backGroundColor = (57,52,61)
screen = pygame.display.set_mode((width, height))

#mainSystem = SystemClass.System([],0,0)
#mainSystem = SystemClass.System.initRandom(30,30)
#mainSystem = SystemClass.System.initFromFile("19:37:23")
parser = argparse.ArgumentParser()
parser.add_argument("-r", type=int)
parser.add_argument("-f")
options = parser.parse_args()

memoryTrackerObject = hpy()

if options.f == None and options.r == None:
	mainSystem = SystemClass.System.initRandom(30, 30)
elif options.f == None:
	mainSystem = SystemClass.System.initRandom(int(options.r), 30)
else:
	mainSystem = SystemClass.System.initFromFile(options.f)

Focus = False
running = True
gamemode = 0
start = False
FocusNum = 0

while running:
	if gamemode == 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key   == pygame.K_a:			#Move Screen left
					mainSystem.offset[0] += 108
				elif event.key == pygame.K_d:			#Move Screen right
					mainSystem.offset[0] -= 100
				elif event.key == pygame.K_w:	
					mainSystem.offset[1] += 100			#Move Screen up
				elif event.key == pygame.K_s:
					mainSystem.offset[1] -= 100 		#Move Screen down
				elif event.key == pygame.K_z:			#Print Memory
					print memoryTrackerObject.heap()
				elif event.key == pygame.K_RETURN:		#Save Current system
					mainSystem.saveSystem("savefile")
				elif event.key == pygame.K_c: 			#Clear screen
					del mainSystem.particleList[:]
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
					mainSystem.zoom = mainSystem.zoom/2
				elif event.key == pygame.K_RIGHTBRACKET:#Zoom in
					mainSystem.zoom = mainSystem.zoom*2
				elif event.key == pygame.K_p:			#reset offset and zoom
					mainSystem.offset = [0,0]
					mainSystem.zoom = 1.0
				elif event.key == pygame.K_1:
					gamemode = 1
				elif event.key == pygame.K_COMMA:
					Focus = True
					FocusNum += 1
				elif event.key == pygame.K_PERIOD:
					Focus = True
					FocusNum -= 1
				elif event.key == pygame.K_SLASH:
					Focus = False

			if mainSystem.pause == 2:					#handle new particle creation
				if event.type == pygame.MOUSEBUTTONDOWN:
					mainSystem.pause = 0
					creating.updateVelocity(event.pos, mainSystem.offset, mainSystem.zoom)
					newParticle = creating.createRealParticle()
					mainSystem.addParticle(newParticle)
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						creating.updateStatic()
					if event.key == pygame.K_e:
						creating.updateGoal()
					if event.key == pygame.K_r:
						creating.updateStart()
					if event.key == pygame.K_SPACE:
						mainSystem.pause = 0
						newParticle = creating.createRealParticle()
						mainSystem.addParticle(newParticle)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mainSystem.size = False
				creating = temp.Temp((event.pos[0] - mainSystem.offset[0], event.pos[1] - mainSystem.offset[1]), mainSystem.zoom)
				creating.updateColor()
				mainSystem.pause = 2

			if event.type == pygame.MOUSEBUTTONUP:
				mainSystem.size = True

	if len(mainSystem.particleList) == 0:
		Focus = False
	elif FocusNum < 0:
		FocusNum = len(mainSystem.particleList) - 1
	elif FocusNum >= len(mainSystem.particleList):
		FocusNum = 0


	if gamemode == 1:
		if event.type == pygame.MOUSEBUTTONDOWN:
			start = True
			"""
			for particle in mainSystem.particleList:
				if particle.type == "start":
					position = pygame.mouse.get_pos()
					radius = math.sqrt((position[0] - particle.position[0])**2 + (position[1] - particle.position[1])**2)
					if radius < particle.radius:
						start = True
			"""
						

		elif event.type == pygame.MOUSEBUTTONUP:
			if start:
				end = pygame.mouse.get_pos()
				dx = end[0]-position[0]
				dy = end[1]-position[1]
				player = PlayerClass(position, [dx,dy])
				mainSystem.particleList.append(player)
	
	if Focus == True:
		mainSystem.offset[0] = - mainSystem.particleList[FocusNum].position[0] + width/2
		mainSystem.offset[1] = - mainSystem.particleList[FocusNum].position[1] + height/2	

	screen.fill((0,0,0))
	for particle in mainSystem.particleList:
		particle.draw(screen, mainSystem.offset, mainSystem.zoom)
	if mainSystem.pause == 2:

		if not mainSystem.size:
			creating.updateRadius(pygame.mouse.get_pos(), mainSystem.offset, mainSystem.zoom)
		creating.draw(screen, mainSystem.offset, mainSystem.zoom)

	mainSystem.update(screen)

	pygame.display.flip()
	screen.fill(backGroundColor)
	
pygame.quit()
