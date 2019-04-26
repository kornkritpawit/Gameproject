import arcade
from template.mod import World
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BLOCK_SIZE = 100
BLOCK_HEIGHT = 60
BLOCK_WIDTH = 100



class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()


class gamewindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Bouncing ball')
        self.world = World(SCREEN_WIDTH,SCREEN_HEIGHT)
        arcade.set_background_color(arcade.color.PINK)
        self.background = arcade.load_texture('images/galaxy.jpg')
        self.wood_sprite = ModelSprite('images/wood1.png',model=self.world.wood)
        self.ball_sprite = ModelSprite('images/ball.png',model=self.world.ball)
        self.brick_drawer = BrickDrawer(self.world.brick)

    # def update(self,delta):

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key,key_modifiers)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.world.on_mouse_press(x,y)



    def update(self, delta):
        self.world.update(delta)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.brick_drawer.draw()
        self.wood_sprite.draw()
        self.ball_sprite.draw()
        arcade.draw_text('BALL LIFE: '+str(self.world.ball_life),
                         self.width - 200, self.height - 50,
                         arcade.color.YELLOW, 20)

class BrickDrawer:
    def __init__(self, brick):
        self.brick = brick
        self.width = self.brick.width
        self.height = self.brick.height

        self.brick_sprite = arcade.Sprite('images/wall.png')

    def get_sprite_position(self, r, c):
        x = c * BLOCK_WIDTH + (BLOCK_WIDTH // 2);
        y = r * BLOCK_HEIGHT + (BLOCK_HEIGHT + (BLOCK_HEIGHT // 2))+360
        return x,y
    def draw_sprite(self, sprite, r, c):
        x, y = self.get_sprite_position(r, c)
        sprite.set_position(x, y)
        sprite.draw()

    def draw(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.brick.has_dot_at(r, c):
                    self.draw_sprite(self.brick_sprite, r, c)

def main():
    window = gamewindow()
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()