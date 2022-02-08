import string


class ParametricTable:

    def __init__(self, columns, rows, title="Title", cell_width=5, cell_height=1, title_height=3):
        self.intersection = "+"
        self.horizontal_border = "-"
        self.vertical_border = "|"
        self.columns = columns
        self.rows = rows
        self.title = title
        # cell width must be odd number
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.title_height = title_height
        self.content = dict()
        self.title_cell = str()
        self.table_data = str()

    def create_title(self):
        """Creates a title field above tha table."""
        # title top border depending on number of columns and predefined cell width
        title_length = (self.columns * self.cell_width) + (self.columns - 1)
        title_top = self.intersection + (title_length * self.horizontal_border) + self.intersection + "\n"
        title_text_row = " " * int((title_length - len(self.title)) / 2) + self.title + \
                         " " * int((title_length - len(self.title)) / 2)
        title_sides = str()
        # if title height is set to higher than 1, align title in center, or one above the center in case
        # of even title height
        additional_space = str()
        if not title_length % 2:
            additional_space = " "
        # if title height is bigger than 1
        if self.title_height > 1:
            for row in range(self.title_height):
                # if height number is even, place text one above the middle
                # if height number is odd, place text in middle row
                if row == round(self.title_height / 2) - 1:
                    title_sides += \
                        self.vertical_border + additional_space + title_text_row + self.vertical_border + "\n"
                # for other rows just make borders with empty space in the middle
                else:
                    title_sides += \
                        self.vertical_border + ((len(title_top) - 3) * " ") + self.vertical_border + "\n"
        # if title height is set to one, just make single cell row
        else:
            title_sides = self.vertical_border + additional_space + title_text_row + self.vertical_border + "\n"
        self.title_cell = title_top + title_sides

    def table_content(self):
        """Generates table content depending on amount of rows and columns."""
        # generate columns names
        columns = list(string.ascii_uppercase)[0:self.columns]
        # generate rows names
        rows = list(range(self.rows))
        # fill content dictionary with (for now) empty values
        for column in columns:
            for row in rows:
                self.content[str(column) + str(row)] = ""

    def update_table_data(self):
        """Function needed after every change in table content."""
        cells_top_border = \
            self.columns * (self.intersection + self.cell_width * self.horizontal_border) + self.intersection + "\n"
        cells_bottom_border = cells_top_border
        # all rows are in single variable
        cells_row = str()
        for row in range(self.rows):
            # iterating through each column in first row (extracting keys from content dictionary
            # with leap equal to number of rows (to show only cells of current row)
            for cell in list(self.content.keys())[row::self.rows]:
                # if cell is empty its contents is equal to its width value
                if len(self.content[cell]) == 0:
                    cell_gap = " " * self.cell_width
                    cells_row += self.vertical_border + cell_gap
                # if cell has value, it's showed in the middle of the cell
                else:
                    cell_gap = " " * int((self.cell_width - len(self.content[cell])) / 2)
                    cells_row += self.vertical_border + cell_gap + self.content[cell] + cell_gap
                # for last cell in row, add last vertical border
                if cell == list(self.content.keys())[row::self.rows][-1]:
                    cells_row += self.vertical_border + "\n" + cells_bottom_border
        self.table_data = cells_top_border + cells_row

    def print_table(self):
        """Show table."""
        print(self.title_cell + self.table_data)

# EXAMPLE USAGE
# table = ParametricTable(columns=3, rows=3, title="XYZ")
# table.create_title()
# table.table_content()
# table.update_table_data()
# table.print_table()
