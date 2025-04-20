import pygame

from point import Point


class StaticTextBox:
    def __init__(self,
                 position: Point,
                 color: tuple[int, int, int],
                 font_size: int):
        self.font = pygame.font.SysFont("Arial",font_size)
        self.position = position
        self.color = color

    def draw(self, window: pygame.Surface, text: str):
        window.blit(self.font.render(text, True, self.color), (self.position.x, self.position.y))
