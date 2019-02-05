from Random import *
from math import sqrt, log

class RandomStrategy:

    def __init__(self, iterations, bandits):
        self.bandits = bandits
        self.banditsCount = len(bandits)
        self.iterations = iterations
        self.totalReward = 0

    def play(self):
        for i in range(self.iterations):
            index = randInt(0, self.banditsCount-1)
            self.totalReward += self.bandits[index].play()
        return self.totalReward, self.bandits
    
