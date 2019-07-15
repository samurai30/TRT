import numpy as num
import matplotlib.pyplot as plot

INSIDE = "0000"
LEFT = "0001"
RIGHT = "0010"
BOTTOM = "0100"
TOP = "1000"


class Initial:
    x_max = 0
    y_max = 0
    x_min = 0
    y_min = 0

    def init_points(self,xmax,ymax,xmin,ymin):
        self.x_max = xmax
        self.y_max = ymax
        self.x_min = xmin
        self.y_min = ymin


def bitWise(code, side):
    result = []

    for i in range(len(code)):
        result.append(int(side[i]) | int(code[i]))
    return result


a = Initial()
a.init_points(int(input("X_MAX")), int(input("Y_MAX")), int(input("X_MIN")), int(input("Y_MIN")))


# Function to compute region code for a point(x,y)
def getZone(x, y):
    code = INSIDE
    result = []
    if x < a.x_min:
        result = bitWise(code, LEFT)
        code = str("".join(map(str, result)))
        print(code)
    elif x > a.x_max:
        result = bitWise(code, RIGHT)
        code = str("".join(map(str, result)))
        print(code)
    if y < a.y_min:
        result = bitWise(code, BOTTOM)
        code = str("".join(map(str, result)))
    elif y > a.y_max:
        result = bitWise(code, TOP)
        code = str("".join(map(str, result)))
    return result


print(getZone(int(input("X CORD")), int(input("Y CORD"))))



