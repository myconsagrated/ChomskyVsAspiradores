import pygame
from utils import load_image_list_from_sprite_sheet

class Chomsky(pygame.sprite.Sprite):
    
    def __init__(self, pos, group):
        super().__init__(group)

        self.image_list = load_image_list_from_sprite_sheet("./assets/images/Cat2.png", frames=8)
        self.image = pygame.Surface.copy(self.image_list[0])
        self.current_image_frame = 0


        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 3.5
        
        self.rect = self.image.get_rect()
        # self.rect.topleft = (0, 0)

        self.speed = 400

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(pos[0], pos[1])


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            # print(self.pos)
            # print("left")

        elif keys[pygame.K_RIGHT]:
            # print("right")
            self.direction.x = 1

        else:
            self.direction.x = 0


    def move(self, dt):

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def animate(self, dt):
        self.current_image_frame += 4 * dt
        if self.current_image_frame >= 8:
            self.current_image_frame = 0

        self.image = self.image_list[int(self.current_image_frame)]
        self.image = pygame.transform.smoothscale_by(self.image, self.scale)

        if self.direction.x < 0:
            # print("left")
            self.image = pygame.transform.flip(self.image, True, False)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)