import numpy
import math
import random
import pygame
import pygame.gfxdraw

class Particle:

	def __init__(self,position,velocity,radius,mass,color,pType = "Basic"):
		self.position = list(position)					  #list [x,y]
		self.velocity = list(velocity)					  #list [x,y]
		self.mass     = mass						  #int positive
		self.radius   = radius 						  #positive int
		self.color    = color						  #fuple (r,g,b,a)
		self.static   = False						  #false moves, true does not move
		self.delete   = False 						  
		self.path     = []							  #array of points (x,y)
		self.type     = pType						  #designates particle type

	@classmethod
	def initRandomParticle(self, systemRadius, maxSize, systemCenter):
		position = [random.randrange(systemCenter[0],systemRadius),random.randrange(systemCenter[1],systemRadius)]  #this creates a square system
		velocity = [random.randrange(-50,50),random.randrange(-50,50)]					  	  
		mass     = random.lognormvariate(1,6)
		radius   = math.pow(mass,0.25) 
		color    = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),0)
		return self(position,velocity,radius,mass,color)

	def updateVelocity(self, ls, timestep):
		for particle in ls:
			if particle.static:
				particle.velocity =[0,0]
			if self is not particle:
				self._calculateAccelerationFrom(particle, timestep)

	def _calculateAccelerationFrom(self, other, timestep): 														#this adds acceleration due to gravity to the particle 'self' based on the mass of 'other'
		grav = 6.673*math.pow(10,-1) 																	#gravity is 10^10 times more powerful here than in real life; that is the equivalent of scaling the masses by a factor of ten as well.
		radius = math.sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)								#this uses numpy's algorithm to get the position vector from other to self
		#print self.type
		self._handleCollision(other)
		accel = [0,0]
		try:
			accel[0] = (other.mass * grav)/(math.pow(radius,2)) * ((other.position[0]-self.position[0])/radius) 		#using the radius above and newton's law of gravitational acceleration, calculate the acceleration vector
			accel[1] = (other.mass * grav)/(math.pow(radius,2)) * ((other.position[1]-self.position[1])/radius)
		except ZeroDivisionError:
			accel[0] = 0
			accel[1] = 0

		self.velocity[0] = (self.velocity[0] + (accel[0] * timestep) )	
		self.velocity[1] = (self.velocity[1] + (accel[1] * timestep) )	

	def _handleCollision(self, other):
		distance = self._distanceToParticle(other)
		if distance <= self.radius + other.radius and not other.static: # if static allow the other particles handle method to control
			self.velocity[0] = ((self.mass * self.velocity[0]) + (other.mass * other.velocity[0])) / (self.mass + other.mass)
			self.velocity[1] = ((self.mass * self.velocity[1]) + (other.mass * other.velocity[1])) / (self.mass + other.mass)
			if self.mass > other.mass:
				other.delete = True
				self.mass += other.mass


	def _distanceToParticle(self, other): #These need to account for zoom
		distance = math.sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)
		return distance
	def _distanceBetweenPoints(self, a1, a2):
		distance = math.sqrt((a1[0] - a2[0])**2 + (a1[1] - a2[1])**2)
		return distance

	def updatePosition(self, timestep):
		self.position[0] = self.position[0] + (self.velocity[0] * timestep)	#zoomOffset scales velocity to zoom level
		self.position[1] = self.position[1] + (self.velocity[1] * timestep)								#multiply the velocity by the time to find change in position, and add this change to the inital position

	def draw(self, screen, offset, zoom):
		for point in self.path:
			pygame.draw.circle(screen, self.color, ((int((point[0]+offset[0]) * zoom),int((point[1]+offset[1])* zoom))), 0, 0)
		pygame.draw.circle(screen, self.color, (int((self.position[0]+offset[0])*zoom),int((self.position[1]+offset[1])*zoom)), int(self.radius*zoom), 0)
		self.path.append((self.position[0],self.position[1]))
		self.path = self.path[-1500:] #This deletes any points older than 500
	def __str__(self):
		return "Type: %s | Radius: %s" % (self.type, str(self.radius))
