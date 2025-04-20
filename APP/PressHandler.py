from asyncio import Event

import pygame
from game_process import GameProcess


class KeyPressHandler(GameProcess):
    def __init__(self):
        self.pressed_keys = set()

    def tick(self, events: list[pygame.event.Event]) -> tuple:
        self.pressed_keys = set()
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.pressed_keys.add(event.key)

        return tuple(self.pressed_keys)

    def __getitem__(self, item) -> bool:
        return item in self.pressed_keys


