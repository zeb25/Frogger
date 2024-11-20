import arcade

arcade.load_font("fonts/ARCADE_N.TTF")  # Load a .ttf font file
# TODO: replace these with actual top scoring
top_scores = [3000, 2000, 1500]

class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.NAVY_BLUE)

    def on_draw(self):
        """ Draw the menu """
        self.clear()

        # Draw the game title with a shadow effect
        arcade.draw_text(
            "FROGGER",
            self.window.width / 2,
            self.window.height - 100,
            arcade.color.LIME_GREEN,
            font_size=60,
            anchor_x="center",
            font_name="Arcade Normal"
        )
        # Add a shadow for the title
        arcade.draw_text(
            "FROGGER",
            (self.window.width / 2) + 5,  # Slight offset for shadow
            (self.window.height - 100) - 2,
            arcade.color.GREEN,
            font_size=60,
            anchor_x="center",
            font_name="Arcade Normal"
        )

        arcade.draw_text(" -POINT TABLE- ", self.window.width / 2, self.window.height - 250,
                         arcade.color.AZURE_MIST, font_size=20, anchor_x="center", font_name="Arcade Normal")
        arcade.draw_text("10 PTS FOR EACH STEP", self.window.width / 2, self.window.height - 300,
                         arcade.color.AUREOLIN, font_size=12, anchor_x="center", font_name="Arcade Normal")
        arcade.draw_text("50 PTS FOR EVERY FROG ON A LILY PAD", self.window.width / 2, self.window.height - 350,
                         arcade.color.AUREOLIN, font_size=12, anchor_x="center", font_name="Arcade Normal")

        arcade.draw_text("PRESS \"I\" FOR INSTRUCTIONS", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.AZURE_MIST, font_size=18, anchor_x="center", font_name="Arcade Normal")

        arcade.draw_text("PRESS \"P\" TO PLAY", self.window.width / 2, self.window.height / 2 - 130,
                         arcade.color.AZURE_MIST, font_size=18, anchor_x="center", font_name="Arcade Normal")
        arcade.draw_text(" -TOP SCORES- ", self.window.width / 2, self.window.height / 2 - 200,
                         arcade.color.AUREOLIN, font_size=20, anchor_x="center", font_name="Arcade Normal")
        for index, score in enumerate(top_scores):
            arcade.draw_text(f"{index + 1}. {score}", self.window.width / 2, self.window.height / 2 - 240 - (index * 30),
                             arcade.color.AZURE_MIST, font_size=20, anchor_x="center", font_name="Arcade Normal")

    def on_key_press(self, key, _modifiers):
        """ Use a key press to advance to the 'game' view. """
        if key == arcade.key.P:
            from frogger import FroggerGame
            frogger_game = FroggerGame()
            frogger_game.setup()
            self.window.show_view(frogger_game)

        if key == arcade.key.I:
            instruction_view = InstructionView()
            self.window.show_view(instruction_view)

class InstructionView(arcade.View):
    """ Class that manages the 'instruction' view. """
    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
        """ Draw the instruction screen """
        self.clear()

        arcade.draw_text(" -HOW TO PLAY- ", self.window.width / 2, self.window.height - 250,
                         arcade.color.AZURE_MIST, font_size=20, anchor_x="center", font_name="Arcade Normal")
        arcade.draw_text("Use the arrow keys to move the frog", self.window.width / 2, self.window.height - 300,
                         arcade.color.AUREOLIN, font_size=10, anchor_x="center", font_name="Arcade Normal")
        arcade.draw_text("Avoid cars and reach the lily pads safely", self.window.width / 2, self.window.height - 350,
                         arcade.color.AUREOLIN, font_size=10, anchor_x="center", font_name="Arcade Normal")

        # Instruction to return to the menu
        arcade.draw_text(
            "Press \"ESC\" to return to the main menu", self.window.width / 2, self.window.height - 400,
            arcade.color.AZURE_MIST, font_size=12, anchor_x="center", font_name="Arcade Normal")

    def on_key_press(self, key, _modifiers):
        """ Use a key press to get back to the start screen"""
        if key == arcade.key.ESCAPE:
            menu_view = MenuView()
            self.window.show_view(menu_view)
