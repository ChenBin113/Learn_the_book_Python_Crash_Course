class Settings(object):
	"""
	存储相关设置
	"""

	def __init__(self):
		"""初始化游戏的静态设置"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		self.ship_speed_factor = 1.5
		self.ship_limit = 3

		# 子弹设置
		self.bullet_speed_factor = 3

		# 可以制作大炸弹
		self.bullet_width = 10

		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 3

		# 外星人设置，平移速度和下降速度
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction为1表示右移，-1表示左移
		self.fleet_direction = 1

		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1

		self.score_scale = 1.5

		# 初始化动态设置
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction为1表示向右，-1表示向左
		self.fleet_direction = 1

		# 计分
		self.alien_points = 50

	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
	# print(self.alien_points)
