import os

def part1():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt'), "r") as file:
        score = 0
        for line in file.read().splitlines():
            pair = ([list(map(int, sec.split('-'))) for sec in line.split(',')]) 
            for i, s in enumerate(pair):
                pair[i] = set(range(s[0], s[1] + 1))
            if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
                score += 1
        return score


print(part1())

