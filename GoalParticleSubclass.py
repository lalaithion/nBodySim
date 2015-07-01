import ParticleClass
import LevelClass

import math
import random
import pygame

class Goal(ParticleClass.Particle):
	def __init__(self, position, radius):
		color = (255,255,255,0)
		position = list(position)
		ParticleClass.Particle.__init__(self, position, [0,0], radius, 0, color)
		self.static = True
		self.type = "goal"

	def updateVelocity(self, ls, timestep):
		for particle in ls:
			if particle.type is "player":
				self._handleCollision(particle)

	def _handleCollision(self, other):
		distance = math.sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)
		if distance < self.radius:
			print "You win"

	def draw(self, screen, offset, zoom):
		self.delete = False
		if int(self.radius*zoom) < 10:
			border = 0
		else: border = 10
		pygame.draw.circle(screen, self.color, (int((self.position[0]+offset[0])*zoom),int((self.position[1]+offset[1])*zoom)), int(self.radius*zoom), border)