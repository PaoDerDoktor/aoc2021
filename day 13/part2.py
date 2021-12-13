from sys import maxsize


Point = tuple[int, int]


def fold(dots: set[Point], instruction: tuple[str, int]) -> set[Point]:
    newPoints: set[Point] = set()
    for dot in dots:
        if instruction[0] == 'y' and dot[1] > instruction[1]:
            newPoints.add((dot[0], instruction[1]-(dot[1]-instruction[1])))
        elif instruction[0] == 'x' and dot[0] > instruction[1]:
            newPoints.add((instruction[1]-(dot[0]-instruction[1]), dot[1]))
        else:
            newPoints.add(dot)
    return newPoints
            
def print_dots(dots: set[Point]) -> None:
    minX: int = maxsize
    maxX: int = -1
    minY: int = maxsize
    maxY: int = -1
    
    for dot in dots:
        if dot[0] < minX:
            minX = dot[0]
        elif dot[0] > maxX:
            maxX = dot[0]
        if dot[1] < minY:
            minY = dot[1]
        elif dot[1] > maxY:
            maxY = dot[1]
            
    for j in range(minY, maxY+1):
        for i in range(minX, maxX+1):
            if (i,j) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print()
    
def day13_part1_main() -> int:
    with open("day 13/inputs.txt", 'r') as inFile:
        rawDots, rawFolds = inFile.read().split("\n\n")
        dots: set[Point] = {(int(dot.split(',')[0]), int(dot.split(',')[1])) for dot in rawDots.split('\n')}
        folds: list[tuple[str, int]] = []
        for rawFold in rawFolds.split("\n"):
            folds.append((rawFold.split("=")[0][-1], int(rawFold.split("=")[1])))
        
        for foldInstr in folds:
            dots = fold(dots, foldInstr)
        
        print_dots(dots)
        
        return len(dots)

if __name__ == "__main__":
    print(day13_part1_main())