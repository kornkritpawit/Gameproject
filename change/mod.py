import arcade.key
class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <=hit_size)

class wood(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

    def update(self,delta):
        if self.x <= 0:
            self.x +=50
        elif self.x >= 1000:
            self.x -= 50


class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wood = wood(self, 500, 25)
        self.score = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.wood.x -= 50
        elif key == arcade.key.RIGHT:
            self.wood.x += 50

    def update(self, delta):
        self.wood.update(delta)

    # def update(self, delta):
    #     self.ship.update(delta)
    #     if self.ship.hit(self.gold, 10):
    #         self.gold.random_location()
    #         self.score += 1
    #
    # def on_key_press(self, key, key_modifiers):
    #     if key == arcade.key.SPACE:
    #         self.ship.switch_direction()

