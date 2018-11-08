import numpy as np
import matplotlib.pyplot as plot

class Checker():

    def __init__(self, resolution, tile_size, gridsize):
        self.gridsize = gridsize
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = np.ndarray

    def draw(self):
        grid = np.ndarray(shape=(self.gridsize, self.gridsize))
        for row in range(self.gridsize):
            for col in range(self.gridsize):
                if col % 2 == 0 and row % 2 == 0:
                    grid[row][col] = 0
                elif col % 2 == 0 and row % 2 != 0:
                    grid[row][col] = 1
                elif col % 2 != 0 and row % 2 == 0:
                    grid[row][col] = 1
                else:
                    grid[row][col] = 0
        self.output = grid

    def show(self):
        fig, ax = plot.subplots()
        ax.imshow(self.output, cmap=plot.cm.gray, interpolation='nearest')
        plot.show()
