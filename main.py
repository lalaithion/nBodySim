import SystemClass
import ParticleClass
import TempParticleSubclass as temp

import pygame
import math
import sys
from guppy import hpy
import argparse

width = 1080
height = 720
screen = pygame.display.set_mode((width, height))

memoryTrackerObject = hpy()

mainSystem = SystemClass.System.initRandom(30,30)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key   == pygame.K_a:
				mainSystem.offset[0] += 100
			elif event.key == pygame.K_d:
				mainSystem.offset[0] -= 100
			elif event.key == pygame.K_w:
				mainSystem.offset[1] += 100
			elif event.key == pygame.K_s:
				mainSystem.offset[1] -= 100
			elif event.key == pygame.K_z:
				print memoryTrackerObject.heap()
			elif event.key == pygame.K_RETURN:
				mainSystem.saveSystem("savefile")
			elif event.key == pygame.K_c: #clear screen
				del mainSystem.particleList[:]
			elif event.key == pygame.K_x: #clear paths
				for particle in mainSystem.particleList:
					del particle.path[:]
			elif event.key == pygame.K_SPACE:
				if mainSystem.pause   == 1:
					mainSystem.pause = 0
				elif mainSystem.pause == 0:
					mainSystem.pause = 1
			elif event.key == pygame.K_MINUS:
				if mainSystem.timestep > 0.00125:
					mainSystem.timestep = mainSystem.timestep/2
			elif event.key == pygame.K_EQUALS:
				if mainSystem.timestep<0.08:
					mainSystem.timestep = mainSystem.timestep*2
			elif event.key == pygame.K_0:
				mainSystem.timestep = .01
				
			elif event.key == pygame.K_LEFTBRACKET:
				mainSystem.offset[0] = mainSystem.offset[0]/2
				mainSystem.offset[1] = mainSystem.offset[1]/2
				mainSystem.zoom = mainSystem.zoom/2
			elif event.key == pygame.K_RIGHTBRACKET:
				mainSystem.offset[0] = mainSystem.offset[0]*2
				mainSystem.offset[1] = mainSystem.offset[1]*2
				mainSystem.zoom = mainSystem.zoom*2
			elif event.key == pygame.K_p:
				mainSystem.offset = [0,0]
				mainSystem.zoom = 1.0


		if mainSystem.pause == 2:
			if event.type == pygame.MOUSEBUTTONDOWN:
				mainSystem.pause = 0
				creating.updateVelocity(event.pos, mainSystem.offset)
				newParticle = creating.createRealParticle()
				mainSystem.addParticle(newParticle)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					creating.updateStatic()
				if event.key == pygame.K_SPACE:
					mainSystem.pause = 0
					newParticle = creating.createRealParticle()
					mainSystem.addParticle(newParticle)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mainSystem.size = False
			creating = temp.Temp((event.pos[0] - mainSystem.offset[0], event.pos[1] - mainSystem.offset[1]), mainSystem.zoom)
			creating.updateStatic()
			creating.updateStatic()
			mainSystem.pause = 2
		if event.type == pygame.MOUSEBUTTONUP:
			mainSystem.size = True

	screen.fill((0,0,0))
	
	for particle in mainSystem.particleList:
		particle.draw(screen, mainSystem.offset, mainSystem.zoom)
	if mainSystem.pause == 2:
		if not mainSystem.size:
			creating.updateRadius(pygame.mouse.get_pos(), mainSystem.offset)
		creating.draw(screen, mainSystem.offset, mainSystem.zoom)

	pygame.display.flip()

	if mainSystem.pause == 0:
		for particle in mainSystem.particleList:
			if not particle.static:
				particle.updateVelocity(mainSystem.particleList, mainSystem.timestep)
			if particle.delete:
				mainSystem.removeParticle(particle)

		for particle in mainSystem.particleList:
			if not particle.static:
				particle.updatePosition(mainSystem.timestep)

pygame.quit()

