import pygame 
from settings import *
from chomsky import Chomsky
from aspirador import Aspirador, create_pair_aspirador
from time import sleep
from score import Score

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = pygame.sprite.Group()
		self.player_group_sprite = pygame.sprite.Group()
		self.elapsed_time = 0

		self.score = Score()
		self.setup()
		self.is_running = False
		self.myFont = pygame.font.Font("SquashyFlow.ttf", 18)

	def setup(self):
		for sprite in self.all_sprites:
			sprite.kill()

		for sprite in self.player_group_sprite:
			sprite.kill()

		self.player = Chomsky((SCREEN_WIDTH//2,SCREEN_HEIGHT - 200), self.player_group_sprite)
		self.score.score = 0

	def update_colision(self):
		if pygame.sprite.spritecollide(self.player, self.all_sprites, False, pygame.sprite.collide_mask):
			print("END GAME")
			self.is_running = False
			for aspiradores in self.all_sprites:
				print(aspiradores.pos.x, aspiradores.pos.y, end=" , ")
				print()
				self.display_surface.blit(aspiradores.mask.to_surface(), aspiradores.pos)


			self.display_surface.blit(self.player.mask.to_surface(), self.player.pos)	
			print(self.player.pos)

	def run(self,dt):

		self.display_surface.fill([95, 205, 228])

		# checa se tem mais de 10 aspiradores. Se tiver, ignora
		# print(len(self.list_aspiradores))
		if int(self.elapsed_time * 1000) % 50 == 0 and self.elapsed_time > 1:
			# print(f"Time: {(self.elapsed_time * 1000)}")
			# print(f"Time int: {int(self.elapsed_time * 1000)}")
			# print(f"Division: {int(self.elapsed_time * 1000) % 1000 }")
			# print(f"Len: {len(self.all_sprites)}")
			create_pair_aspirador(self.all_sprites)
			# for aspiradores in self.all_sprites:
				# print(aspiradores.pos.y, aspiradores.pos.y, end=" , ")
			# print()

			print("="*50)
			print(self.score.score)
			self.elapsed_time = 0			


		self.all_sprites.draw(self.display_surface)
		self.all_sprites.update(dt, self.score)
		self.player_group_sprite.draw(self.display_surface)
		self.player_group_sprite.update(dt)

		score_lable = self.myFont.render(f"Score: {self.score.score}", 1, (0,0,0))
		self.display_surface.blit(score_lable, (SCREEN_WIDTH//2 - 50, 0))

		self.update_colision()
		
		self.elapsed_time += (dt)
			