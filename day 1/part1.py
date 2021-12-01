from typing import List

def day1_part1_main():
    with open("day 1/inputs.txt", 'r') as inFile:
        sweeps: List[int] = [int(_) for _ in inFile.readlines()]
        
        incCount: int = 0
        for sweepIndex in range(1, len(sweeps)):
            if sweeps[sweepIndex] > sweeps[sweepIndex-1]:
                incCount+=1
        
        return incCount

if __name__ == "__main__":
    print(day1_part1_main())