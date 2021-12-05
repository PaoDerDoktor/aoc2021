from dataclasses import dataclass

@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int
    
@dataclass(frozen=True, eq=True)
class Line:
    start: Point
    end: Point

def day5_part1_main():
    with open("day 5/inputs.txt", 'r') as inFile:
        lines: list[Line] = [Line(Point(int(line.split(" -> ")[0].split(',')[0]),
                                        int(line.split(" -> ")[0].split(',')[1])),
                                  Point(int(line.split(" -> ")[1].split(',')[0]),
                                        int(line.split(" -> ")[1].split(',')[1]))) for line in inFile.readlines()]
        
        smokeMap: dict[Point, int] = dict()
        maxX: int = -1
        maxY: int = -1
        
        overlapCounter: int = 0
        
        for line in lines:
            if max(line.start.x, line.end.x) > maxX:
                maxX = max(line.start.x, line.end.x)
            if max(line.start.y, line.end.y) > maxY:
                maxY = max(line.start.y, line.end.y)
            if line.start.x == line.end.x or line.start.y == line.end.y:
                for point in [Point(x, y)
                              for x in range(min(line.start.x, line.end.x), max(line.start.x, line.end.x)+1)
                              for y in range(min(line.start.y, line.end.y), max(line.start.y, line.end.y)+1)]:
                    if not point in smokeMap:
                        smokeMap[point] = 1
                    elif smokeMap[point] == 1:
                        smokeMap[point] += 1
                        overlapCounter  += 1
                    else:
                        smokeMap[point] += 1
                        
        return overlapCounter
        
        
if __name__ == '__main__':
    print(day5_part1_main())