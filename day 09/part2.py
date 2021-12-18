Point = tuple[int, int]
Basin = list[Point]
ADJACENT: list[Point] = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def day9_part2_main() -> int:
    with open("day 9/inputs.txt", 'r') as inFile:
        heightMap: list[list[int]] = [[int(tile) for tile in line.strip()] for line in inFile.readlines()]
        
        lowPoints: list[Point] = []
        for j in range(len(heightMap)):
            for i in range(len(heightMap[0])):
                isLowPoint: bool = True
                for adjacent in ADJACENT:
                    if 0 <=j+adjacent[1] < len(heightMap) and 0 <= i+adjacent[0] < len(heightMap[0]):
                        if not heightMap[j+adjacent[1]][i+adjacent[0]] > heightMap[j][i]:
                            isLowPoint = False
                            break
                if isLowPoint:
                    lowPoints.append((i, j))
        
        basins:  list[Basin] = list(map(list, zip(lowPoints[:])))
        latests: list[list[Point]] = basins[:]
        
        while sum([len(latestBasin) for latestBasin in latests]) != 0:
            for latestBasinId, latestBasin in enumerate(latests):
                if len(latestBasin) == 0:
                    continue
                
                newLatest: list[Point] = []
                for latestLow in latestBasin:
                    for adjacent in ADJACENT:
                        if (0 <= latestLow[1]+adjacent[1] < len(heightMap) and 0 <= latestLow[0]+adjacent[0] < len(heightMap[0])
                            and not (latestLow[0]+adjacent[0], latestLow[1]+adjacent[1]) in basins[latestBasinId]
                            and not (latestLow[0]+adjacent[0], latestLow[1]+adjacent[1]) in newLatest
                            and heightMap[latestLow[1]+adjacent[1]][latestLow[0]+adjacent[0]] > heightMap[latestLow[1]][latestLow[0]]
                            and heightMap[latestLow[1]+adjacent[1]][latestLow[0]+adjacent[0]] != 9):
                            
                            newLatest.append((latestLow[0]+adjacent[0], latestLow[1]+adjacent[1]))
                            basins[latestBasinId].append((latestLow[0]+adjacent[0], latestLow[1]+adjacent[1]))
                latests[latestBasinId] = newLatest
        basins = sorted(basins, key=len)
        
        return len(basins[-3])*len(basins[-2])*len(basins[-1])
    
if __name__ == "__main__":
    print(day9_part2_main())