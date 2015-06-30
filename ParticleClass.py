import numpy
import math
import random
import pygame
import pygame.gfxdraw

timestep = .01 #THIS NEEDS TO BE FIXED

class Particle:

	def __init__(self,position,velocity,radius,mass,color):
		self.position = list(position)					  #list [x,y]
		self.velocity = list(velocity)					  #list [x,y]
		self.mass     = mass						  #int positive
		self.radius   = radius 						  #positive int
		self.color    = color						  #fuple (r,g,b,a)
		self.static   = False						  #false moves, true does not move
		self.delete   = False 						  
		self.path     = []							  #array of points (x,y)
	@classmethod
	def initRandomParticle(self, systemRadius, maxSize, systemCenter):
		position = [random.randrange(systemCenter[0],systemRadius),random.randrange(systemCenter[1],systemRadius)]  #this creates a square system
		velocity = [random.randrange(-50,50),random.randrange(-50,50)]					  	  
		mass     = random.lognormvariate(1,6)
		radius   = math.pow(mass,0.25) 
		color    = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),0)
		return self(position,velocity,radius,mass,color)

	def _calculateAccelerationFrom(self, other): 														#this adds acceleration due to gravity to the particle 'self' based on the mass of 'other'
		grav = 6.673*math.pow(10,-1) 																	#gravity is 10^10 times more powerful here than in real life; that is the equivalent of scaling the masses by a factor of ten as well.
		radius = math.sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)								#this uses numpy's algorithm to get the position vector from other to self
		self._handleCollision(other)
		accel = [0,0]
		accel[0] = (other.mass * grav)/(math.pow(radius,2)) * ((other.position[0]-self.position[0])/radius) 		#using the radius above and newton's law of gravitational acceleration, calculate the acceleration vector
		accel[1] = (other.mass * grav)/(math.pow(radius,2)) * ((other.position[1]-self.position[1])/radius)
		self.velocity[0] = self.velocity[0] + (accel[0] * timestep) 	
		self.velocity[1] = self.velocity[1] + (accel[1] * timestep) 	

	def _handleCollision(self, other):
		distance = math.sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)
		if distance <= self.radius and self.mass > other.mass and not other.static:
			self.velocity[0] = ((self.mass * self.velocity[0]) + (other.mass * other.velocity[0])) / (self.mass + other.mass)
			self.velocity[1] = ((self.mass * self.velocity[1]) + (other.mass * other.velocity[1])) / (self.mass + other.mass)
			self.mass += other.mass
			other.delete = True
		elif not other.static or (self.mass < other.mass and not self.static):
			if distance <= other.radius:
				other.velocity[0] = ((self.mass * self.velocity[0]) + (other.mass * other.velocity[0])) / (self.mass + other.mass)
				other.velocity[1] = ((self.mass * self.velocity[1]) + (other.mass * other.velocity[1])) / (self.mass + other.mass)
				other.mass += self.mass
				self.delete = True

	def updatePosition(self):
		self.position[0] = self.position[0] + (self.velocity[0] * timestep) 	
		self.position[1] = self.position[1] + (self.velocity[1] * timestep) 									#multiply the velocity by the time to find change in position, and add this change to the inital position

	def updateVelocity(self, ls):
		for particle in ls:
			if self is not particle:
				self._calculateAccelerationFrom(particle)

	def draw(self, screen, offset):
		i = 1
		for point in self.path:
			i += 1
			pygame.draw.circle(screen, self.color, ((int(point[0]+offset[0]),int(point[1])+offset[1])), 0, 0)
		#pygame.draw.circle(screen, self.color, (int(self.position[0]+offset[0]),int(self.position[1]+offset[1])), int(self.radius), 0)
		pygame.gfxdraw.filled_circle(screen, int(self.position[0]+offset[0]),int(self.position[1]+offset[1]), int(self.radius), self.color)
		self.path.append((self.position[0],self.position[1]))
		self.path = self.path[-5000:] #This deletes any points older than 500
