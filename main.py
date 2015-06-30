import SystemClass
import ParticleClass
import TempParticleSubclass as temp

import pygame
import math
import sys
from guppy import hpy

width = 1080
height = 720

screen = pygame.display.set_mode((width, height))

memoryTrackerObject = hpy()

offset = [0,0]
running = True
size = True
pause = 0 	#0 when not paused, 1 when paused, 2 when creating


mainSystem = SystemClass.System.initRandom(30,30)
#mainSystem = SystemClass.System.initFromFile("14:27:03")
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key   == pygame.K_a:
				offset[0] += 100
			elif event.key == pygame.K_d:
				offset[0] -= 100
			elif event.key == pygame.K_w:
				offset[1] += 100
			elif event.key == pygame.K_s:
				offset[1] -= 100
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
				if pause   == 1:
					pause = 0
				elif pause == 0:
					pause = 1
			elif event.key == pygame.K_MINUS:
				if ParticleClass.timestep > 0.00125:
					ParticleClass.timestep = ParticleClass.timestep/2
			elif event.key == pygame.K_EQUALS:
				if ParticleClass.timestep<0.08:
					ParticleClass.timestep = ParticleClass.timestep*2
			elif event.key == pygame.K_0:
				ParticleClass.timestep = .01

		if pause == 2:
			if event.type == pygame.MOUSEBUTTONDOWN:
				pause = 0
				creating.updateVelocity(event.pos, offset)
				newParticle = creating.createRealParticle()
				mainSystem.addParticle(newParticle)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					creating.updateStatic()
				if event.key == pygame.K_SPACE:
					pause = 0
					newParticle = creating.createRealParticle()
					mainSystem.addParticle(newParticle)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			size = False
			creating = temp.Temp((event.pos[0] - offset[0], event.pos[1] - offset[1]))
			creating.updateStatic()
			creating.updateStatic()
			pause = 2
		if event.type == pygame.MOUSEBUTTONUP:
			size = True

	screen.fill((0,0,0))
	
	for particle in mainSystem.particleList:
		particle.draw(screen, offset)
	if pause == 2:
		if not size:
			creating.updateRadius(pygame.mouse.get_pos(), offset)
		creating.draw(screen, offset)

	pygame.display.flip()

	if pause == 0:
		for particle in mainSystem.particleList:
			if not particle.static:
				particle.updateVelocity(mainSystem.particleList)
			if particle.delete:
				mainSystem.removeParticle(particle)

		for particle in mainSystem.particleList:
			if not particle.static:
				particle.updatePosition()

pygame.quit()

