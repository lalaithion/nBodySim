import numpy
import math
import random

TIMESTEP = .01

class Particle:
	def __init__(self, x, y, s, r):
		self.position = numpy.array([x,y], float)
		self.velocity = numpy.array([s,r], float)
		self.mass = random.lognormvariate(1,6)
		self.active = True
		self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
		self.delete = False
	def addForce(self, other):
		grav = 6.673*math.pow(10,-1)
		radius = numpy.linalg.norm(other.position - self.position)
		if radius < math.sqrt(math.sqrt((self.mass+other.mass))):
			if self.mass > other.mass:
				self.mass += other.mass
				other.delete = True
		accel = (other.mass * grav)/(math.pow(radius,2)) * ((other.position-self.position)/radius)
		self.velocity = self.velocity + (accel * TIMESTEP)
	def move(self):
		self.position = self.position + (self.velocity * TIMESTEP)

def update(ls):
	for a in ls:
		if a.active:
			for b in ls:
				if b is not a:
					a.addForce(b)
	for a in ls:
		a.move()





