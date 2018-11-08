import numpy as np
import matplotlib.pyplot as plot

class Circle():

    def __init__(self, resolution, radius, positions=[]):
        self.resolution = resolution
        self.radius = radius
        self.positions = positions
        self.output = np.ndarray

    def draw(self):
        t = np.arange(0,2*np.pi, .01)
        y = self.radius*np.cos(t)
        x = self.radius*np.sin(t)
        plot.plot(x, y)

    def show(self):
        plot.show()

