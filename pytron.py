from turtle import *


class BikerControls:
    def __init__(self, up_key, left_key, down_key, right_key):
        self.up_key = up_key
        self.left_key = left_key
        self.down_key = down_key
        self.right_key = right_key

    def is_mapped(self, event_char):
        return self.up_key == event_char or self.left_key == event_char or self.down_key == event_char or self.right_key == event_char


class Biker:
    def __init__(self, turtle, name, controls):
        self.turtle = turtle
        self.name = name
        self.controls = controls
        self.direction = "right"
        self.turtle.pencolor("red")

    def matches(self, event):
        return self.controls.is_mapped(event.char)

    def handle(self, event):
        if self.controls.right_key == event.char and not self.direction == "left":
            self.go_right()
        elif self.controls.left_key == event.char and not self.direction == "right":
            self.go_left()
        elif self.controls.up_key == event.char and not self.direction == "down":
            self.go_up()
        elif self.controls.down_key == event.char and not self.direction == "up":
            self.go_down()

    def go_right(self):
        if self.direction == "up":
            self.turtle.rt(90)
        elif self.direction == "down":
            self.turtle.lt(90)

        self.turtle.fd(50)
        self.direction = "right"

    def go_left(self):
        if self.direction == "up":
            self.turtle.lt(90)
        elif self.direction == "down":
            self.turtle.rt(90)

        self.turtle.fd(50)
        self.direction = "left"

    def go_up(self):
        if self.direction == "right":
            self.turtle.lt(90)
        elif self.direction == "left":
            self.turtle.rt(90)

        self.turtle.fd(50)
        self.direction = "up"

    def go_down(self):
        if self.direction == "right":
            self.turtle.rt(90)
        elif self.direction == "left":
            self.turtle.lt(90)

        self.turtle.fd(50)
        self.direction = "down"

    def get_to_position(self):
        self.turtle.penup()
        self.turtle.sety(100)
        self.turtle.pendown()

    def get_name(self):
        return self.name


class KeyboardListener:
    listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def on_key_press(self, event):
        for listener in self.listeners:
            if listener.matches(event):
                listener.handle(event)


def main():
    canvas = getcanvas()
    root = canvas.winfo_toplevel()
    player_one = Biker(Turtle(), "plot 1", BikerControls('w', 'a', 's', 'd'))
    player_two = Biker(Turtle(), "plot 2", BikerControls('i', 'j', 'k', 'l'))
    player_two.get_to_position()
    keyboard_listener = KeyboardListener()
    keyboard_listener.add_listener(player_one)
    keyboard_listener.add_listener(player_two)
    root.bind('<KeyPress>', keyboard_listener.on_key_press)


if __name__ == '__main__':
    main()
    Screen().exitonclick()
