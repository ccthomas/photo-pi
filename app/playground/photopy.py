import numpy as np
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import ImageTk,Image  
from editor.tools import Brush

class Editor(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    # Global Var for image so garbage collector does not remove it
    BASE_IMAGE = None

    def __init__(self):
        self.root = Tk()

        # Import
        self.import_button = Button(self.root, text="Import", command=self.menu_import)
        self.import_button.grid(row = 0, column = 0)

        # Export
        self.export_button = Button(self.root, text="Export", command=self.menu_export)
        self.export_button.grid(row = 0, column = 1)

        # Open
        self.open_button = Button(self.root, text="Open", command=self.menu_open)
        self.open_button.grid(row = 0, column = 2)

        # Save
        self.save_button = Button(self.root, text="Save", command=self.menu_save)
        self.save_button.grid(row = 0, column = 3)

        # Undo
        self.undo_button = Button(self.root, text="Undo", command=self.menu_undo)
        self.undo_button.grid(row = 0, column = 4)

        # Redo
        self.redo_button = Button(self.root, text="Redo", command=self.menu_redo)
        self.redo_button.grid(row = 0, column = 5)
    
        # brush
        self.brush_button = Button(self.root, text='Brush', command=self.menu_brush)
        self.brush_button.grid(row=0, column=6)

        # eraser
        self.eraser_button = Button(self.root, text='Eraser', command=self.menu_eraser)
        self.eraser_button.grid(row=0, column=7)

        # Color
        self.color_button = Button(self.root, text="Color", command=self.menu_color)
        self.color_button.grid(row = 0, column = 8)

        # Line Width
        self.line_width_button = Scale(self.root, from_=1, to=100, orient=HORIZONTAL)
        self.line_width_button.grid(row = 0, column = 9)

        # Set Canvas
        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=10)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.line_width_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.brush_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.history = {}
        self.undid = {}
        self.history_index = 0
        self.history[self.history_index] = []

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        if len(self.undid) > 0:
            self.undid.clear()
        
        self.line_width = self.line_width_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            line = Brush(self.old_x, self.old_y, event.x, event.y, self.line_width, paint_color)
            line.draw(self.c)
            self.history[self.history_index].append(line)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.history_index = self.history_index + 1
        self.history[self.history_index] = []

        self.old_x, self.old_y = None, None

    def menu_brush(self):
        print('Brush Button pressed')
        self.activate_button(self.brush_button)

    def menu_color(self):
        print('Color Button pressed')
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def menu_eraser(self):
        print('Eraser Button pressed')
        self.activate_button(self.eraser_button, eraser_mode=True)

    def menu_export(self):
        print('Export Button pressed')
        export = []
        for history in self.history.values():
            for line in history:
                export.append(line.export())
        print(export)
        with open('example.phpy', 'w') as fp:
            for t in export:
                fp.write(' '.join(str(s) for s in t) + '\n')

    def menu_import(self):
        print('Import Button pressed')
        global BASE_IMAGE
        path=filedialog.askopenfilename(filetypes=[("Image File",'.png')])
        if len(path) == 0:
            return
        BASE_IMAGE = ImageTk.PhotoImage(file=path)
        self.c.create_image(20,20, anchor=NW, image=BASE_IMAGE)

    def menu_open(self):
        print('Open Button pressed')
        pass

    def menu_redo(self):
        print('Redo Button pressed')
        if self.history_index in self.undid and len(self.undid[self.history_index]) > 0:
            undid_index = self.history_index
            history_index = self.history_index + 1
            self.history[history_index] = []

            for line in self.undid[undid_index]:
                line.draw(self.c)
                self.history[self.history_index].append(line)
            self.undid[undid_index].clear
            self.history_index = history_index

    def menu_save(self):
        print('Save Button pressed')
        pass

    def menu_undo(self):
        print('Undo Button pressed')
        self.history_index = self.history_index - 1
        if self.history_index in self.history:
            self.undid[self.history_index] = []
        
            for line in self.history[self.history_index]:
                self.undid[self.history_index].append(line)
                self.c.delete(line.id)
        else:  
            self.history_index = self.history_index + 1
        self.history[self.history_index] = []