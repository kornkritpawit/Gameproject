import arcade
import math

import arcade
import math


class Line:
    INPUT_POINT_COUNT = 2

    def __init__(self, points, options=None):
        self.x1 = points[0][0]
        self.y1 = points[0][1]
        self.x2 = points[1][0]
        self.y2 = points[1][1]

        if options and 'color' in options:
            self.color = options['color']
        else:
            self.color = arcade.color.BLACK

    def draw(self):
        arcade.draw_line(self.x1, self.y1,
                         self.x2, self.y2,
                         self.color)


class Circle:
    INPUT_POINT_COUNT = 2

    def __init__(self, points, options=None):
        self.x = points[0][0]
        self.y = points[0][1]

        self.rx = points[1][0]
        self.ry = points[1][1]

        self.radius = math.sqrt((self.x - self.rx) ** 2
                                + (self.y - self.ry) ** 2)
        if options and 'color' in options:
            self.color = options['color']
        else:
            self.color = arcade.color.BLACK

    def draw(self):
        arcade.draw_circle_outline(self.x, self.y,
                                   self.radius,
                                   self.color)


class Rectangle:
    INPUT_POINT_COUNT = 2

    def __init__(self, points, options=None):
        self.x1 = points[0][0]
        self.y1 = points[0][1]
        self.x2 = points[1][0]
        self.y2 = points[1][1]
        self.widht = abs(self.x1 - self.x2)
        self.height = abs(self.y1 - self.y2)
        self.center_x = (self.x1 + self.x2) / 2
        self.center_y = (self.y1 + self.y2) / 2

        if options and 'color' in options:
            self.color = options['color']
        else:
            self.color = arcade.color.BLACK

    def draw(self):
        arcade.draw_rectangle_outline(
            self.center_x, self.center_y, self.widht, self.height, self.color)


class Triangle:
    INPUT_POINT_COUNT = 3

    def __init__(self, points, options=None):
        self.x1 = points[0][0]
        self.y1 = points[0][1]
        self.x2 = points[1][0]
        self.y2 = points[1][1]
        self.x3 = points[2][0]
        self.y3 = points[2][1]

        if options and 'color' in options:
            self.color = options['color']
        else:
            self.color = arcade.color.BLACK

    def draw(self):
        arcade.draw_triangle_outline(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.color)


class Square:
    INPUT_POINT_COUNT = 2

    def __init__(self, points, options=None):
        self.x1 = points[0][0]
        self.y1 = points[0][1]
        self.x2 = points[1][0]
        self.y2 = points[1][1]
        self.widht = abs(self.x1 - self.x2)
        self.height = abs(self.y1 - self.y2)
        self.center_x = (self.x1 + self.x2) / 2
        self.center_y = (self.y1 + self.y2) / 2
        self.abs_widht = max(self.widht, self.height)

        if options and 'color' in options:
            self.color = options['color']
        else:
            self.color = arcade.color.BLACK

    def draw(self):
        arcade.draw_rectangle_outline(
            self.center_x, self.center_y, self.abs_widht, self.abs_widht, self.color)


class Ellipse:
    INPUT_POINT_COUNT = 2

    def __init__(self, points, options=None):
        self.x1 = points[0][0]
        self.y1 = points[0][1]
        self.x2 = points[1][0]
        self.y2 = points[1][1]
        self.widht = abs(self.x1 - self.x2)
        self.height = abs(self.y1 - self.y2)
        self.center_x = (self.x1 + self.x2) / 2
        self.center_y = (self.y1 + self.y2) / 2

        if options and 'color' in options:
            self.color = options['color']
        else:
            self.color = arcade.color.BLACK

    def draw(self):
        arcade.draw_ellipse_outline(
            self.center_x, self.center_y, self.widht, self.height, self.color)