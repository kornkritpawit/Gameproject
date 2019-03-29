import arcade
from template.mod import World
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


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

    # def update(self,delta):

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.wood_sprite.draw()

def main():
    gamewindow()
    arcade.run()


if __name__ == '__main__':
    main()