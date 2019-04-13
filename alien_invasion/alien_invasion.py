import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
	# 初始化游戏，创建屏幕和标题栏
	pygame.init()

	# 这个是总的实例的一个对象，它包含很多属性
	ai_settings = Settings()

	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height)
	)
	pygame.display.set_caption("Alien Invasion")

	# 创建Play按钮
	play_button = Button(ai_settings, screen, "Play")

	# 设置背景色
	bg_color = (230, 230, 230)

	# 创建一艘飞船，一个子弹编组和一个外星人编组
	# 创建一艘飞船，实例化之后有很多属性
	ship = Ship(ai_settings, screen)
	# 创建存储子弹的编组,用的是pygame的类
	bullets = Group()
	aliens = Group()

	# 创建外星人舰队
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

		if stats.game_active:
			ship.update()

			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
	run_game()