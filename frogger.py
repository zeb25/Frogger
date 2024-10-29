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
        if self.left >= 679:
            self.right = -1.5 * 146 #146 is log length
    

class Logs2(arcade.Sprite): #middle logs
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
    #I don't think I need this
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        if self.left >= 679:
            self.right = -3 * 146


class Logs3(arcade.Sprite): #highest logs
    def __init__(self, filename = None, scale = 1, image_x = 0, image_y = 0, image_width = 0, image_height = 0, center_x = 0, center_y = 0, repeat_count_x = 1, repeat_count_y = 1, flipped_horizontally = False, flipped_vertically = False, flipped_diagonally = False, hit_box_algorithm = "Simple", hit_box_detail = 4.5, texture = None, angle = 0, logSpeed = 5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.logSpeed = logSpeed
    #I don't think I need this
    def setLogSpeed(self, logSpeed):
        self.logSpeed = logSpeed
    def update(self):
        self.left += self.logSpeed
        if self.left >= 679:
            self.right = 0


class FroggerGame(arcade.View):
    def __init__(self):
        """ Initializer """
        super().__init__()

        # variables that will hold sprite lists
        self.player_list = None
        self.background = None
        self.log_list = None
        self.car_list = None

        # set up the player info
        self.player_sprite = None

        # default score and lives
        self.score = 0
        self.lives = 3

        # track y position for score
        self.max_y_position = 0

        # # setting default x, y positions and velocity
        # self.x = 0
        # self.y = SCREEN_HEIGHT - 20
        # self.velocity = 300

    def setup(self):
        """ Set up the game and initialize the variables. """
        # sprite lists
        self.player_list = arcade.SpriteList()
        self.log_list = arcade.SpriteList()
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
        lane_start = 2  # Starting from lane 2 (if spawn is lane 0)
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
        log_source3 = "MediumLogFinal.png"
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
        #self.log_sprite.center_y = LANE_SIZE * 12 + 20
        self.log_list.append(self.log_sprite)
        #end of log sprites----------------------------------------------

    def on_draw(self):
        """ Render the screen. """
        self.clear()

        # draw the background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # draw all the sprites
        self.log_list.draw()
        self.player_list.draw()
        self.car_list.draw()

        # draw the score and lives at the top of the screen
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.YELLOW_ROSE, 20)
        arcade.draw_text(f"Lives: {self.lives}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30, arcade.color.YELLOW_ROSE, 20)

        # draw an obstacle
        # arcade.draw_rectangle_filled(self.x, self.y, 100, 50, arcade.color.GREEN)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_list.update()
        self.car_list.update()

        # check for collision with logs
        for log in self.log_list:
            log_collision = arcade.check_for_collision(self.player_sprite, log)
            if log_collision:
                self.player_sprite.left += log.logSpeed

        for car in self.car_list:
            if arcade.check_for_collision(self.player_sprite, car):
                self.player_sprite.center_x, self.player_sprite.center_y = 0, 0  # Reset to start
                self.lives -= 1

        # # move the obstacle
        # self.x += self.velocity * delta_time

        self.log_list.update()


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


def main():
    """ Main function """
    """ Startup """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
