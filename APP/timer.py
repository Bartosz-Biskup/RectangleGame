from game_process import GameProcess


class Timer(GameProcess):
    def __init__(self):
        self.time = 0

    def tick(self, tick):
        self.time += tick
        print(self.time)


class DecreasingTimer(Timer):
    def __init__(self, max_time: float, decrease: float):
        super().__init__()
        self.max_time = max_time
        self.decrease = decrease

    def tick(self, tick):
        self.time += tick

        if self.time > self.max_time:
            self.time = 0
            self.max_time = self.max_time - self.decrease

            return True

        return False
