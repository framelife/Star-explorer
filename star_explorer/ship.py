import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('images/2dfly.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.bottom - 20
		self.rect.bottom = self.screen_rect.bottom
		#self.rect.top = self.screen_rect.top
		self.center = float(self.rect.centerx)
		self.center_1 = float(self.rect.centery)
		self.moving_right = False
		self.moving_left = False 
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top> self.screen_rect.top:
			self.center_1 -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_1 += self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center 
		self.rect.centery = self.center_1
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	def center_ship(self):
		self.center = self.screen_rect.centerx
		self.center_1 = self.screen_rect.bottom - 20