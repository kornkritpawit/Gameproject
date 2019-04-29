import arcade.key
import math
from template.pos import check_brick
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
        self.vx = 0
    def update(self,delta):
        if self.x >= 875:
            self.x = 874
        elif self.x<=90:
            self.x = 95
        self.x += self.vx


class ball(Model):
    STATE_FROZEN = 1
    STATE_STARTED = 2

    def __init__(self, world, x, y,brick):
        super().__init__(world, x, y, 0)
        self.vx = 0
        self.vy = 0
        self.state = ball.STATE_FROZEN
        self.brick = brick


    def is_hit(self, wood):
        if self.y-20<=wood.y+25 and wood.x+125>=self.x>=wood.x-125:
            return True
    def brick_bounce(self):
        y,x = check_brick(self.x,self.y)
        if y==-1 or x == -1:
            return
        if self.brick.has_dot[y][x] == True:
            self.brick.has_dot[y][x] = False
            print(self.brick.has_dot)
            return True


    def update(self,delta):
        if self.state == ball.STATE_FROZEN:
            if self.x >= 875:
                self.x = 874
            elif self.x<=90:
                self.x = 95
        self.x += self.vx
        self.y += self.vy
        def bounce():
            if self.x>=1000 or self.x<=0:
                self.vx = -self.vx
            if self.y>=800:
                self.vy = -self.vy
        bounce()
        if self.brick_bounce():
            self.vy = -self.vy
class Brick:
    def __init__(self, world):
        self.map = [ '##########',
                     '##########',
                     '##########',
                     '##########',
                     '##########',
                    ]
        self.pos_x = [[50, 150, 250, 350, 450, 550, 650, 750, 850, 950],
         [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],
         [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],
         [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],
         [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]]
        self.pos_y = [[450, 450, 450, 450, 450, 450, 450, 450, 450, 450],
         [510, 510, 510, 510, 510, 510, 510, 510, 510, 510],
         [570, 570, 570, 570, 570, 570, 570, 570, 570, 570],
         [630, 630, 630, 630, 630, 630, 630, 630, 630, 630],
         [690, 690, 690, 690, 690, 690, 690, 690, 690, 690]]
        self.pos = pos = [(50, 450), (150, 450), (250, 450), (350, 450), (450, 450),
 (550, 450), (650, 450), (750, 450), (850, 450), (950, 450),
 (50, 510), (150, 510), (250, 510), (350, 510), (450, 510),
 (550, 510), (650, 510), (750, 510), (850, 510), (950, 510),
 (50, 570), (150, 570), (250, 570), (350, 570), (450, 570),
 (550, 570), (650, 570), (750, 570), (850, 570), (950, 570),
 (50, 630), (150, 630), (250, 630), (350, 630), (450, 630),
 (550, 630), (650, 630), (750, 630), (850, 630), (950, 630),
 (50, 690), (150, 690), (250, 690), (350, 690), (450, 690),
 (550, 690), (650, 690), (750, 690), (850, 690), (950, 690)]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.init_dot_data()



    def init_dot_data(self):
        has_dot = {}
        for r in range(self.height):
            has_dot[r] = {}
            for c in range(self.width):
                has_dot[r][c] = self.map[r][c] == '#'
        self.has_dot = has_dot

    def init_brick_pos(self,pos):
        self.pos = pos
        if self.n<=0:
            print(self.pos)
            self.n+=1

    def remove_dot_at(self, r, c):
        self.has_dot[r][c] = False

    # def has_wall_at(self, r, c):
    #     return self.map[r][c] == '#'

    def has_dot_at(self, r, c):
        return self.has_dot[r][c]

class World:
    STATE_FROZEN = 1
    STATE_STARTED = 2
    STATE_DEAD = 3
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wood = wood(self, 500, 25)
        self.state = World.STATE_FROZEN
        self.brick = Brick(self)
        self.ball = ball(self, 500, 65,self.brick)

        self.score = 0
        self.ball_life = 5

    def start(self):
        self.state = World.STATE_STARTED
        self.ball.state = ball.STATE_STARTED

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.wood.vx = -20
            if self.state == World.STATE_FROZEN:
                self.ball.vx = -20
        elif key == arcade.key.RIGHT:
            self.wood.vx = 20
            if self.state == World.STATE_FROZEN:
                self.ball.vx = 20
    def is_hit(self):
        if self.ball.y-20<=self.wood.y+25 and self.wood.x+125>=self.ball.x>=self.wood.x-125:
            return True

    def reset(self):
        if self.ball.y < 0:
            self.wood.x = 500
            self.ball.x = self.wood.x
            self.ball.y = 65
            self.ball.state = ball.STATE_FROZEN
            self.state = World.STATE_FROZEN
            self.ball.vx = 0
            self.ball.vy = 0
            self.ball_life -= 1
            # self.ball.state =


    def on_mouse_press(self,x,y):
        dx = (x - self.ball.x)
        dy = (y - self.ball.y)
        angle = math.atan2(dy,dx)
        vx = math.cos(angle)
        vy = math.sin(angle)
        if self.state == World.STATE_FROZEN:
            self.ball.state = ball.STATE_STARTED
            self.ball.vx = vx*10
            self.ball.vy = vy*10
            self.state = World.STATE_STARTED

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.wood.vx = 0
        if self.ball.state == self.STATE_FROZEN:
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.ball.vx = 0

    def update(self, delta):
        self.wood.update(delta)
        self.ball.update(delta)
        if self.state == self.STATE_STARTED:
            if self.is_hit():
                # self.ball.vx = -self.ball.vx
                self.ball.vy = -self.ball.vy
        self.reset()




