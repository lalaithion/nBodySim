class Levels:
	def __init__(self,filename):
		self.level = 0
		self.levelList = [line.rstrip('\n') for line in open(filename)]
		self.max = len(self.levelList)

	def nextlevel(self):
		if self.level is not self.max:
			self.level += 1
			return self.levelList[self.level]
		else:
			print "you win"
			return 0
