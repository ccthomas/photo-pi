from tkinter import Button, Label, Canvas, Frame, Scrollbar, BOTH, LEFT, NW, TRUE, TOP, FLAT
from editor.layer import Layer

class LayersWindow(object):
    def __init__(self, root, row, rowspan, column, columnspan):
        # Create a frame for the canvas with non-zero row&column weights
        self.frame_canvas = Frame(root)
        self.frame_canvas.grid(row=0, column=1, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        self.frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        self.canvas = Canvas(self.frame_canvas, bg="yellow")
        self.canvas.grid(row=0, column=0, sticky="news")
        
        # Link a scrollbar to the canvas
        self.vsb = Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # Create a frame to contain the buttons
        self.frame_buttons = Frame(self.canvas, bg="blue")
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor='nw')

        # Add 9-by-5 buttons to the frame
        self.grid_system = []
        rows = 9
        for i in range(0, rows):
            self.grid_system.append([])
            self.grid_system[i].append(Label(self.frame_buttons, text="Label"))
            self.grid_system[i][0].grid(row=i, column=0)
            self.grid_system[i].append(Button(self.frame_buttons, text=("%d,%d" % (i+1, 1+1))))
            self.grid_system[i][1].grid(row=i, column=1, sticky='news')

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        self.frame_buttons.update_idletasks()

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        self.first5columns_width = Layer.DISPLAY_NAME_LENGTH * 10
        self.first5rows_height = Layer.DISPLAY_NAME_LENGTH * 50
        self.frame_canvas.config(width=self.first5columns_width + self.vsb.winfo_width(),
                            height=self.first5rows_height)

        # Set the canvas scrolling region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def add_layer(self, layer):
        self.grid_system.append([])
        row = len(self.grid_system)
        self.grid_system[row].append(Label(self.frame_buttons, text=layer.display_name()))
        self.grid_system[row][0].grid(row=row, column=0)
        self.grid_system[row].append(Button(self.frame_buttons, text=layer.name))
        self.grid_system[row][1].grid(row=row, column=1, sticky='news')
        