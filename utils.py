import pygame
import math

def load_image_list_from_sprite_sheet(filename: str, frames=1) -> list:
    image_list = []
    spritesheet = pygame.image.load(filename).convert_alpha()


    original_width = spritesheet.get_width() // frames
    original_height = spritesheet.get_height()

    # iterate over spritesheet
    x = 0
    for frame in range(frames):
        frame_surface = pygame.Surface((original_width, original_height), pygame.SRCALPHA, 32)
        frame_surface.blit(spritesheet, (x, 0))
        image_list.append(frame_surface.copy())
        x -= original_width

    return image_list


def transformScaleKeepRatio(image, scale):
    iwidth, iheight = image.get_size()
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size) 
    return scaled_image

def sine(speed: float, time: int, amplitude: float, overall_y: int) -> int:
    t = pygame.time.get_ticks() / 2 % time
    y = math.sin(t / speed) * amplitude + overall_y
    return int(y)
    