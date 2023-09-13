import pygame, sys
from settings import *
from level import Level
from menu import Menu

from pygame import mixer
class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(window_size)
		pygame.display.set_caption('Chomsky vs aspirador do mal')
		self.clock = pygame.time.Clock()
		self.level = Level()
		self.menu = Menu()
		mixer.init()
		mixer.music.load('musica.mp3')
		mixer.music.set_volume(0.2)

	def run(self):
		mixer.music.play(loops=-1)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
			dt = self.clock.tick(60) / 1000
			if self.level.is_running:
				# print(dt)
				self.level.run(dt)
			else:
				self.level.is_running = self.menu.run(self.level.score.score)
				if self.level.is_running:
					self.level.setup()

			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()
