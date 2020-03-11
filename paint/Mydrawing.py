from drawings import Line, Circle, Rectangle, Triangle, Ellipse, Square
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CANVAS_BORDER = 50
TOOLBOX_ICON_SIZE = 30

drawing_tools = []

COLOR_OPTIONS = [
    arcade.color.WHITE,
    arcade.color.RED,
    arcade.color.GREEN,
    arcade.color.BLUE,
    arcade.color.YELLOW,
    arcade.color.BLACK,
]


class DrawingTool:
    def __init__(self, drawing_cls, name, icon_char, point_count):
        self.drawing_cls = drawing_cls
        self.name = name
        self.icon_char = icon_char
        self.point_count = point_count


def register_drawing_tool(cls, name, icon_char):
    drawing_tools.append(DrawingTool(
        cls, name, icon_char, cls.INPUT_POINT_COUNT))


class PaintWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.mouse_x = 0
        self.mouse_y = 0
        self.canvas_mouse_x = 0
        self.canvas_mouse_y = 0
        self.on_canvas = False
        self.command_mode = False
        self.current_tool = None
        self.current_color = arcade.color.BLACK

        self.tool_points = []

        self.drawings = []

    def draw_pointer(self):
        arcade.draw_circle_filled(self.mouse_x,
                                  self.mouse_y,
                                  10,
                                  arcade.color.BLACK)

    def draw_canvas(self):
        arcade.draw_rectangle_outline(SCREEN_WIDTH // 2,
                                      SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH - CANVAS_BORDER * 2,
                                      SCREEN_HEIGHT - CANVAS_BORDER * 2,
                                      arcade.color.BLACK)

    def tool_icon_box(self, idx):
        box_center_x = CANVAS_BORDER // 2
        box_center_y = (SCREEN_HEIGHT - CANVAS_BORDER - (TOOLBOX_ICON_SIZE // 2)
                        - idx * TOOLBOX_ICON_SIZE)
        return (box_center_x - TOOLBOX_ICON_SIZE // 2, box_center_y - TOOLBOX_ICON_SIZE // 2,
                box_center_x + TOOLBOX_ICON_SIZE // 2, box_center_y + TOOLBOX_ICON_SIZE // 2)

    def draw_tools(self):
        i = 0
        for t in drawing_tools:
            x1, y1, x2, y2 = self.tool_icon_box(i)

            box_center_x = (x1 + x2) // 2
            box_center_y = (y1 + y2) // 2
            if t == self.current_tool:
                arcade.draw_rectangle_filled(box_center_x, box_center_y,
                                             TOOLBOX_ICON_SIZE, TOOLBOX_ICON_SIZE,
                                             arcade.color.BLUEBERRY)

                arcade.draw_text(t.icon_char,
                                 box_center_x - 5,
                                 box_center_y - 5,
                                 arcade.color.WHITE)
            else:
                arcade.draw_rectangle_outline(box_center_x, box_center_y,
                                              TOOLBOX_ICON_SIZE, TOOLBOX_ICON_SIZE,
                                              arcade.color.BLACK)
                arcade.draw_text(t.icon_char,
                                 box_center_x - 5,
                                 box_center_y - 5,
                                 arcade.color.BLACK)

            i += 1

    def draw_color_boxes(self):
        i = 0
        for c in COLOR_OPTIONS:
            arcade.draw_rectangle_filled(CANVAS_BORDER + TOOLBOX_ICON_SIZE // 2 + TOOLBOX_ICON_SIZE * i,
                                         CANVAS_BORDER - TOOLBOX_ICON_SIZE // 2,
                                         TOOLBOX_ICON_SIZE, TOOLBOX_ICON_SIZE,
                                         c)
            arcade.draw_rectangle_outline(CANVAS_BORDER + TOOLBOX_ICON_SIZE // 2 + TOOLBOX_ICON_SIZE * i,
                                          CANVAS_BORDER - TOOLBOX_ICON_SIZE // 2,
                                          TOOLBOX_ICON_SIZE, TOOLBOX_ICON_SIZE,
                                          arcade.color.BLACK)
            i += 1

    def draw_interface(self):
        self.draw_canvas()
        self.draw_tools()
        self.draw_color_boxes()

        if self.on_canvas:
            self.draw_pointer()

    def on_draw(self):
        arcade.start_render()
        if self.tool_points:
            for t in self.tool_points:
                arcade.draw_circle_filled(t[0], t[1], 5, self.current_color)
        self.draw_interface()
        for d in self.drawings:
            d.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
        self.on_canvas = ((CANVAS_BORDER <= x <= SCREEN_WIDTH - CANVAS_BORDER) and
                          (CANVAS_BORDER <= y <= SCREEN_HEIGHT - CANVAS_BORDER))
        if self.on_canvas:
            self.canvas_mouse_x = x - CANVAS_BORDER
            self.canvas_mouse_y = y - CANVAS_BORDER
        else:
            self.canvas_mouse_x = 0
            self.canvas_mouse_y = 0

    def check_tool_press(self, x, y):
        tool = None
        for i in range(len(drawing_tools)):
            x1, y1, x2, y2 = self.tool_icon_box(i)
            if (x1 <= x <= x2) and (y1 <= y <= y2):
                tool = drawing_tools[i]

        if tool != None:
            if self.current_tool != tool:
                self.reset_tool_state()
                self.current_tool = tool

    def check_color_press(self, x, y):
        if CANVAS_BORDER - TOOLBOX_ICON_SIZE <= y <= CANVAS_BORDER:
            cidx = (x - CANVAS_BORDER) // TOOLBOX_ICON_SIZE
            if (cidx >= 0) and (cidx < len(COLOR_OPTIONS)):
                self.current_color = COLOR_OPTIONS[cidx]

    def reset_tool_state(self):
        self.tool_points = []

    def check_canvas_press(self, x, y):
        if not self.current_tool:
            return

        if not self.current_tool.drawing_cls:
            return

        self.tool_points.append((x, y))

        if len(self.tool_points) == self.current_tool.point_count:
            cls = self.current_tool.drawing_cls

            drawing_options = {
                'color': self.current_color,
            }

            new_drawing = cls(self.tool_points, drawing_options)

            self.drawings.append(new_drawing)

            self.reset_tool_state()

    def on_mouse_press(self, x, y, button, modifiers):
        self.check_tool_press(x, y)
        self.check_color_press(x, y)

        if self.on_canvas:
            self.check_canvas_press(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        pass


def initialize():
    drawing_tools.append(DrawingTool(None, 'Reset', 'R', 0))

    register_drawing_tool(Line, 'Line', 'L')
    register_drawing_tool(Circle, 'Circle', 'C')
    register_drawing_tool(Rectangle, "Rectangle", 'R')
    register_drawing_tool(Triangle, "Triangle", 'T')
    register_drawing_tool(Square, "Square", "S")
    register_drawing_tool(Ellipse, "Ellipse", "E")


def main():
    initialize()
    window = PaintWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()