from tkinter import ROUND, TRUE

class Brush(object):
    def __init__(self, x0, y0, x1, y1, width, color):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.color = color

    def draw(self, canvas):
        self.id = canvas.create_line(self.x0, self.y0, self.x1, self.y1,
                               width=self.width, fill=self.color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
    
    def export_tuple(self):
        return ("brush", self.x0, self.y0, self.x1, self.y1, self.width, self.color)

    def undo(self, canvas):
        canvas.delete(self.id)