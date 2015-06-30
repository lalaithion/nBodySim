import ParticleClass
import pickle
import time

class System:
	def __init__(self, particleList):
		self.particleList = particleList

	@classmethod
	def initFromFile(self, fileName):
		#file handling
		return self(particleList)

	#generate random system
	@classmethod
	def initRandom(self, maxParticles, maxSize):
		if(maxParticles>50):
			maxParticles = 50
		for i in range(maxParticles):
			newParticle = ParticleClass.initRandomParticle()
			self.particleList.append(newParticle)
		return self(particleList)

	def addParticle(self, particle):
		self.particleList.append(particle)

	def removeParticle(self, particle):
		self.particleList.remove(particle)

	def deleteSystem(self):
		del self.particleList[:]

	def saveSystem(self, fileName):
		name = time.strftime("%H:%M:%S")		#Procedural filenames, later.
		saveFile = open(fileName,'w')
		total = [ls,paths]
		pickle.dump(total,f)