from dataclasses import dataclass


@dataclass
class Physical:
    velocity: float
    max_velocity: float
    acceleration: float


NO_MOVEMENT_ITEM: Physical = Physical(0, 0, 0)
