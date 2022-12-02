import os

# A = rock
# B = paper
# C = scissors

# Y = lose
# X = rock
# Z = scissors

def part1():
    # paths
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'data.txt')

    player1 = []
    player2 = []

    # load data
    with open(filename, 'r') as file:
        single_inventory = []
        for x in file.read().splitlines():
            if x[0] == 'A':
                x1 = 1
            elif x[0] == 'B':
                x1 = 2
            elif x[0] == 'C':
                x1 = 3
            if x[2] == 'X':
                x2 = 1
            elif x[2] == 'Y':
                x2 = 2
            elif x[2] == 'Z':
                x2 = 3

            if x1 == x2:
                player2.append(x2 + 3)
            elif x1 == 1 and x2 == 3:
                player2.append(x2)
            elif x1 == 1 and x2 == 2:
                player2.append(x2 + 6)
            elif x1 == 2 and x2 == 1:
                player2.append(x2)
            elif x1 == 2 and x2 == 3:
                player2.append(x2 + 6)
            elif x1 == 3 and x2 == 1:
                player2.append(x2 + 6)
            elif x1 == 3 and x2 == 2:
                player2.append(x2)

    return sum(player2)


def part2():
    # paths
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'data.txt')

    player1 = []
    player2 = []

    # load data
    with open(filename, 'r') as file:
        single_inventory = []
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