class Shape:
    color = 'red'
    filled = True

    def __init__(self, input_color, input_filled):
        global color
        global filled

        if input_color:
            color = input_color

        if input_filled:
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
