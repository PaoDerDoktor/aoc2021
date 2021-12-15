from sys import maxsize
import heapq

Point = tuple[int, int]
Grid  = list[list[int]]


def get_neighbors(current: Point, grid: Grid, visitedPoints: set[Point]) -> set[Point]:
    neighbors: set[Point] = set()
    if 0 <= current[0]-1 < len(grid[0]) and not (current[0]-1, current[1]) in visitedPoints:
            neighbors.add((current[0]-1, current[1]))
    if 0 <= current[0]+1 < len(grid[0]) and not (current[0]+1, current[1]) in visitedPoints:
            neighbors.add((current[0]+1, current[1]))
    if 0 <= current[1]-1 < len(grid) and not (current[0], current[1]-1) in visitedPoints:
            neighbors.add((current[0], current[1]-1))
    if 0 <= current[1]+1 < len(grid) and not (current[0], current[1]+1) in visitedPoints:
            neighbors.add((current[0], current[1]+1))
    return neighbors

def dijkstra(grid: Grid) -> int:
    visited:  set[Point]         = set()
    distance: dict[Point, int]   = {}
    previous: dict[Point, Point] = {}
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            distance[(i, j)] = maxsize
            previous[(i, j)] = (-1, -1)        
    distance[(0, 0)] = 0
    
    
    heapq.heappush(priorityQueue := [], (0, (0,0)))
    while len(priorityQueue) > 0:
        currentPoint: Point = heapq.heappop(priorityQueue)[1]
        visited.add(currentPoint)
        for neighbor in get_neighbors(currentPoint, grid, visited):
            newDist: int = distance[currentPoint]+grid[neighbor[1]][neighbor[0]]
            if (distance[neighbor] > newDist):
                distance[neighbor] = newDist
                heapq.heappush(priorityQueue, (newDist, neighbor))
    
    return distance[(len(grid)-1, len(grid[0])-1)]

def generate_big_grid(grid: Grid) -> Grid:
    bigGrid: Grid = []
    for j in range(len(grid)*5):
        gridLine: list[int] = []
        for i in range(len(grid[0])*5):
            gridLine.append((grid[j%len(grid)][i%len(grid[0])] + int(i/len(grid)) + int(j/len(grid[0])) - 1) % 9 + 1)
        bigGrid.append(gridLine)
    return bigGrid


def day15_part1_main() -> int:
    with open("day 15/inputs.txt", 'r') as inFile:
        initGrid: Grid = [[int(val) for val in line.strip()] for line in inFile.readlines()]
        grid: Grid = generate_big_grid(initGrid)
        print(grid[0][10])
        
        return dijkstra(grid)


if __name__ == "__main__":
    print(day15_part1_main())