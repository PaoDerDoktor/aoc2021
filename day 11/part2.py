from typing import NoReturn


Point = tuple[int, int]
Grid = list[list[int]]

ADJACENTS: set[Point] = {(i, j) for i in range(-1,2) for j in range(-1,2)} - {(0,0)}

def increment(grid: Grid) -> list[Point]:
    flashers: list[Point] = []
    for lineID, line in enumerate(grid):
        for colID, col in enumerate(line):
            line[colID] += 1
            if line[colID] > 9:
                flashers.append((colID, lineID))
    return flashers

def flash(grid: Grid, flashers: list[Point]) -> int:
    flashesCount: int = 0
    while len(flashers) > 0:
        flashesCount += len(flashers)
        nextFlashers: list[Point] = []
        for flasher in flashers:
            grid[flasher[1]][flasher[0]] = 0
            for adjacent in ADJACENTS:
                if (0 <= flasher[1]+adjacent[1] < 10 and 0 <= flasher[0]+adjacent[0] < 10
                    and grid[flasher[1]+adjacent[1]][flasher[0]+adjacent[0]] != 0):
                    grid[flasher[1]+adjacent[1]][flasher[0]+adjacent[0]] += 1
                    if (grid[flasher[1]+adjacent[1]][flasher[0]+adjacent[0]] > 9
                        and not (flasher[0]+adjacent[0], flasher[1]+adjacent[1]) in nextFlashers+flashers):
                        nextFlashers.append((flasher[0]+adjacent[0], flasher[1]+adjacent[1]))

        flashers = nextFlashers
    return flashesCount

def step(grid: Grid) -> int:
    return flash(grid, increment(grid))

def day11_part2_main() -> int:
    with open("day 11/inputs.txt", 'r') as inFile:
        grid: Grid = [[int(col) for col in line.strip()] for line in inFile.readlines()]
    
        steps: int = 0
        while sum([sum(line) for line in grid]) != 0:
            _ = step(grid)
            steps += 1
    
        for line in grid:
            for col in line:
                print(col, end=' ')
            print()
        
        return steps
        
if __name__ == "__main__":
    print(day11_part2_main())