import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = float(self.rect.centerx)

		self.moving_right = False
		self.moving_left = False

	# self.moving_up = False
	# self.moving_down = False

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		# 更新飞船的center值，而不是rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		# if self.moving_up:
		# 	self.rect.centery -= 1
		# if self.moving_down:
		# 	self.rect.centery += 1

		self.rect.centerx = self.center

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		# 通过和屏幕的中心x坐标赋值，确定飞船的坐标
		self.center = self.screen_rect.centerx
