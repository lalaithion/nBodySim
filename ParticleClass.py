import numpy
import math
import random

class Particle:

	def __init__(self,position,velocity,radius,mass,color):
		self.position = position					  #tuple (x,y)
		self.velocity = velocity					  #tuple (x,y)
		self.mass     = mass						  #int positive
		self.radius   = radius 						  #positive int
		self.color    = color						  #fuple (r,g,b,a)
		self.static   = False						  #false moves, true does not move
		self.delete   = False 						  
		self.path     = []							  #array of points (x,y)

	@classmethod
	def initRandomParticle(self, systemRadius, maxSize, systemCenter):
		position = (random.randrange(systemCenter[0],systemRadius),random.randrange(systemCenter[1],systemRadius))  #this creates a square system
		velocity = (random.randrange(-50,50),random.randrange(-50,50))					  	  
		mass     = random.lognormvariate(1,6)
		radius   = math.pow(self.mass,0.25) 
		color    = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),1)
		self(position,velocity,radius,mass,color)

	def _calculateAccelerationFrom(self, other): 														#this adds acceleration due to gravity to the particle 'self' based on the mass of 'other'
		grav = 6.673*math.pow(10,-11) 																	#gravity is 10^10 times more powerful here than in real life; that is the equivalent of scaling the masses by a factor of ten as well.
		radius = numpy.linalg.norm(other.position - self.position) 										#this uses numpy's algorithm to get the position vector from other to self
		self._handleCollision(other)
		accel = (other.mass * grav)/(math.pow(radius,2)) * ((other.position-self.position)/radius) 		#using the radius above and newton's law of gravitational acceleration, calculate the acceleration vector
		self.velocity = self.velocity + (accel * TIMESTEP[x]) 		
	
	def _handleCollision(self, other):
		radius = numpy.linalg.norm(other.position - self.position) 										#this uses numpy's algorithm to get the position vector from other to self
		if radius < math.sqrt(math.sqrt((self.mass+other.mass))): 										#if one of the particles is within the displayed radius (which is the fourth root of the mass) of the other

	def updatePosition(self):
		self.position = self.position + (self.velocity * TIMESTEP[x])									#multiply the velocity by the time to find change in position, and add this change to the inital position
	
	def updateVelocity(self, ls):
		for particle in ls:
			if self is not particle:
				self.calculateAccelerationFrom(particle)