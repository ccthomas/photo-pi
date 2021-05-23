from tkinter import Canvas

class EditorV1(object):
    def __init__(self, root, row, rowspan, column, columnspan):
        self.canvas = Canvas(root, bg='white', width=600, height=600)
        self.canvas.grid(row=row, rowspan=rowspan, column=column, columnspan=columnspan)