import ParticleClass

import pygame
import random
import WormHoleClass

class Blackhole(ParticleClass.Particle):
	def __init__(self,position, position2=[],velocity=[0,0],mass=10000000):
		self.position = list(position)				  #list [x,y]
		self.position2 = []
		self.velocity = list(velocity)				  #list [x,y]
		self.mass     = mass						  #int positive
		self.radius   = 5	 						  #positive __init__
		self.color    = (0,0,0,0)					  #fuple (r,g,b,a)
		self.static   = False						  #false moves, true does not move
		self.delete   = False 						  
		self.path     = []							  #array of points (x,y)
		self.type     = "Blackhole"
		ParticleClass.Particle.__init__(self, self.position, self.velocity, self.radius, self.mass, self.color, self.type)
	@classmethod
	def initNewWormhole(self, position1, position2, mass = 10):
		return self(position1, position2, mass)

	def _handleCollision(self,other):
		if self._distanceToParticle(other) <= self.radius+other.radius:
			if self.type == "Wormhole":
				print "teleport"
				if self._distanceBetweenPoints(self.position, other.position) < (self.radius + other.radius):
					other.position = self.position2
					print self.position2
			else:
				if(self.type == "Blackhole" and other.type == "Blackhole"):
					other.velocity = [0,0]
					self.convertToWormhole()
					if not self.delete:
						other.delete = True
				else:
					self.velocity[0] = ((self.mass * self.velocity[0]) + (other.mass * other.velocity[0])) / (self.mass + other.mass)
					self.velocity[1] = ((self.mass * self.velocity[1]) + (other.mass * other.velocity[1])) / (self.mass + other.mass)
					if not self.delete:
						other.delete = True
					self.mass += other.mass
	
	def convertToWormhole(self):
		self.position2 = [0,0]
		self.position2[0] = random.randrange(int(self.position[0]), 600)
		self.position2[1] = random.randrange(int(self.position[1]), 600)
		self.mass = 1
		self.radius = 10
		self.color = (0,25,23,0)
		self.velocity = [0,0]
		self.static = True
		self.type = "Wormhole"
		del self.path[:] 

	def draw(self, screen, offset, zoom):
		if self.position2:
			pygame.draw.circle(screen, (255,255,255,0.5), (int((self.position2[0]+offset[0])*zoom),int((self.position2[1]+offset[1])*zoom)), int(self.radius*zoom), 0)
		ParticleClass.Particle.draw(self,screen,offset,zoom)

	def __str__(self):
		if self.type == "Wormhole":
			return "Type: %s | Radius: %s | It links to: %s" % (self.type, str(self.radius), str(self.position2))
		else:
			return "Type: %s | Radius: %s" % (self.type, str(self.radius))