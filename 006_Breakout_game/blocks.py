from turtle import Turtle
from turtle import Screen

# ------ CONSTANTS
# --- COLORS
COLORS = ["yellow", "yellow", "green", "green", "orange", "orange", "red", "red"]


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.block_body = list()
        self.game_width = int()
        self.game_height = int()
        self.number_of_blocks_in_line = int()
        self.row_blocks = list()

    def create_rows(self, game_width, game_height):
        self.game_width = game_width
        self.game_height = game_height
        self.number_of_blocks_in_line = int(self.game_width / 45)
        y_cord = 40
        for k in range(8):
            x_cord = -(self.game_width / 2) + 20
            for i in range(self.number_of_blocks_in_line):
                block = list()
                for piece in range(2):
                    piece = Turtle()
                    piece.penup()
                    piece.shape("square")
                    piece.color(COLORS[k])
                    piece.goto(x=x_cord, y=y_cord)
                    block.append(piece)
                    x_cord += 20
                self.row_blocks.append(block)
                all_blocks_width = self.number_of_blocks_in_line * 40
                borders = 20
                block_spaces = self.number_of_blocks_in_line - 1
                x_cord += int(((self.game_width - all_blocks_width) - borders) / block_spaces)
            y_cord += 25

    def delete_block(self, index):
        for piece in self.row_blocks[index]:
            piece.hideturtle()
        print("inside")
        self.row_blocks.pop(index)
        self.screen.update()












