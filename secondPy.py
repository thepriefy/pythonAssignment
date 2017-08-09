class Shape:
    color = None
    filled = None

    def __init__(self):
        global color
        color = 'red'
        global filled
        filled = True

    def Shape(self, input_color, input_filled):
        global color
        global filled
        color = input_color
        filled = input_filled

    def getColor(self):
        global color
        print(color)

    def setColor(self, input_color):
        global color
        color = input_color

    def isFilled(self):
        global filled
        print(filled)

    def setFilled(self, input_filled):
        global filled
        filled = input_filled
