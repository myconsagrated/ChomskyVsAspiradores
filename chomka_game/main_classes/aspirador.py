import pygame
from settings import *
from utils import sine
import random
from main_classes.score import Score

class Aspirador(pygame.sprite.Sprite):
    
    def __init__(self, pos, group, amplitude, flip=False, verbose=False):
        """
        Cria o par de aspiradores, na mesma ideia de par de tubos do flappy bird
        O par tera posição e velocidade iguais no eixo Y
        No eixo X eles estarão em em lugares iguais mas com movimentos com amplitudes distintas
        """
        super().__init__(group)
        self.verbose = verbose

        # init imagem
        self.image = pygame.image.load("./assets/images/aspiradorv1.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.scale = 1.5
        self.image = pygame.transform.smoothscale_by(self.image, self.scale)


        # movement info
        self.speed = 150
        self.amplitude = amplitude + random.randint(0, 100)
        self.direction = pygame.math.Vector2(0, 1)
        self.pos = pygame.math.Vector2(pos[0], pos[1])
        self.initial_x = pos[0]

        if flip:
            self.image = pygame.transform.flip(self.image, True, False)

        self.mask = pygame.mask.from_surface(self.image)


    def move(self, dt):
        self.pos.y += self.speed * dt
        self.pos.x = sine(100.0, 620, self.amplitude, self.initial_x)

        if self.verbose:
            print(self.pos)
        self.rect.center = self.pos

    def die(self, score: Score):
        if self.rect.top > SCREEN_HEIGHT:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            self.kill()
            score.update_score()

    def update(self, dt, score: Score):
        self.move(dt)
        self.die(score)


def create_pair_aspirador(group) -> list[Aspirador, Aspirador]:
    Aspirador(
		(0,0), 
        group,
        20
	)

    Aspirador(
		(SCREEN_WIDTH,0), 
        group,
        20,
        flip=True
	)