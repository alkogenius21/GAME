import pygame
import colorspy as color
import random


class Particle:
	def __init__(self, x, y, direction=[1, 1], size=5, pType='circle', gravity=0, colors=[color.white], speed=0.15):
		self.x = x
		self.y = y
		self.x_vel = direction[0]
		self.y_vel = direction[1]
		self.size = random.randint(size-1, size+1)
		self.gravity = gravity
		self.color = random.choice(colors)
		self.type = pType
		self.speed = speed

	def render(self, win):
		self.x += self.x_vel
		self.y += self.y_vel
		self.size -= self.speed
		self.y_vel += self.gravity

		if self.type == 'circle':
			pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), int(self.size))
		elif self.type == 'square':
			pygame.draw.rect(win, self.color, pygame.Rect(int(self.x), int(self.y), int(self.size), int(self.size)))

		if self.size <= 0:
			del self
