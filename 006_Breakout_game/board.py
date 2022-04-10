import time
from turtle import Turtle, Screen


class Board:

    def __init__(self):
        self.body = list()
        self.screen = Screen()
        self.distance = 30
        self.game_width = int()
        self.game_height = int()

    def starting_body(self, game_width, game_height):
        self.game_width = game_width
        self.game_height = game_height
        x_cord = -90
        y_cord = -((self.game_height / 2) - 30)

        for piece in range(10):
            piece = Turtle("square")
            piece.color("white")
            piece.penup()
            piece.setposition(y=y_cord, x=x_cord)
            x_cord += 20
            self.body.append(piece)

    def move_left(self):
        # move palette so last piece takes place of previous block, no gap between blocks when animated
        for piece in range((len(self.body) - 1), -1, -1):
            if self.body[0].xcor() >= -((self.game_width / 2) - 20):
                self.body[piece].backward(self.distance)
            else:
                pass
        self.screen.update()

    def move_right(self):
        # move palette so last piece takes place of previous block, no gap between blocks when animated
        for piece in range(0, (len(self.body))):
            if self.body[-1].xcor() <= (self.game_width / 2) - 30:
                self.body[piece].forward(self.distance)
            else:
                pass
        self.screen.update()
