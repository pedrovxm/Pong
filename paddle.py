import pygame

Black =(0,0,0)
class Paddle(pygame.sprite.Sprite):

	def __init__(self,color,width,height):

		super().__init__() # (Sprite) Constructor

		self.image = pygame.Surface ([width,height])
		self.image.fill(Black)
		self.image.set_colorkey(Black)

		pygame.draw.rect(self.image,color,[0,0,width,height])
		self.rect=self.image.get_rect()

	def moveUp(self,pixels):
		self.rect.y-=pixels
		if self.rect.y <0:
			self.rect.y =0

	def moveDown(self,pixels):
		self.rect.y +=pixels
		if self.rect.y > 600-110:
			self.rect.y = 600-110

