from tkinter import *


class Application(Frame):
    def __init__(self, parent, rows=40, columns=40, size=20, color1="white"):
        """size is the size of a square, in pixels"""

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color1
        self.pieces = {}
        self.squares = {}

        canvas_width = columns * size
        canvas_height = rows * size

        Frame.__init__(self, parent)
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                             width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        v = StringVar(master=root)
        values = {
            "1": "Start Node",
            "2": "End Node",
            "3": "Wall Node"
        }
        self.radio1 = Radiobutton(master=root, text=values["1"], variable=v,
                                  value=values["1"], indicator=0,
                                  background="light blue", command=self.set_start_node).pack(side=RIGHT)
        self.radio2 = Radiobutton(master=root, text=values["2"], variable=v,
                                  value=values["2"], indicator=0,
                                  background="light blue", command=self.set_end_note).pack(side=RIGHT)
        self.radio3 = Radiobutton(master=root, text=values["3"], variable=v,
                                  value=values["3"], indicator=0,
                                  background="light blue").pack(side=RIGHT)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def refresh(self, event):
        """Redraw the board, possibly in response to window being resized"""
        x_size = int((event.width - 1) / self.columns)
        y_size = int((event.height - 1) / self.rows)
        self.size = min(x_size, y_size)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2

    def set_start_node(self):
        row = 10
        column = 10
        x0 = (column * self.size)
        y0 = (row * self.size)
        print(x0, y0)
        x1 = x0 + self.size
        y1 = y0 + self.size
        self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="green", tags="start")

    def set_end_note(self):
        row = 20
        column = 20
        x0 = (column * self.size)
        y0 = (row * self.size)
        x1 = x0 + self.size
        y1 = y0 + self.size
        self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="red", tags="start")

    def create_walls(self):
        pass


if __name__ == "__main__":
    root = Tk()
    board = Application(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
