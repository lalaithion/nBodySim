import numpy
import math
import random

TIMESTEP = [1, .5, .3, .2, .1, .05, .03, .01, .005]
x = 6

class Particle:
	"""
	This class holds the data needed for creating and simulating a particle,
	or an object in physical space, that is acted on by gravity. Currently, some 
	magic numbers are used to make the gravity more real; this is in essence
	the same as just making the masses bigger.
	"""
	def __init__(self, x, y, s, r): 															#this is called to initialize the particle
		self.position = numpy.array([x,y], float) 													#this holds the position in 2D space; 0,0 is the initial top left corner of the display
		self.velocity = numpy.array([s,r], float) 													#this holds the velocity as a vector
		self.mass = random.lognormvariate(1,6) 														#during initialization, a random mass is chosen; it can be overwritten later
		self.active = True 																			#all particles are active be default; and inactive particle will exert gravitational acceleration but not experience it
		self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)) 		#a random color will be chosen; it can be overwritten later
		self.delete = False 																		#if this is True, then it will be deleted from the list at the next opporitunity
	def addForce(self, other): 																	#this adds acceleration due to gravity to the particle 'self' based on the mass of 'other'
		grav = 6.673*math.pow(10,-1) 																#gravity is 10^10 times more powerful here than in real life; that is the equivalent of scaling the masses by a factor of ten as well.
		radius = numpy.linalg.norm(other.position - self.position) 									#this uses numpy's algorithm to get the position vector from other to self
		if radius < math.sqrt(math.sqrt((self.mass+other.mass))): 									#if one of the particles is within the displayed radius (which is the fourth root of the mass) of the other
			if self.mass > other.mass: 																	#and this is the bigger mass
				#calculate the avergae velocity of the two
				self.velocity[0] = ((other.velocity[0] * other.mass) + (self.velocity[0] * self.mass))/(self.mass+other.mass)
				self.velocity[1] = ((other.velocity[1] * other.mass) + (self.velocity[1] * self.mass))/(self.mass+other.mass)
				self.mass += other.mass 																#add the mass of the smaller one to this mass
				other.delete = True 																	#and delete the other
				return 
			if self.mass < other.mass:																	#if the other one is bigger
				if not other.active:																	#and it's not active
					other.mass += self.mass 															#add the mass of us to this mass
					self.delete = True																	#and delete ourselves
		accel = (other.mass * grav)/(math.pow(radius,2)) * ((other.position-self.position)/radius) 	#using the radius above and newton's law of gravitational acceleration, calculate the acceleration vector
		self.velocity = self.velocity + (accel * TIMESTEP[x]) 											#multiply the acceleration by the time to find delta-v, and add delta-v to the initial velocity.
	def move(self): 																			#This finds the change in position
		self.position = self.position + (self.velocity * TIMESTEP[x])								#multiply the velocity by the time to find change in position, and add this change to the inital position
	def conicmove(self,ls):
		otherranking = 0
		for b in ls:
			if b is not self:
				radius = numpy.linalg.norm(b.position - self.position) 
				branking = b.mass/math.pow(radius,2)
				if branking > otherranking:
					other = b
		#Universal Variable Formulation????



def update(ls): 				#this updates all the particles in ls
	for a in ls: 					#for every paricle in ls
		if a.active: 				#as long as the particle is active
			for b in ls: 			#take every other particle in ls
				if b is not a: 		#except for itself
					a.addForce(b) 	#and add the force from the other particles to it
	for a in ls: 					#after adding the forces
		a.move() 					#move the particles





