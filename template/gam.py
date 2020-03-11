import arcade
from mod import World
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BLOCK_HEIGHT = 60
BLOCK_WIDTH = 100
text = 'You need to break all bricks to win this game.'


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
        print(self.world.brick.has_dot)
        arcade.set_background_color(arcade.color.PINK)
        self.background = arcade.load_texture('images/background.jpg')
        self.wood_sprite = ModelSprite('images/wood1.png',model=self.world.wood)
        self.ball_sprite = ModelSprite('images/ball.png',model=self.world.ball)
        self.brick_drawer = BrickDrawer(self.world.brick)

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
        if self.world.state == self.world.STATE_FROZEN:
            arcade.draw_text(f'{"You need to break all bricks to win this game.":^100}'+'\n'
                             +f'{"If the ball falls under the wood,your life will decrease.":^100}'+'\n'
                            +f'{"Press left or right arrow key to move the wood to bounce th ball":^100}'+
                             '\n'+f'{"Press somewhere on the screen to shoot the ball and to start the game:":^100}'
                              +'\n'+f' {"Good luck! Beware of your life:":^100}',0
                             ,SCREEN_HEIGHT//2 - 200,arcade.color.WHITE_SMOKE,20)
        if self.world.state == self.world.STATE_WIN:
            arcade.draw_text(f'{"You win the game!!":^100}' + '\n'
                             + f'{"Press space to restart or enter to exit":^100}'
                             , 0, SCREEN_HEIGHT // 2, arcade.color.HEART_GOLD, 25)
        elif self.world.ball_life>=0:
            self.brick_drawer.draw()
            self.wood_sprite.draw()
            self.ball_sprite.draw()
        else:
            arcade.draw_text(f'{"You lose":^100}'+'\n'+f'{"Press space to restart or enter to exit":^100}'
                             ,0,SCREEN_HEIGHT//2,arcade.color.RED_DEVIL,25)

        arcade.draw_text('BALL LIFE: '+str(self.world.ball_life),
                         self.width - 200, self.height - 50,
                         arcade.color.YELLOW, 20)
        arcade.draw_text('Your score: '+str(self.world.score),0,self.height - 50,
                         arcade.color.WHITE_SMOKE,20)


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
        return x,y

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