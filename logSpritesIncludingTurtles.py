# Class for log sprites
# Contains the three different sized logs, the two different sized turtles, and the two different sized animated turtles
import arcade
from frogger_config import LANE_SIZE, SCREEN_WIDTH

class Logs(arcade.Sprite): #lowest  logs
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.RESET_VALUE = -1.5 * 146 #Where the logs reset to
        
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed

    def update(self):
        self.left += self.logSpeed
        #This resets the pattern
        #three logs go across the screen and start going off
        #when the second is half of the first reappears
        if self.left >= SCREEN_WIDTH:
            self.right = self.RESET_VALUE


class Logs2(arcade.Sprite): # middle logs
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.RESET_VALUE = -3 * 146  #Where the logs reset to
        
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed

    def update(self):
        self.left += self.logSpeed
        #resets logs for pattern
        if self.left >= SCREEN_WIDTH:
            self.right = self.RESET_VALUE


class Logs3(arcade.Sprite): # highest logs
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.RESET_VALUE = -194  #Where the logs reset to

    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed

    def update(self):
        self.left += self.logSpeed
        #resets logs for pattern
        if self.left >= SCREEN_WIDTH:
            self.right = self.RESET_VALUE


class LowerTurtles(arcade.Sprite): #lowest turtle
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.RESET_VALUE = SCREEN_WIDTH + LANE_SIZE * 8  #Where the logs reset to

    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed

    def update(self):
        self.left += self.logSpeed
        #resets turtles for pattern
        if self.right <= 0:
            self.right = self.RESET_VALUE



class LowerTurtlesAnimated(arcade.Sprite): #lowest turtle
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.texture = arcade.load_texture("assets/Turtles.png") #starts as full turtles
        self.update_counter = 0 #tracks Turtle animation
        self.RESET_VALUE = SCREEN_WIDTH + LANE_SIZE * 8  #Where the logs reset to

    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed

    def update(self):
        self.left += self.logSpeed
        #Loop of turtle Animation
        self.update_counter += 1 #keeps track of the state of the turtles
        turtle_loop_speed = 25  #how fast turtles cycle
        if self.right <= 0:
            self.right = self.RESET_VALUE
        if self.update_counter < turtle_loop_speed:
            self.texture = arcade.load_texture("assets/Turtles.png") #Regular turtles
        elif self.update_counter < turtle_loop_speed * 2:
            self.texture = arcade.load_texture("assets/TurtlesTucking1.png") #turtles start sinking
        elif self.update_counter < turtle_loop_speed * 3:
            self.texture = arcade.load_texture("assets/TurtlesTucking2.png") #turtles sink farther
        elif self.update_counter < turtle_loop_speed * 4:
            self.texture = arcade.load_texture("assets/TurtlesTucking3.png")  #turtles almost gone
        elif self.update_counter == turtle_loop_speed * 4:
            self.visible = False  #Turtles Have gone under
            #self.texture = arcade.load_texture("assets/Water.png")
        elif self.update_counter == turtle_loop_speed * 5:
            self.visible = True  #resets to showing turtle sprites
        elif self.update_counter < turtle_loop_speed * 6:
            self.texture = arcade.load_texture("assets/TurtlesRising.png") #Turtles rising
        if self.update_counter > turtle_loop_speed * 6:
            self.update_counter = 0  #restart turtle loop



class UpperTurtles(arcade.Sprite): #lowest turtle
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.RESET_VALUE = SCREEN_WIDTH + LANE_SIZE * 8  #Where the logs reset to

    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed

    def update(self):
        self.left += self.logSpeed
        #resets turtles for pattern
        if self.right <= 0:
            self.right = self.RESET_VALUE


class UpperTurtlesAnimated(arcade.Sprite): #lowest turtle
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.texture = arcade.load_texture("assets/TwoTurtles.png")
        self.update_counter = 0 #tracks Turtle animation
        self.RESET_VALUE = SCREEN_WIDTH + LANE_SIZE * 8  #Where the logs reset to

    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed

    def update(self):
        self.left += self.logSpeed
        #Loop of turtle Animation
        self.update_counter += 1 #keeps track of the state of the turtles
        turtle_loop_speed = 25  #how fast turtles cycle
        if self.right <= 0:
            self.right = self.RESET_VALUE
        if self.update_counter < turtle_loop_speed:
            self.texture = arcade.load_texture("assets/TwoTurtles.png") #Regular turtles
        elif self.update_counter < turtle_loop_speed * 2:
            self.texture = arcade.load_texture("assets/TwoTurtlesTucking1.png") #turtles start sinking
        elif self.update_counter < turtle_loop_speed * 3:
            self.texture = arcade.load_texture("assets/TwoTurtlesTucking2.png") #turtles sink farther
        elif self.update_counter < turtle_loop_speed *4:
            self.texture = arcade.load_texture("assets/TwoTurtlesTucking3.png")  #turtles almost gone
        elif self.update_counter == turtle_loop_speed * 4:
            self.visible = False  #Turtles Have gone under
            #self.texture = arcade.load_texture("assets/Water.png")
        elif self.update_counter == turtle_loop_speed * 5:
            self.visible = True  #resets to showing turtle sprites
        elif self.update_counter < turtle_loop_speed * 6:
            self.texture = arcade.load_texture("assets/TwoTurtlesRising.png") #Turtles rising
        if self.update_counter > turtle_loop_speed * 6:
            self.update_counter = 0  #restart turtle loop