from turtle import Turtle, Screen
import random
import time


class Ball(Turtle):
    def __init__(self, game_width, game_height):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # designate ball speed
        self.speed = 0.001
        self.movement_distance = 5
        self.screen = Screen()
        self.setposition(x=0, y=-250)
        self.left_boundary = -(game_width / 2) + 10
        self.right_boundary = (game_width / 2) - 15
        self.top_boundary = (game_height / 2) - 10
        self.bottom_boundary = (-game_height / 2) + 20
        self.direction = random.randint(45, 135)
        # precise angle used for debugging
        # self.direction = 95
        self.setheading(self.direction)

    def move(self):
        self.forward(self.movement_distance)
        time.sleep(self.speed)
        self.screen.update()

    # both reflections from boundary and palette are calculated to have same angle as when approaching
    def board_reflection(self, index):
        # reflection angle depends on ball current heading
        if index == 0 or index == 1:
            self.setheading(160)
        elif index == 2 or index == 3:
            self.setheading(135)
        elif index == 4:
            self.setheading(110)
        elif index == 5:
            self.setheading(70)
        elif index == 6 or index == 7:
            self.setheading(45)
        else:
            self.setheading(20)


        # if 180 <= self.heading() <= 270:
        #     self.setheading(abs(self.heading() - 180 + extra_angle))
        # elif 270 < self.heading() <= 360:
        #     self.setheading(abs(90 - (self.heading() - 270) - extra_angle))

    def side_boundary_reflection(self):
        # reflection angle depends on ball current heading
        if 0 < self.heading() <= 90:
            self.setheading(180 - self.heading())
            pass
        elif 90 < self.heading() <= 180:
            self.setheading(180 - self.heading())
            pass
        elif 180 < self.heading() <= 270:
            self.setheading(270 + (270 - self.heading()))
            pass
        elif 270 < self.heading() <= 360:
            self.setheading(self.heading() - 90)
            pass

    def top_boundary_reflection(self):
        # reflection angle depends on ball current heading
        if 0 < self.heading() <= 90:
            self.setheading(270 + (90 - self.heading()))
            pass
        elif 90 < self.heading() <= 180:
            self.setheading(270 - (self.heading() - 90))
            pass

