class Layer(object):

    DISPLAY_NAME_LENGTH = 10
    
    def _init__(self, name):
        self.name = name
        self.opacity = 100
        self.active = True
        self.image = None
        self.history = []
        self.undid = []
    
    def set_image(self, image):
        self.image = image
    
    def display_name(self):
        return self.name[:self.DISPLAY_NAME_LENGTH]

    def add_to_history(self, edges):
        self.history.append(edges)

    def undo(self):
        if len(self.history) > 0:
            self.undid.append(self.history.pop())

    def redo(self):
        if len(self.undid) > 0:
            self.history.append(self.undid.pop())

    def draw(self, canvas):
        if self.active:
            for edges in self.history:
                for edge in edges:
                    edge.draw(canvas)
