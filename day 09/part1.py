Point = tuple[int, int]
ADJACENT: list[Point] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def day9_part1_main() -> int:
    with open("day 9/inputs.txt", 'r') as inFile:
        heightMap: list[list[int]] = [[int(tile) for tile in line.strip()] for line in inFile.readlines()]
        
        lowPoints: list[Point] = []
        for j in range(len(heightMap)):
            for i in range(len(heightMap[0])):
                isLowPoint: bool = True
                for adjacent in ADJACENT:
                    if 0 <=j+adjacent[1] < len(heightMap) and 0  <= i+adjacent[0] < len(heightMap[0]):
                        if not heightMap[j+adjacent[1]][i+adjacent[0]] > heightMap[j][i]:
                            isLowPoint = False
                            break
                if isLowPoint:
                    lowPoints.append((i, j))
                    
        return sum([1+heightMap[point[1]][point[0]] for point in lowPoints])
    
if __name__ == "__main__":
    print(day9_part1_main())