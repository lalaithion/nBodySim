import numpy
import math
import random
import pygame

timestep = .03 #THIS NEEDS TO BE FIXED

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
		grav = 6.673*math.pow(10,-1) 																	#gravity is 10^10 times more powerful here than in real life; that is the equivalent of scaling the masses by a factor of ten as well.
		radius = math.sqrt(math.pow((other.position[0] - self.position[0]),2) + math.pow((other.position[1] - self.position[1]),2))								#this uses numpy's algorithm to get the position vector from other to self
		self._handleCollision(other)
		accel[0] = (other.mass * grav)/(math.pow(radius,2)) * ((other.position[0]-self.position[0])/radius) 		#using the radius above and newton's law of gravitational acceleration, calculate the acceleration vector
		accel[1] = (other.mass * grav)/(math.pow(radius,2)) * ((other.position[1]-self.position[1])/radius)
		self.velocity[0] = self.velocity[0] + (accel[0] * timestep) 	
		self.velocity[1] = self.velocity[1] + (accel[1] * timestep) 	
	def _handleCollision(self, other):
		radius = numpy.linalg.norm(other.position - self.position) 										#this uses numpy's algorithm to get the position vector from other to self
		if radius < math.sqrt(math.sqrt((self.mass+other.mass))): 										#if one of the particles is within the displayed radius (which is the fourth root of the mass) of the other
	
	def updatePosition(self):
		self.position[0] = self.position[0] + (self.velocity[0] * timestep) 	
		self.position[1] = self.position[1] + (self.velocity[1] * timestep) 									#multiply the velocity by the time to find change in position, and add this change to the inital position

	def updateVelocity(self, ls):
		for particle in ls:
			if self is not particle:
				self.calculateAccelerationFrom(particle)

	def draw(self, screen, offset):
		for point in self.path:
			pygame.draw.circle(screen, self.color, ((int(point[0]+offset[0]),int(point[1])+offset[1])), 0, 0)
		pygame.draw.circle(screen, self.color, (int(self.position[0]+offset[0]),int(self.position[1]+offset[1])), self.radius, 0)
		path.append((self.position[0],self.position[]))
