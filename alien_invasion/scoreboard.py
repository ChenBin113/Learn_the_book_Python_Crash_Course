import pygame.font


class Scoreboard():

	def __init__(self, ai_settings, screen, stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# 显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# 准备初始得分图像和最高分图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()


	def prep_score(self):

		score_str = str(self.stats.score)
		# -1使得圆整到最近的10的整数倍，用Python3可以不用int
		# rounded_score = int(round(self.stats.score, -1))
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)

		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

		# 将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.

	def prep_high_score(self):

		# -1使得圆整到最近的10的整数倍，用Python3可以不用int
		# rounded_score = int(round(self.stats.score, -1))
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)

		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

		# 将最高得分放在屏幕顶部中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		# 将等级放在得分下方
		self.level_rect.top = self.score_rect.bottom + 10