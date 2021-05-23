from window.menu import MenuBar
from window.editor import Editor
from window.layers import LayersWindow
from editor.layer import Layer
from playground.zoom import CanvasImage
from tkinter import Tk
#from playground.zoom import CanvasImage


class Window(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    
    def __init__(self):
        self.root = Tk()
        
        # menu bar
        self.menu_bar = MenuBar(self)

        # layers
        self.layers = LayersWindow(self.root, 0,1,1,1)
        self.layers.add_layer(Layer("Background"))
        self.layers.add_layer(Layer("Layer 1"))
        self.layers.add_layer(Layer("Scribble"))

        # editor
        self.editor = Editor(self.root, 0,1,0,1)
        self.editor.set_layer_window
        #self.editor = CanvasImage(self.root, "app/resources/photo-pie.png")
        #self.editor.grid(row=0, column=0)

        # mainloop 
        self.root.mainloop()

    def add_layer(self, layer):
        self.layers.add_layer(layer)
        self.editor.draw()

    def draw():
        for layer in self.lat