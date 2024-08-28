import pygame as py
import sys
import math
from random import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

BGCOLOR = (0, 0, 0)
CIRCLECOLOR = (255, 255, 255)

# border class
class Border(py.sprite.Sprite):
	def __init__(self, radius, color, x, y, border_width):
		super().__init__()
		self.radius = radius
		self.border_width = border_width
		self.x = x
		self.y = y
		self.image = py.Surface((self.radius * 2, self.radius * 2), py.SRCALPHA)
		py.draw.circle(self.image, color, (self.radius, self.radius), self.radius, self.border_width)
		self.rect = self.image.get_rect(center = (self.x, self.y))
	

# ball class
'''
class Ball:
	def __init__(self, r, color, speed):
		self.r = r
		self.color = color
		self.speed = speed
		self.reset()

	# draws the Ball object
	def draw(self):
		py.draw.circle(DISPLAYSURF, self.color, (self.x, self.y), self.r)

	def reset(self):
		self.speedx = choice(range(self.speed // 2, self.speed))
		self.speedy = choice(range(self.speed // 2, self.speed))

		if random() > 0.5:
			self.speedx *= -1
		if random()	>	0.5:
			self.speedy *= -1
		self.x = SCREEN_WIDTH // 2
		self.y = SCREEN_HEIGHT // 2
'''

class Ball(py.sprite.Sprite):
	def __init__(self, circleColor, radius, width, x, y, speed):
		py.__init__(self)
		self.x = x
		self.y = y
		self.radius = radius
		self.speedx = float(speed)
		self.speedy = float(speed)
		self.image = py.Surface((self.radius * 2, self.radius * 2), py.SRCALPHA)
		
	def update(self):
		self.rect.move_ip(self.spped, self.speed)


py.init()
DISPLAYSURF = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("circle in circle")
clock = py.time.Clock()
FPS = 60
border1 = Border(175, CIRCLECOLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 5)







while True:
	DISPLAYSURF.fill(BGCOLOR)

	border1.update()
	border1.draw(DISPLAYSURF)
	balls.draw(DISPLAYSURF)
	balls.update()
	


	#ball.x += ball.speedx
	#ball.y += ball.speedy
	
	distance_to_center = math.sqrt((ball.x - SCREEN_HEIGHT // 2) ** 2 + (ball.y - SCREEN_HEIGHT // 2) ** 2)
	
	border1.draw()

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			sys.exit()

	py.display.update()
	clock.tick(FPS)