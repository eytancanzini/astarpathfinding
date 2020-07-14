import tkinter as tk

def create_grid(event=None):
    w = c.winfo_width()
    h = c.winfo_width()
    d.delete('grid_line')

    for i in range(0, w, 100):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    for i in range(0, h, 100):
        c.create_line([(0,i), (w, i)], tag='grid_line')

root = tk.Tk()

c = tk.Canvas(root, height=1000, width=1000, big='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Congigure>', create_grid)

root.mainloop()