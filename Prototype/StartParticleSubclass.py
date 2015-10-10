import ParticleClass
import LevelClass

import math
import random
import pygame

class Start(ParticleClass.Particle):
	def __init__(self, position, radius):
		color = (230,230,230,0)
		position = list(position)
		ParticleClass.Particle.__init__(self, position, [0,0], radius, 0, color)
		self.static = True
		self.type = "start"

	def updateVelocity(self, ls, timestep):
		pass

	def draw(self, screen, offset, zoom):
		self.delete = False
		pygame.draw.circle(screen, self.color, (int((self.position[0]+offset[0])*zoom),int((self.position[1]+offset[1])*zoom)), int(self.radius*zoom), 0)