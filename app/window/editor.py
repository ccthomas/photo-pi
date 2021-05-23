import numpy as np
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import ImageTk,Image  
from editor.tools import Brush

class Editor(object):
    def __init__(self, root, row, rowspan, column, columnspan):
        self.canvas = Canvas(root, bg='white', width=600, height=600)
        self.canvas.grid(row=row, rowspan=rowspan, column=column, columnspan=columnspan)
   