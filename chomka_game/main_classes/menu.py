import pygame 
from settings import *

class Menu:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()
		self.myFont = pygame.font.Font("./assets/fonts/SquashyFlow.ttf", 18)
		self.start_button = self.myFont.render(f"Click here to start", 1, (0,0,0))
		self.start_button_rect = self.start_button.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
		# self.display_surface.blit(self.start_button, )


	def handle_input(self, event_list):
		for event in event_list:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print(self.start_button_rect, pygame.mouse.get_pos())
				return self.update_colision(pygame.mouse.get_pos())
			else:
				return False

	def update_colision(self, pos):
		if self.start_button_rect.collidepoint(pos):
			return True
		
		else:
			return False

	def run(self, event_list, score=0):

		self.display_surface.fill([95, 205, 228])
		if score > 0:
			self.score_text = self.myFont.render(f"Final Score {score}", 1, (0,0,0))
			self.score_text_rect = self.start_button.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100))
			self.display_surface.blit(self.score_text, self.score_text_rect)

		pygame.draw.rect(self.start_button, (0,0,0), self.start_button_rect, 1)
		self.display_surface.blit(self.start_button, self.start_button_rect)

		return self.handle_input(event_list)