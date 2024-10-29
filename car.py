# Class for car sprites
import arcade
from frogger_config import LANE_SIZE, SCREEN_WIDTH


class Car(arcade.Sprite):
    def __init__(self, filename, car_speed=5, direction=1):
        super().__init__(filename)
        self.scale = LANE_SIZE / self.height
        self.car_speed = car_speed
        self.direction = direction

    def update(self):
        self.center_x += self.car_speed * self.direction
        if self.left > SCREEN_WIDTH or self.right < 0:
            if self.direction > 0:
                self.right = 0
            else:
                self.left = SCREEN_WIDTH