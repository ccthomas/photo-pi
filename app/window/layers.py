from tkinter import Button, Label, Canvas, Frame, Scrollbar, BOTH, LEFT, NW, TRUE, TOP, FLAT

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
        #rows = 9
        #for i in range(0, rows):
        #    self.add_layer("Label " + str(i))
            #self.grid_system.append([])
            #row_num = len(self.grid_system) - 1
            #self.grid_system[row_num].append(Label(self.frame_buttons, text="Label" + str(i)))
            #self.grid_system[row_num][0].grid(row=row_num, column=0)
            #self.grid_system[row_num].append(Button(self.frame_buttons, text="Delete"))
            #self.grid_system[row_num][1].grid(row=row_num, column=1, sticky='news')

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        self.frame_buttons.update_idletasks()

        self.frame_canvas.config(width=200, height=100)

        # Set the canvas scrolling region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def refresh_layer(self): 
        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        self.frame_buttons.update_idletasks()
        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        #self.first5columns_width = sum([self.grid_system[0][j].winfo_width() for j in range(0, 2)])
        #self.first5rows_height = sum([self.grid_system[i][0].winfo_height() for i in range(0, 5)])
        #self.frame_canvas.config(width=200, height=100)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def add_layer(self, layer):
        self.grid_system.append([])
        row_num = len(self.grid_system) - 1
        self.grid_system[row_num].append(Button(self.frame_buttons, text=layer.display_name()))
        self.grid_system[row_num][0].grid(row=row_num, column=0)
        self.grid_system[row_num].append(Button(self.frame_buttons, text="Delete", command=lambda: self.delete_layer(row_num)))
        self.grid_system[row_num][1].grid(row=row_num, column=1, sticky='news')
        self.refresh_layer()

    def delete_layer(self, index):
        print("Delete idnex=" + str(index))
        self.grid_system[index][0].destroy()
        self.grid_system[index][1].destroy()

    def draw(self, canvas):
        for row in self.grid_system:
            

class Row(object):
    def __init__(self, row_num, layer):
        self.row_num = row_num
        self.layer = layer
        self.active = True