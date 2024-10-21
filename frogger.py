import arcade

# size of one grid square
MOVEMENT_DISTANCE = 48.5
LANE_SIZE = 48.5

# screen dimensions to be multiples of MOVEMENT_DISTANCE
SCREEN_WIDTH = 679
SCREEN_HEIGHT = 776
SCREEN_TITLE = "Frogger"


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


class Logs(arcade.Sprite): #lowest logs
    def update(self):
        self.center_x += 2
        if self.center_x >= 600:
            self.center_x = 0


class Logs2(arcade.Sprite): #middle logs
    def update(self):
        self.center_x += 3
        if self.center_x >= 600:
            self.center_x = 0


class Logs3(arcade.Sprite): #middle logs
    def update(self):
        self.center_x += 2.5
        if self.center_x >= 600:
            self.center_x = 0


class FroggerGame(arcade.Window):
    def __init__(self, width, height, title):
        """ Initializer """
        super().__init__(width, height, title)

        # variables that will hold sprite lists
        self.player_list = None
        self.background = None
        self.log_list = None

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


        #create log sprites--------------------------------------------
        log_source = "Log (1).png"
        #lane 1
        self.log_sprite = Logs(log_source, 6) #creates log of the first variety
        self.log_sprite.center_x = 0 #xposition
        self.log_sprite.center_y = LANE_SIZE * 9 + 13#450 #yposition
        self.log_list.append(self.log_sprite) #add to list of sprites

        #lane2
        self.log_sprite = Logs2(log_source, 6)
        self.log_sprite.center_x = 0
        self.log_sprite.center_y = LANE_SIZE * 10 + 13
        self.log_list.append(self.log_sprite)

        #lane3
        self.log_sprite = Logs3(log_source, 6)
        self.log_sprite.center_x = 0
        self.log_sprite.center_y = LANE_SIZE * 12 + 13
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

        # draw the score and lives at the top of the screen
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.YELLOW_ROSE, 20)
        arcade.draw_text(f"Lives: {self.lives}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30, arcade.color.YELLOW_ROSE, 20)

        # draw an obstacle
        # arcade.draw_rectangle_filled(self.x, self.y, 100, 50, arcade.color.GREEN)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_list.update()

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
    window = FroggerGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
