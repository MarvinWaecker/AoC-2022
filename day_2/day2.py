import os

# A = rock
# B = paper
# C = scissors

# Y = paper
# X = rock
# Z = scissors

def part1():
    # paths
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'data.txt')

    player1 = []
    player2 = []

    # load data
    max_cals = 0
    with open(filename, 'r') as file:
        single_inventory = []
        for x in file.read().splitlines():
            if x[0] == 'A':
                x1 = 1
            elif x[0] == 'B':
                x1 = 2
            elif x[0] == 'C':
                x1 = 3
            if x[2] == 'Y':
                x2 = 2
            elif x[2] == 'X':
                x2 = 1
            elif x[2] == 'Z':
                x2 = 3

            if x1 == x2:
                player1.append(x1 + 3)
                player2.append(x2 + 3)
            elif x1 == 1 and x2 == 3:
                player1.append(x1 + 6)
                player2.append(x2)
            elif x1 == 1 and x2 == 2:
                player1.append(x1)
                player2.append(x2 + 6)
            elif x1 == 2 and x2 == 1:
                player1.append(x1 + 6)
                player2.append(x2)
            elif x1 == 2 and x2 == 3:
                player1.append(x1)
                player2.append(x2 + 6)
            elif x1 == 3 and x2 == 1:
                player1.append(x1)
                player2.append(x2 + 6)
            elif x1 == 3 and x2 == 2:
                player1.append(x1 + 6)
                player2.append(x2)

    return sum(player2)


def part2():
    # paths
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'data.txt')

    player1 = []
    player2 = []

    # load data
    max_cals = 0
    with open(filename, 'r') as file:
        single_inventory = []
        for x in file.read().splitlines():
            if x[0] == 'A':
                x1 = 1
            elif x[0] == 'B':
                x1 = 2
            elif x[0] == 'C':
                x1 = 3
            if x[2] == 'Y':
                x2 = 2
            elif x[2] == 'X':
                x2 = 1
            elif x[2] == 'Z':
                x2 = 3

            if x1 == x2:
                player1.append(x1 + 3)
                player2.append(x2 + 3)
            elif x1 == 1 and x2 == 3:
                player1.append(x1 + 6)
                player2.append(x2)
            elif x1 == 1 and x2 == 2:
                player1.append(x1)
                player2.append(x2 + 6)
            elif x1 == 2 and x2 == 1:
                player1.append(x1 + 6)
                player2.append(x2)
            elif x1 == 2 and x2 == 3:
                player1.append(x1)
                player2.append(x2 + 6)
            elif x1 == 3 and x2 == 1:
                player1.append(x1)
                player2.append(x2 + 6)
            elif x1 == 3 and x2 == 2:
                player1.append(x1 + 6)
                player2.append(x2)

    return sum(player2)

print(part1())
print(part2())