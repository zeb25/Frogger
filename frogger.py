import arcade

# size of one grid square
MOVEMENT_DISTANCE = 64

# screen dimensions to be multiples of MOVEMENT_DISTANCE
SCREEN_WIDTH = 768
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Frogger"


class UserFrog(arcade.Sprite):
    def update(self):
        """ Ensure the player stays within bounds. """
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class FroggerGame(arcade.Window):
    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # sprite lists
        self.player_list = arcade.SpriteList()

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

    def on_draw(self):
        """ Render the screen. """
        self.clear()
        # Draw all the sprites
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.UP:
            self.player_sprite.center_y += MOVEMENT_DISTANCE
            # rotate png up
            self.player_sprite.angle = 0
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
