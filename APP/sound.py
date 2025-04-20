import pygame.mixer


def play_sound(file_path: str):
    sound = pygame.mixer.Sound(file_path)
    pygame.mixer.Sound.play(sound, maxtime=1000)