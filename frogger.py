#TODO: clean up some of the numbers to have names
import arcade
from car import Car
from frogger_config import MOVEMENT_DISTANCE, LANE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Draw the menu """
        self.clear()
        arcade.draw_text("Press S to start", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ Use a key press to advance to the 'game' view. """
        if key == arcade.key.S:  # Detect "S" key press to start the game
            frogger_game = FroggerGame()
            frogger_game.setup()
            self.window.show_view(frogger_game)


class UserFrog(arcade.Sprite):
    def update(self):
        """ Ensure the player stays within bounds. """
        if self.left < 5:
            self.left = 5
        elif self.right > SCREEN_WIDTH - 5:
            self.right = SCREEN_WIDTH - 5

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 145.5:
            self.top = SCREEN_HEIGHT - 145.5


'''class Logs1(arcade.Sprite):  # lowest logs row, similar to Logs2
    def __init__(self, filename=None, scale=1, image_x=0, image_y=0, image_width=0, image_height=0, center_x=0, center_y=0,
                 repeat_count_x=1, repeat_count_y=1, flipped_horizontally=False, flipped_vertically=False,
                 flipped_diagonally=False, hit_box_algorithm="Simple", hit_box_detail=4.5, texture=None, angle=0, logSpeed=4):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x,
                         repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm,
                         hit_box_detail, texture, angle)
        self.logSpeed = logSpeed

    def update(self):
        self.left += self.logSpeed
        if self.left >= 679:
            self.right = -3 * 146  # Reset similar to Logs2'''

class Logs(arcade.Sprite): #lowest  logs
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        
    #I don't think I need this
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        #This resets the pattern
        #three logs go across the screen and start going off
        #when the second is half of the first reappears
        #log length = 146
        if self.left >= SCREEN_WIDTH:
            self.right = -1.5 * 146 #146 is log length
    

class Logs2(arcade.Sprite): # middle logs
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        #resets logs for pattern
        if self.left >= SCREEN_WIDTH:
            self.right = -3 * 146

class Logs3(arcade.Sprite): # highest logs
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        #resets logs for pattern
        if self.left >= SCREEN_WIDTH:
            self.right = -194

class LowerTurtles(arcade.Sprite): #lowest turtle
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        #resets turtles for pattern
        if self.right <= 0:
            self.right = SCREEN_WIDTH + LANE_SIZE * 8

class LowerTurtlesAnimated(arcade.Sprite): #lowest turtle
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.texture = arcade.load_texture("Turtles.png") #starts as full turtles
        self.update_counter = 0 #tracks Turtle animation
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        #Loop of turtle Animation
        self.update_counter += 1 #keeps track of the state of the turtles
        turtle_loop_speed = 25  #how fast turtles cycle
        if self.right <= 0:
            self.right = SCREEN_WIDTH + LANE_SIZE * 8
        if self.update_counter < turtle_loop_speed:
            self.texture = arcade.load_texture("Turtles.png") #Regular turtles
        elif self.update_counter < turtle_loop_speed * 2:
            self.texture = arcade.load_texture("TurtlesTucking1.png") #turtles start sinking
        elif self.update_counter < turtle_loop_speed * 3:
            self.texture = arcade.load_texture("TurtlesTucking2.png") #turtles sink farther
        elif self.update_counter < turtle_loop_speed *4:
            self.texture = arcade.load_texture("TurtlesTucking3.png")  #turtles almost gone
        elif self.update_counter == turtle_loop_speed * 4:
            self.visible = False  #Turtles Have gone under
            #self.texture = arcade.load_texture("Water.png")
        elif self.update_counter == turtle_loop_speed * 5:
            self.visible = True  #resets to showing turtle sprites
        elif self.update_counter < turtle_loop_speed * 6:
            self.texture = arcade.load_texture("TurtlesRising.png") #Turtles rising
        if self.update_counter > turtle_loop_speed * 6:
            self.update_counter = 0  #restart turtle loop

class UpperTurtles(arcade.Sprite): #lowest turtle
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        if self.right <= 0:
            self.right = SCREEN_WIDTH + LANE_SIZE * 8

class UpperTurtlesAnimated(arcade.Sprite): #lowest turtle
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
        self.texture = arcade.load_texture("TwoTurtles.png")
        self.update_counter = 0 #tracks Turtle animation
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        #Loop of turtle Animation
        self.update_counter += 1 #keeps track of the state of the turtles
        turtle_loop_speed = 25  #how fast turtles cycle
        if self.right <= 0:
            self.right = SCREEN_WIDTH + LANE_SIZE * 8
        if self.update_counter < turtle_loop_speed:
            self.texture = arcade.load_texture("TwoTurtles.png") #Regular turtles
        elif self.update_counter < turtle_loop_speed * 2:
            self.texture = arcade.load_texture("TwoTurtlesTucking1.png") #turtles start sinking
        elif self.update_counter < turtle_loop_speed * 3:
            self.texture = arcade.load_texture("TwoTurtlesTucking2.png") #turtles sink farther
        elif self.update_counter < turtle_loop_speed *4:
            self.texture = arcade.load_texture("TwoTurtlesTucking3.png")  #turtles almost gone
        elif self.update_counter == turtle_loop_speed * 4:
            self.visible = False  #Turtles Have gone under
            #self.texture = arcade.load_texture("Water.png")
        elif self.update_counter == turtle_loop_speed * 5:
            self.visible = True  #resets to showing turtle sprites
        elif self.update_counter < turtle_loop_speed * 6:
            self.texture = arcade.load_texture("TwoTurtlesRising.png") #Turtles rising
        if self.update_counter > turtle_loop_speed * 6:
            self.update_counter = 0  #restart turtle loop


