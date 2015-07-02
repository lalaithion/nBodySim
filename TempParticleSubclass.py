import ParticleClass

import math
import random
import pygame

class Temp(ParticleClass.Particle):
	
	def __init__(self, position, zoom):
		color = (255,255,255,0)
		velocity = [0,0]
		position = list(position)
		position[0] = position[0] / zoom
		position[1] = position[1] / zoom
		mass = 0
		radius = 0
		ParticleClass.Particle.__init__(self, position, velocity, radius, mass, color)

	def updateRadius(self, mousePosition, offset, zoom):
		self.radius = math.sqrt(math.pow((self.position[0] - mousePosition[0]/zoom + offset[0]/zoom),2) + math.pow((self.position[1] - mousePosition[1]/zoom + offset[1]/zoom),2))
		self.mass = math.pow(self.radius,4)

	def updateVelocity(self, mousePosition, offset, zoom):
		centerToMouse = math.sqrt(math.pow((self.position[0] - mousePosition[0]/zoom + offset[0]),2) + math.pow((self.position[1] - mousePosition[1]/zoom + offset[1]),2))
		borderToMouse = centerToMouse - self.radius
		if borderToMouse <= 0:
			self.velocity = (0,0)
			return
		constant = borderToMouse/centerToMouse
		self.velocity = (constant * (self.position[0] - mousePosition[0]/zoom + offset[0]), constant * (self.position[1] - mousePosition[1]/zoom + offset[1]))

	def updateStatic(self):
		self.static = not self.static
		if self.static:
			self.color = (230,20,20,0)
		else:
			self.color = (20,230,20,0)

	def createRealParticle(self):
		randomcolor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),1)
		created = ParticleClass.Particle(self.position, self.velocity, self.radius, self.mass, randomcolor)
		created.static = self.static
		return created
