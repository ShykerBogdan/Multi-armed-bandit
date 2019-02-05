# Shyker Bogdan
from Bandit import Bandit
from Strategies.Eps_Greedy import Eps_Greeedy
from Strategies.UCB import UCB
from Strategies.RandomStrategy import RandomStrategy
from operator import attrgetter


def UseEpsGreedy(bandits):
    eps_greedy = Eps_Greeedy(gamesCount, bandits, 0.005)
    game = eps_greedy.play()
    obj = max(game[1], key=attrgetter('totalReward'))
    summery('Eps_Greedy', game, obj)


def UseUCB(bandits):
    ucb = UCB(gamesCount, bandits, 0.05)
    game = ucb.play()
    obj = max(game[1], key=attrgetter('totalReward'))
    summery('UBC', game, obj)


def useRandom(bandits):
    randomSt = RandomStrategy(gamesCount, bandits)
    game = randomSt.play()
    obj = max(game[1], key=attrgetter('totalReward'))
    summery('Random', game, obj)


def summery(name, game, obj):
    print(f'{name} method results')
    print(
        f"Total reward: {game[0]}\nIndex of best Bandit: {game[1].index(obj)}\nBest bandit's reward: {obj.totalReward}")
    print('='*40)


if __name__ == "__main__":
    gamesCount = 2000
    banditsCount = 500

    for i in range(10):
        bandits = [Bandit(-1, 1, -2, 2) for bandit in range(banditsCount)]
        UseEpsGreedy(bandits)
        UseUCB(bandits)
        useRandom(bandits)