class FroggerGame(arcade.View):
    def __init__(self):
        """ Initializer """
        super().__init__()

        # variables that will hold sprite lists
        self.player_list = None
        self.background = None
        self.log_list = None
        self.animated_log_list = None
        self.car_list = None

        # set up the player info
        self.player_sprite = None

        # default score and lives
        self.score = 0
        self.lives = 3

        # track y position for score
        self.max_y_position = 0

    def setup(self):
        """ Set up the game and initialize the variables. """
        # sprite lists
        self.player_list = arcade.SpriteList()
        self.log_list = arcade.SpriteList()  #list of logs (TURTLES ARE CONSIDERED LOGS)
        self.animated_log_list = arcade.SpriteList()  #list of animated logs (turtles)
        self.car_list = arcade.SpriteList()

        # load frogger grid
        self.background = arcade.load_texture("assets/froggerGrid.png")

        # set up player sprite size
        self.player_sprite = UserFrog("assets/froggerSprite.png", 1.0)
        sprite_width = self.player_sprite.width
        sprite_height = self.player_sprite.height

        # scaling player sprite
        scale_x = MOVEMENT_DISTANCE / sprite_width
        scale_y = MOVEMENT_DISTANCE / sprite_height
        self.player_sprite.scale = min(scale_x, scale_y)

        # set initial player sprite position
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0
        self.player_list.append(self.player_sprite)

        # create car sprites
        car_sprites = ["assets/car1.png", "assets/car2flipped.png", "assets/car3.png",
                       "assets/car4flipped.png", "assets/car5.png"]
        # Starting from lane 2 (if spawn is lane 0)
        lane_start = 2
        # create each car and add it to car_list
        for i, car_sprite in enumerate(car_sprites):
            lane = lane_start + i
            car = Car(car_sprite, car_speed = 2 + i * 0.5, direction = 1 if i % 2 == 0 else -1)
            car.center_x = i * 100
            car.bottom = LANE_SIZE * lane
            self.car_list.append(car)


        #create log sprites--------------------------------------------
        #log_source = "Log (1).png"
        log_source = "SmallLogFinal.png"
        log_source2 = "BigLogFinal.png"
        log_source3 = "MediumLogFinal2.png"
        turtle_source1 = "Turtles.png"
        turtle_source2 = "TwoTurtles.png"
        log_length = 146
        #lane 1*************************************
        self.log_sprite = Logs(log_source, logSpeed=2) #creates log of the first variety
        self.log_sprite.right = 0 #xposition
        self.log_sprite.bottom = LANE_SIZE * 9 
        self.log_list.append(self.log_sprite) #add to list of sprites
        self.log_sprite = Logs(log_source, logSpeed=2)
        self.log_sprite.right = -log_length*2
        self.log_sprite.bottom = LANE_SIZE * 9
        self.log_list.append(self.log_sprite)
        self.log_sprite = Logs(log_source, logSpeed=2)
        self.log_sprite.right = -log_length*4
        self.log_sprite.bottom = LANE_SIZE * 9
        self.log_list.append(self.log_sprite)
        #end lane 1***********************************

        #lane2****************************************
        self.log_sprite = Logs2(log_source2, logSpeed=3)
        self.log_sprite.right = 0
        self.log_sprite.bottom = LANE_SIZE * 10 
        self.log_list.append(self.log_sprite)
        self.log_sprite = Logs2(log_source2, logSpeed=3)
        self.log_sprite.right = -log_length * 3
        self.log_sprite.bottom = LANE_SIZE * 10 
        self.log_list.append(self.log_sprite)
        self.log_sprite = Logs2(log_source2, logSpeed=3)
        self.log_sprite.right = -log_length * 6
        self.log_sprite.bottom = LANE_SIZE * 10 
        self.log_list.append(self.log_sprite)
        #end Lane 2***********************************

        #lane3
        self.log_sprite = Logs3(log_source3, logSpeed=2.5)
        self.log_sprite.right = 0
        self.log_sprite.bottom = LANE_SIZE * 12 
        self.log_list.append(self.log_sprite)

        self.log_sprite = Logs3(log_source3, logSpeed=2.5)
        self.log_sprite.right = -194 - 48.5
        self.log_sprite.bottom = LANE_SIZE * 12 
        self.log_list.append(self.log_sprite)
        self.log_sprite = Logs3(log_source3, logSpeed=2.5)
        self.log_sprite.right = (-194 - 48.5) * 2
        self.log_sprite.bottom = LANE_SIZE * 12 
        self.log_list.append(self.log_sprite)
        self.log_sprite = Logs3(log_source3, logSpeed=2.5)
        self.log_sprite.right = (-194 - 48.5) * 3
        self.log_sprite.bottom = LANE_SIZE * 12 
        self.log_list.append(self.log_sprite)
        #end of log sprites---------------------------------------------

        #Start Turtle Sprites--------------------------------------------
        #Upper Turtles
        #Blinking
        self.log_sprite = UpperTurtlesAnimated(logSpeed=-3)
        self.log_sprite.left = SCREEN_WIDTH
        self.log_sprite.bottom = LANE_SIZE * 11 
        self.log_sprite.hit_box = [[-65, 0], [17, 0]]  #adjusts the hitbox of the turtles to be smaller
        self.animated_log_list.append(self.log_sprite)
        #Non blinking
        for i in range(1,4):
            self.log_sprite = UpperTurtles(turtle_source2, logSpeed=-3)
            self.log_sprite.left = SCREEN_WIDTH + (LANE_SIZE * 4) * i
            self.log_sprite.bottom = LANE_SIZE * 11 
            self.log_sprite.hit_box = [[-65, 0], [17, 0]]  #adjusts the hitbox of the turtles to be smaller
            self.log_list.append(self.log_sprite)
        
        #Lower Turtles
        #Non blinking
        for i in range(4):
            self.log_sprite = LowerTurtles(turtle_source1, logSpeed=-3)
            self.log_sprite.left = SCREEN_WIDTH + (LANE_SIZE * 4) * i
            self.log_sprite.bottom = LANE_SIZE * 8 
            self.log_sprite.hit_box = [[-65, 0], [66, 0]]  #adjusts the hitbox of the turtles to be smaller
            self.log_list.append(self.log_sprite)
        #Blinking
        self.log_sprite = LowerTurtlesAnimated(logSpeed=-3)
        self.log_sprite.left = SCREEN_WIDTH + LANE_SIZE * 16
        self.log_sprite.bottom = LANE_SIZE * 8 
        self.log_sprite.hit_box = [[-65, 0], [66, 0]]  #adjusts the hitbox of the turtles to be smaller
        self.animated_log_list.append(self.log_sprite)
        #end of turtle sprites----------------------------------------------

    def on_draw(self):
        """ Render the screen. """
        self.clear()

        # draw the background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # draw all the sprites
        self.log_list.draw()
        #self.log_list.draw_hit_boxes()
        self.animated_log_list.draw()
        self.player_list.draw()
        self.car_list.draw()

        # draw the score and lives at the top of the screen
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.YELLOW_ROSE, 20)
        arcade.draw_text(f"Lives: {self.lives}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30, arcade.color.YELLOW_ROSE, 20)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_list.update()
        self.car_list.update()

        # check for collision with cars
        for car in self.car_list:
            if arcade.check_for_collision(self.player_sprite, car):
                self.player_sprite.center_x, self.player_sprite.center_y = 0, 0  # Reset to start if collision
                self.lives -= 1

        # check for collision with logs
        frog_on_log = False
        for log in self.log_list:
            if arcade.check_for_collision(self.player_sprite, log):
                self.player_sprite.left += log.logSpeed
                frog_on_log = True

                
        for log in self.animated_log_list:
            #with the animated logs (turtles) no collision occurs if they are not visible (under water)
            log_collision = arcade.check_for_collision(self.player_sprite, log) and log.visible == True
            if log_collision:
                self.player_sprite.left += log.logSpeed
                frog_on_log = True

        lake_area_bottom = SCREEN_HEIGHT - 400
        lake_area_top = SCREEN_HEIGHT - 70

        # check if player is in the lake area and not on a log
        if lake_area_bottom <= self.player_sprite.center_y <= lake_area_top and not frog_on_log:
            # Reset frog to starting position and decrease life count
            self.player_sprite.center_x, self.player_sprite.center_y = 0, 0
            self.lives -= 1

        self.log_list.update()
        self.animated_log_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.UP:
            new_y = self.player_sprite.center_y + MOVEMENT_DISTANCE
            self.player_sprite.center_y = new_y
            # rotate png up
            self.player_sprite.angle = 0

            # check if the sprite moved up higher than ever before
            if new_y > self.max_y_position:
                self.score += 10
                self.max_y_position = new_y

        elif key == arcade.key.DOWN:
            self.player_sprite.center_y -= MOVEMENT_DISTANCE
            # rotate png down
            self.player_sprite.angle = 180
        elif key == arcade.key.LEFT:
            self.player_sprite.center_x -= MOVEMENT_DISTANCE
            # rotate png left
            self.player_sprite.angle = 90
        elif key == arcade.key.RIGHT:
            self.player_sprite.center_x += MOVEMENT_DISTANCE
            # rotate png right
            self.player_sprite.angle = 270

        # TODO: escape key brings player back to start menu or a pause screen
        # if key == arcade.key.ESCAPE:


def main():
    """ Main function """
    """ Startup """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
