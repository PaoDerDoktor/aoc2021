from collections import Counter
from sys import maxsize

def day7_part1_main():
    with open("day 7/inputs.txt", 'r') as inFile:
        positions: list[int] = [int(_) for _ in inFile.readline().split(',')]
        
        minAmount: int = maxsize
        for position in positions:
            fuel: int = sum([abs(position - i) for i in positions])
            if minAmount > fuel:
                minAmount = fuel
            
        return minAmount

if __name__ == '__main__':
    print(day7_part1_main())