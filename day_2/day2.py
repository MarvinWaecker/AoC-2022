import os
import pandas as pd

# A = rock
# B = paper
# C = scissors

# Y = lose
# X = rock
# Z = scissors

#    A  B  C
# X  4  1  7
# Y  8  5  2
# Z  3  9  6


def part1():
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    m = pd.DataFrame([[4,1,7],[8,5,2],[3,9,6]], index=['X','Y','Z'], columns=['A','B','C'])
    with open(filename, 'r') as file:
        return sum([m[x[0]][x[2]] for x in file.read().splitlines()])


def part2():
    # paths
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'data.txt')

    player2 = []

    # load data
    with open(filename, 'r') as file:
        for x in file.read().splitlines():
            if x[0] == 'A':
                x1 = 'rock' # 3
            elif x[0] == 'B':
                x1 = 'paper' # 2
            elif x[0] == 'C':
                x1 = 'scissors' # 1
            if x[2] == 'X':
                strat = 'lose'
            elif x[2] == 'Y':
                strat = 'draw'
            elif x[2] == 'Z':
                strat = 'win'

            if strat == 'lose' and x1 == 'rock':
                player2.append(3) # scissors
            elif strat == 'lose' and x1 == 'paper':
                player2.append(1) # rock
            elif strat == 'lose' and x1 == 'scissors':
                player2.append(2) # paper
            if strat == 'draw' and x1 == 'rock':
                player2.append(1+3) # rock
            elif strat == 'draw' and x1 == 'paper':
                player2.append(2+3) # paper
            elif strat == 'draw' and x1 == 'scissors':
                player2.append(3+3) # scissors
            if strat == 'win' and x1 == 'rock':
                player2.append(2+6) # paper
            elif strat == 'win' and x1 == 'paper':
                player2.append(3+6) # scissors
            elif strat == 'win' and x1 == 'scissors':
                player2.append(1+6) # rock

    return sum(player2)

print(part1())  # 14375
print(part2())  # 10274