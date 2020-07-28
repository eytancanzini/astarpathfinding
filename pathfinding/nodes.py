class HomeNode:
    def __init__(self, _row_, _column_):
        if _row_ < 0 and _column_ < 0:
            self.row = None
            self.column = None
        self.row = _row_
        self.column = _row_

    def change_pos(self, new_row, new_column):
        self.row = new_row
        self.column = new_column

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column


class ExitNode:
    def __init__(self, _row_, _column_):
        self.row = _row_
        self.column = _column_

    def change_pos(self, new_row, new_column):
        self.row = new_row
        self.column = new_column

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column
