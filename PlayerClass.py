import ParticleClass
import pygame

class Player(ParticleClass.Particle):
	def __init__(self, position, velocity):
		color = (255,255,255,0)
		position = list(position)
		velocity = list(velocity)
		ParticleClass.Particle.__init__(self, position, [0,0], 15, 15, color)
		self.static = False
		self.type = "player"

	def _handleCollision(self, other):
		pass

	def draw(self, screen, offset, zoom):
		i = 1
		for point in self.path:
			i += 1
			pygame.draw.circle(screen, self.color, ((int((point[0]+offset[0]) * zoom),int((point[1]+offset[1])* zoom))), 0, 0)
		pygame.draw(screen, (11,223,0,0), ((int((self.position[0]+offset[0]) * zoom),int((self.position[1]+offset[1])* zoom))), 10, 0)
		pygame.draw(screen, (150,150,150,0), ((int((self.position[0]+offset[0]) * zoom),int((self.position[1]+offset[1])* zoom))), 15, 10)
		self.path.append((self.position[0],self.position[1]))
		self.path = self.path[-5000:] #This deletes any points older than 500

