import ParticleClass

import math

class Temp(ParticleClass):
	
	def __init__(position):
		color = (255,255,255,1)
		velocity = (0,0)
		mass = 0
		radius = 0
		ParticleClass.__init__(position, velocity, radius, mass, color)

	def updateRadius(self, mousePosition):
		self.radius = math.sqrt(math.pow((self.position[0] - mousePosition[0]),2) + math.pow((self.position[1] - mousePosition[1]),2))
		self.mass = math.pow(self.radius,4)

	def updateVelocity(self, mousePosition):
		centerToMouse = math.sqrt(math.pow((self.position[0] - mousePosition[0]),2) + math.pow((self.position[1] - mousePosition[1]),2))
		borderToMouse = centerToMouse - self.radius
		constant = borderToMouse/centerToMouse
		self.velocity = (constant * (self.position[0]-mousePosition[0]), constant * (self.position[1]-mousePosition[1]))
		if borderToMouse < 0:
			self.velocity = (0,0)

	def updateActive(self):
		self.active = not self.active
		if self.active:
			color = (0,255,0,1)
		else:
			color = (255,0,0,1)

	def createRealParticle(self):
		randomcolor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),1)
		created = ParticleClass.Particle(self.position, self.velocity, self.radius, self.mass, randomcolor)
		return created

