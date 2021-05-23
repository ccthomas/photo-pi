class Layer(object):

    DISPLAY_NAME_LENGTH = 10

    def __init__(self, name):
        self.name = name
        self.opacity = 100
        self.image = None
        self.history = {}
        self.history_index = 0
    
    def display_name(self):
        return self.name[:self.DISPLAY_NAME_LENGTH]