import numpy as np
import matplotlib.pyplot as plot

class Spectrum():
    def __init__(self, resolution):
        self.resolution = resolution
        self.output = np.ndarray

    def getIfromRGB(self, rgb=[]):
        red = rgb[0]
        print(rgb[0])
        green = rgb[1]
        blue = rgb[2]
        print(red, green, blue)
        RGBint = (red << 16) + (green << 8) + blue
        return RGBint

    def draw(self):
        # Create a 3-dim array 256 x 256 x 3. Used to divide the
        # three rgb spectrums for concatenation purposes down below.
        spectrum = np.zeros([256, 256*6, 3], dtype=np.uint8)
        spectrum[:, :, 0] = np.concatenate(
            ([255] * 256, np.linspace(255, 0, 256), [0] * 256, [0] * 256, np.linspace(0, 255, 256), [255] * 256),
            axis=0)
        spectrum[:, :, 1] = np.concatenate(
            (np.linspace(0, 255, 256), [255] * 256, [255] * 256, np.linspace(255, 0, 256), [0] * 256, [0] * 256),
            axis=0)
        spectrum[:, :, 2] = np.concatenate(
            ([0] * 256, [0] * 256, np.linspace(0, 255, 256), [255] * 256, [255] * 256, np.linspace(255, 0, 256)),
            axis=0)
        self.output = spectrum

    def show(self):
        plot.imshow(self.output)
        plot.axis('off')
        plot.show()