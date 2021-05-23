from tkinter import Menu
from window.layer import Layer
from tkinter import filedialog
from PIL import ImageTk,Image  
from tkinter import simpledialog

class MenuBar(object):
    def __init__(self, main_window):
        # save root to call back to
        self.main_window = main_window

        # create menu
        menu = Menu(main_window.root)
        main_window.root.config(menu=menu)

        # file menu items
        file = Menu(menu)
        file.add_command(label="New", command=self.menu_new)
        file.add_command(label="Open", command=self.menu_open)
        file.add_command(label="Save", command=self.menu_save)
        file.add_command(label="Import", command=self.menu_import)
        file.add_command(label="Export", command=self.menu_export)
        file.add_command(label="Exit", command=self.menu_exit)

        # edit menu items
        edit = Menu(menu)
        edit.add_command(label="Undo", command=self.menu_undo)
        edit.add_command(label="Redo", command=self.menu_redo)

        # construct menu
        menu.add_cascade(label="File", menu=file)
        menu.add_cascade(label="Edit", menu=edit)

    def menu_exit(self):
        exit()
    
    def menu_export(self):
        print('TODO Export pressed')
    
    def menu_import(self):
        path=filedialog.askopenfilename(filetypes=[("Image File",'.png')])
        if len(path) == 0:
            return

        import re
        name = re.findall("(\S)+(\.png)", path)
        layer = Layer(name)
        layer.set_image(ImageTk.PhotoImage(file=path))
        self.add_layer(layer)

    def menu_new(self):
        print('TODO New Pressed')
        width = ""
        while len(width) == 0 or not width.isdigit():
            width = simpledialog.askstring(title="Test", prompt="Width:")
        height = ""
        while len(height) == 0 or not height.isdigit():
            height = simpledialog.askstring(title="Test", prompt="Height:")
        print(width, "x", height)
        
    
    def menu_open(self):
        print('TODO Open pressed')

    def menu_redo(self):
        print('TODO Redo pressed')

    def menu_save(self):
        print('TODO Save pressed')

    def menu_undo(self):
        print('TODO Undo pressed')