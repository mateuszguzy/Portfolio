from turtle import Screen
from board import Board
from blocks import Blocks
from ball import Ball
import time

# ------ CONSTANTS
GAME_WIDTH = 800
GAME_HEIGHT = 600

screen = Screen()
screen.tracer(0)
board = Board()
blocks = Blocks()
ball = Ball(GAME_WIDTH, GAME_HEIGHT)
blocks.create_rows(GAME_WIDTH, GAME_HEIGHT)
screen.listen()
screen.onkey(board.move_left, "a")
screen.onkey(board.move_right, "d")
screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
screen.bgcolor("black")
screen.title("BREAKOUT")
board.starting_body(GAME_WIDTH, GAME_HEIGHT)
screen.update()


# TODO-010 game window with separated top area for score
# TODO-020 board.py class in separate file
# TODO-030 blocks class in separate file
# TODO-040 ball class in separate file


def main():
    time.sleep(3)
    game_is_on = True
    while game_is_on:
        ball.move()
        # if ball.ycor() >= 20:
        #     print(ball.position())
        #     for block in blocks.row_blocks[:blocks.number_of_blocks_in_line]:
        #         for square in block:
        #             if ball.distance(square) <= 22:
        #                 print(len(blocks.row_blocks))
        #                 blocks.delete_block(blocks.row_blocks.index(block))
        #                 print(len(blocks.row_blocks))
        #     ball.top_boundary_reflection()
        # print(ball.position())
        if ball.ycor() >= 35:
            for block in blocks.row_blocks[:blocks.number_of_blocks_in_line]:
                for square in block:
                    if ball.distance(square) <= 20:
                        # print(type(blocks.row_blocks[blocks.row_blocks.index(block)]))
                        # print(blocks.row_blocks[blocks.row_blocks.index(block)])
                        # print(f"index: {blocks.row_blocks.index(block)}")
                        # print(len(blocks.row_blocks))
                        blocks.delete_block(blocks.row_blocks.index(block))
                        # print(len(blocks.row_blocks))
                        ball.top_boundary_reflection()
        if ball.bottom_boundary < ball.ycor() <= ball.bottom_boundary + 50:
            for part in board.body:
                if ball.distance(part) <= 20:
                    ball.board_reflection(board.body.index(part))
        elif ball.ycor() >= ball.top_boundary:
            ball.top_boundary_reflection()
        elif ball.xcor() <= ball.left_boundary or ball.right_boundary <= ball.xcor():
            ball.side_boundary_reflection()

        elif ball.ycor() <= ball.bottom_boundary:
            game_is_on = False



if __name__ == "__main__":
    main()

screen.exitonclick()
