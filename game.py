import arcade
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

class gamewindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,'Bouncing ball')
        arcade.set_background_color(arcade.color.PINK)
        self.background= arcade.load_texture('images/galaxy.jpg')

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    

    

def main():
    gamewindow()
    arcade.run()

if __name__ == '__main__':
   main()
