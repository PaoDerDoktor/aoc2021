from sys import maxsize

Point = tuple[int, int]
Grid  = list[list[int]]


def get_neighbors(current: Point, grid: Grid, unvisitedPoints: set[Point]) -> set[Point]:
    neighbors: set[Point] = set()
    if 0 <= current[0]-1 < len(grid[0]) and (current[0]-1, current[1]) in unvisitedPoints:
            neighbors.add((current[0]-1, current[1]))
    if 0 <= current[0]+1 < len(grid[0]) and (current[0]+1, current[1]) in unvisitedPoints:
            neighbors.add((current[0]+1, current[1]))
    if 0 <= current[1]-1 < len(grid) and (current[0], current[1]-1) in unvisitedPoints:
            neighbors.add((current[0], current[1]-1))
    if 0 <= current[1]+1 < len(grid) and (current[0], current[1]+1) in unvisitedPoints:
            neighbors.add((current[0], current[1]+1))
    return neighbors

def get_path(source: Point, target: Point, previousDict: dict[Point, Point]) -> list[Point]:
    path: list[Point] = []
    current = target
    while current != source:
        path.append(current)
        current = previousDict[current]
    return path

def dijkstra(grid: Grid) -> list[Point]:
    unvisited: set[Point] = {(j, i) for j in range(len(grid)) for i in range(len(grid[0]))}
    
    distance: dict[Point, int]   = {point: maxsize  for point in unvisited}
    previous: dict[Point, Point] = {point: (-1, -1) for point in unvisited}
    
    distance[(0, 0)] = 0
    currentPoint: Point = (0, 0)
    
    while (len(grid)-1, len(grid[0])-1) in unvisited:
        neighbors: set[Point] = get_neighbors(currentPoint, grid, unvisited)
        for neighbor in neighbors:
            if distance[currentPoint] + grid[neighbor[1]][neighbor[0]] < distance[neighbor]:
                distance[neighbor] = distance[currentPoint] + grid[neighbor[1]][neighbor[0]]
                previous[neighbor] = currentPoint
        
        unvisited.remove(currentPoint)
        minDist: int = maxsize
        minNode: Point = (-1, -1)
        for unvisitedNode in unvisited:
            if distance[unvisitedNode] < minDist:
                minDist = distance[unvisitedNode]
                minNode = unvisitedNode
        currentPoint = minNode
        
    return get_path((0, 0), (len(grid)-1, len(grid[0])-1), previous)

def get_total_risk(path: list[Point], grid: Grid) -> int:
    totalRisk: int = 0
    for point in path:
        totalRisk += grid[point[1]][point[0]]
    return totalRisk

def day15_part1_main() -> int:
    with open("day 15/inputs.txt", 'r') as inFile:
        grid: Grid = [[int(val) for val in line.strip()] for line in inFile.readlines()]
        
        path: list[Point] = dijkstra(grid)
        
        return get_total_risk(path, grid)


if __name__ == "__main__":
    print(day15_part1_main())