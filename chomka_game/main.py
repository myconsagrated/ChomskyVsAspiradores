import pygame, sys
from settings import *
from main_classes.level import Level
from main_classes.menu import Menu

from pygame import mixer

import asyncio

mixer.pre_init(44100, 16, 2, 4096)



class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(window_size)
		pygame.display.set_caption('Chomsky vs aspirador do mal')
		self.clock = pygame.time.Clock()
		self.level = Level()
		self.menu = Menu()
		mixer.init()
		mixer.music.load('./assets/sounds/musica.ogg')
		mixer.music.set_volume(0.2)

	async def run(self):
		mixer.music.play(loops=-1)
		while True:
			event_list = pygame.event.get()
			for event in event_list:
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
			dt = self.clock.tick(60) / 1000
			if self.level.is_running:
				# print(dt)
				self.level.run(dt)
			else:
				self.level.is_running = self.menu.run(event_list, self.level.score.score)
				if self.level.is_running:
					self.level.setup()
			
			pygame.display.update()
			await asyncio.sleep(0)

async def main():
	game = Game()
	await game.run()
	# asyncio.run(game.run())
	

# if __name__ == '__main__':
# 	game = Game()
# 	game.run()


asyncio.run(main())