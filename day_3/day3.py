import os

def part1():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data.txt'), "r") as file:
        s = 0
        for rs in file.read().splitlines():
            c = list(set(rs[:int(len(rs)/2)]).intersection(set(rs[int(len(rs)/2):])))
            s += ord(c[0].lower()) - 96 + 26 if c[0].isupper() else ord(c[0]) - 96
        return s



print(part1())