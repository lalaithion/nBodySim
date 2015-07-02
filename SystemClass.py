import ParticleClass

import pickle
import time
import pygame

class System:

	def __init__(self, particleList, offset = [0,0], pause = 0, zoom = 1.0, timestep = .01):
		self.particleList = particleList
		self.offset = offset
		self.pause = pause
		self.zoom = zoom
		self.timestep = timestep
		self.size = True

	@classmethod
	def initFromFile(self, fileName):
		dataList = pickle.load(open( fileName, "rb" ))
		offset = dataList[0][0]
		pause = dataList[0][1]
		zoom = dataList[0][2]
		timestep = dataList[0][3]
		particleList = dataList[1]
		return self(particleList, offset, pause, zoom, timestep)

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
		return self(particleList)

	def addParticle(self, particle):
		self.particleList.append(particle)

	def removeParticle(self, particle):
		self.particleList.remove(particle)

	def deleteSystem(self):
		del self.particleList[:]

	def saveSystem(self, fileName):
		dataList = []
		systemList = []
		systemList.append(self.offset)
		systemList.append(self.pause)
		systemList.append(self.zoom)
		systemList.append(self.timestep)
		dataList.append(systemList)
		dataList.append(self.particleList)
		timeString = time.strftime("%H_%M_%S")
		fileName = "savefile_" + timeString
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
