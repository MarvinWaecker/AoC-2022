import os

def part1():
    # paths
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'data.txt')

    # load data
    max_cals = 0
    with open(filename, 'r') as file:
        single_inventory = []
        for x in file.read().splitlines():
            if x != '':
                single_inventory.append(int(x))
            else:
                if sum(single_inventory) > max_cals:
                    max_cals = sum(single_inventory)
                single_inventory = []
        if single_inventory:
            if sum(single_inventory) > max_cals:
                max_cals = sum(single_inventory)
    return max_cals

def part2():
    # paths
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'data.txt')

    # load data
    cals = []
    with open(filename, 'r') as file:
        single_inventory = []
        for x in file.read().splitlines():
            if x != '':
                single_inventory.append(int(x))
            else:
                cals.append(sum(single_inventory))
                single_inventory = []
        if single_inventory:
            cals.append(sum(single_inventory))
    
    #First Highest value: 
    max_cals = []
    max_cals.append((max(cals)))
    cals.remove(max(cals))

    #output: 43

    # Second Highest value:
    max_cals.append((max(cals)))
    cals.remove(max(cals))

    #output: 9
        
            
    # Third Highest Value:
    max_cals.append((max(cals)))

    return sum(max_cals)


print(part1())
print(part2())