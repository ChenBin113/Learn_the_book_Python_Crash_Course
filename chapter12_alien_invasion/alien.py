import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""表示单个外星人的类"""

	def __init__(self, ai_settings, screen):
		"""初始化外星人并设置其起始位置"""
		super().__init__()
		self.screen = screen
		# 一个外星人，所以setting后面没有s
		self.ai_setting = ai_settings

		# 加载外星人图像，并设置其rect属性
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()

		# 出现在屏幕左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 存储外星人的准确位置
		self.x = float(self.rect.x)

	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image, self.rect)

	# edge边缘
	def check_edges(self):
		"""如果外星人位于边缘，则返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		"""向左或向右移动外星人"""
		self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
		self.rect.x = self.x
