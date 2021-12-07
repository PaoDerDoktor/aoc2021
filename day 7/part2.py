from collections import Counter
from sys import maxsize

def day7_part2_main():
    with open("day 7/inputs.txt", 'r') as inFile:
        positions: list[int] = [int(_) for _ in inFile.readline().split(',')]
        
        minPos: int = -1
        minAmount: int = maxsize
        for position in range(min(positions), max(positions)):
            fuel: int = sum([sum([_ for _ in range(abs(position-i)+1)]) for i in positions])
            if minAmount > fuel:
                minAmount = fuel
                minPos    = position
            
        return minAmount

if __name__ == '__main__':
    print(day7_part2_main())