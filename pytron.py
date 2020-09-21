from turtle import *


class BikerControls:
    def __init__(self, up_key, left_key, down_key, right_key):
        self.up_key = up_key
        self.left_key = left_key
        self.down_key = down_key
        self.right_key = right_key


class Biker:
    def __init__(self, turtle, name, controls):
        self.turtle = turtle
        self.name = name
        self.controls = controls

    def matches(self, event):
        return event.char == self.controls.right_key

    def handle(self, event):
        self.turtle.fd(50)

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
        print("You pressed " + event.char)
        for listener in self.listeners:
            if listener.matches(event):
                print("turtle: " + listener.get_name())
                listener.handle(event)


# Make one turtle move around
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
