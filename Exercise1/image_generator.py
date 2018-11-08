import numpy as np
import matplotlib.pyplot as plot
import os


class ImageGenerator():

    def __init__(self, batch_size, image_size):
        self.batch_size = batch_size
        self.image_size = image_size
        self.folder = []
        self.current_batch = []
        self.currentBatchPosition = 0
        for i in range(100):
            self.folder.append(np.load('exercise_data/'+str(i)+'.npy'))



    def next(self):
        for i in range(self.batch_size):
            self.current_batch.append(self.folder[self.currentBatchPosition])
            i += 1
            self.currentBatchPosition += 1
            print(self.currentBatchPosition)
        return self.current_batch

    def show(self):
        for i in range(self.batch_size):
            plot.imshow(self.current_batch[i])
            plot.show()
            i += 1