from Random import *
from math import sqrt, log


class Eps_Greeedy:

    def __init__(self, iterations, bandits, epsilon=0.05):
        self.bandits = bandits
        self.banditsCount = len(bandits)
        self.iterations = iterations
        self.epsilon = epsilon
        self.totalReward = 0
        self.empiricalMeans = [[0]*self.banditsCount, [0]*self.banditsCount]

    def play(self):
        self.initialize()
        for i in range(self.iterations-self.banditsCount):
            p = rand(0, 1)
            if p < 1 - self.epsilon:
                index = self.empiricalMeans[0].index(max(self.empiricalMeans[0]))
            else:
                index = self.empiricalMeans[0].index(max(self.empiricalMeans[0]))
                indexEmpMax = index
                while index == indexEmpMax:
                    index = randInt(0, self.banditsCount-1)
            self.playBandit(index)
        return self.totalReward, self.bandits

    def initialize(self):
        for index in range(self.banditsCount):
            reward = self.bandits[index].play()
            self.totalReward += reward
            self.empiricalMeans[0][index], self.empiricalMeans[1][index] = reward, 1

    def playBandit(self, index):
        reward = self.bandits[index].play()
        self.totalReward += reward
        #Mn = Mn-1 * (n-1)/n + Xn/n
        self.empiricalMeans[0][index] = self.empiricalMeans[0][index] * ((self.empiricalMeans[1][index]-1) / self.empiricalMeans[1][index]) \
            + reward / self.empiricalMeans[1][index]
        self.empiricalMeans[1][index] += 1
