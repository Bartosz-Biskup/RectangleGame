from game_object import GameObject
from game_process import GameProcess
from size import Size
from point import Point


class ScrollingBackground(GameProcess):
    def __init__(self,
                 focus: GameObject,
                 window_size: Size):
        self.focus = focus
        self.window_size = window_size

    def tick(self, window, fps, *args):
        screen_left_x: int = max(0, self.focus.get_position().x - (self.window_size.width // 2))
        screen_top_y: int = max(0, self.focus.get_position().y - (self.window_size.height // 2))

        # args[0] refers to the list of objects in this case, args[1] to window(surface)
        return Point(screen_left_x, screen_top_y)
