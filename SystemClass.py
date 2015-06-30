import ParticleClass

import pickle
import time
class System:
	def __init__(self, particleList):
		self.particleList = particleList

	@classmethod
	def initFromFile(self, fileName):
		particleList = pickle.load(open( fileName, "rb" ) )
		return self(particleList)

	#generate random system
	@classmethod
	def initRandom(self, maxParticles, maxSize):
		particleList = []
		if(maxParticles>50):
			maxParticles = 50
		for i in range(maxParticles):
			newParticle = ParticleClass.Particle.initRandomParticle(1000,maxSize,(0,0))
			particleList.append(newParticle)
		return self(particleList)

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