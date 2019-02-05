from Random import *
from math import sqrt, log

class UCB:

    def __init__(self, iterations, bandits, epsilon=0.05):
        self.bandits = bandits
        self.banditsCount = len(bandits)
        self.iterations = iterations
        self.totalReward = 0
        self.empiricalMeans = [0]*self.banditsCount
        self.upperBounds = [0]*self.banditsCount
        self.epsilon=epsilon

    def play(self):
        self.initialize()
        for index in range(self.iterations-self.banditsCount):
            index = self.upperBounds.index(max(self.upperBounds))
            reward = self.bandits[index].play()
            self.totalReward += reward
            #Mn = Mn-1 * (n-1)/n + Xn/n
            self.empiricalMeans[index][0] = self. empiricalMeans[index][0] * ((self.empiricalMeans[index][1]-1) / \
                                                                            self.empiricalMeans[index][1]) + reward / \
                                                                            self. empiricalMeans[index][1]
            self.empiricalMeans[index][1] += 1           
            self.upperBounds[index] = self.empiricalMeans[index][0] + \
                sqrt(log(1/self.epsilon)/(2 * self.empiricalMeans[index][1]))
        return self.totalReward, self.bandits

    def initialize(self):
        for index in range(self.banditsCount):
            reward = self.bandits[index].play()
            self.totalReward += reward
            self.empiricalMeans[index] = [reward, 1]
            self.upperBounds[index] = self.empiricalMeans[index][0] + \
                sqrt(log(1/self.epsilon)/(2*self.empiricalMeans[index][1]))