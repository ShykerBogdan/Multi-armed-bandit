from Random import *
from math import exp


class Bandit:

    def __init__(self, muMin, muMax, sigmaMin, sigmaMax):
        self.mu = rand(muMin, muMax)
        self.sigma = rand(sigmaMin, sigmaMax)
        self.totalReward = 0

    def play(self):
        reward = self.genNormalDistribution(self.mu, self.sigma)
        self.totalReward += reward
        return reward

    def genNormalDistribution(self, mu, sigma):
        """
        mu: expectation
        sigma: variance
        Returns list
        """
        x = 0
        while True:
            u = rand(0.0, 1.0)
            x = rand(mu - 5*sigma, mu + 5*sigma)
            if u < exp((-(x-mu)**2)/(2*(sigma**2))):
                break
        return x
