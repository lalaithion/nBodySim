import ParticleClass

import pickle
import time
import pygame
class System:

	def __init__(self, particleList, center, radius):
		self.particleList = particleList
		self.center = center
		self.radius = radius
		self.offset = [0,0]
		self.size = False
		self.pause = 0
		self.zoom = 1.0
		self.timestep = 0.00125

	@classmethod
	def initFromFile(self, fileName):
		particleList = pickle.load(open( fileName, "rb" ) )
		return self(particleList,0,0)
	#generate random system
	@classmethod
	def initRandom(self, maxParticles, maxSize):
		particleList = []
		radius = 1000
		center = (0,0)
		if(maxParticles>50):
			maxParticles = 50
		for i in range(maxParticles):
			newParticle = ParticleClass.Particle.initRandomParticle(radius,maxSize,center)
			particleList.append(newParticle)
		return self(particleList, center, radius)

	def addParticle(self, particle):
		self.particleList.append(particle)

	def removeParticle(self, particle):
		self.particleList.remove(particle)

	def deleteSystem(self):
		del self.particleList[:]

	def saveSystem(self, fileName):
		fileName = time.strftime("%H:%M:%S")		#Procedural filenames, later.
		saveFile = open(fileName,'w')
		pickle.dump(self.particleList,saveFile)

	def update(self,screen):
		if not self.pause:
			for particle in self.particleList:	#update all particle velocitys
				particle.updateVelocity(self.particleList, self.timestep)
				if particle.delete:
					self.removeParticle(particle)
			for particle in self.particleList:  #update all particle positions
				particle.updatePosition(self.timestep)

		for particle in self.particleList:
			particle.draw(screen, self.offset, self.zoom)