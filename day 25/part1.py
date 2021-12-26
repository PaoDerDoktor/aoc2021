from copy import deepcopy

def step(map: list[list[str]]) -> tuple[bool, list[list[str]]]:
    mapCopy = deepcopy(map)
    moved: bool = False
    for lineId, line in enumerate(map):
        for eId, e in enumerate(line):
            if e == '.' or e == 'v':
                continue
            next: int = eId+1
            if next >= len(line):
                next = 0
            if line[next] == '.':
                mapCopy[lineId][next] = '>'
                mapCopy[lineId][eId]  = '.'
                moved                 = True
    
    verticalMapCopy = deepcopy(mapCopy)
    for lineId, line in enumerate(mapCopy):
        for eId, e in enumerate(line):
            if e == '.' or e == '>':
                continue
            next: int = lineId+1
            if next >= len(mapCopy):
                next = 0
            if mapCopy[next][eId] == '.':
                verticalMapCopy[lineId][eId] = '.'
                verticalMapCopy[next][eId] = 'v'
                moved              = True
    return moved, verticalMapCopy

def day25_part1_main():
    with open("day 25/inputs.txt", 'r') as inFile:
        map: list[list[str]] = [[e for e in line.strip()] for line in inFile.readlines()]
        moved: bool = True
        steps: int = 0
        
        while moved:
            moved, map = step(map)
            steps += 1
            
        return steps
        
if __name__ == "__main__":
    print(day25_part1_main())