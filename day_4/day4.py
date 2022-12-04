import os

def part1and2():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt'), "r") as file:
        score1 = 0
        score2 = 0
        for line in file.read().splitlines():
            pair = ([list(map(int, sec.split('-'))) for sec in line.split(',')]) 
            for i, s in enumerate(pair):
                pair[i] = set(range(s[0], s[1] + 1))
            if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
                score1 += 1
            if bool(set(pair[0]) & set(pair[1])):
                score2 += 1
        return score1, score2


print(part1and2())

