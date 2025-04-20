from game_process import GameProcess
import pygame


class WindowProcessHandler(GameProcess):
    @classmethod
    def tick(cls, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.WINDOWRESTORED:
                ...
            elif event.type == pygame.WINDOWFOCUSLOST:
                ...
            elif event.type == pygame.WINDOWFOCUSGAINED:
                ...
            elif event.type == pygame.WINDOWHIDDEN:
                ...
            elif event.type == pygame.WINDOWSHOWN:
                ...

        return False
