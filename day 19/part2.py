from typing import Any


Point = tuple[int, int, int]

def parse(input: list[str]) -> list[list[Point]]:
    report: list[list[Point]] = []
    for scanReport in input:
        points: list[Point] = []
        for rawPoint in scanReport.splitlines()[1:]:
            points.append(tuple([int(rawCoord) for rawCoord in rawPoint.split(',')])) # type: ignore --- We can because of the input file's structure
        report.append(points)
    return report


def calc_distances(beacons: list[Point]) -> list[set[int]]:
    distances: list[set[int]] = [set() for _ in beacons]
    
    for firstBeaconId, firstBeacon in enumerate(beacons):
        for secondBeaconId, secondBeacon in enumerate(beacons[firstBeaconId+1:], firstBeaconId+1):
            manhattanDistance: int = (abs(firstBeacon[0] - secondBeacon[0]) +
                                      abs(firstBeacon[1] - secondBeacon[1]) +
                                      abs(firstBeacon[2] - secondBeacon[2]))
            distances[ firstBeaconId].add(manhattanDistance)
            distances[secondBeaconId].add(manhattanDistance)
    return distances


def num_overlapping(firstScanner: list[set[int]], secondScanner: list[set[int]]) -> int:
    total: int = 0
    for firstScannersDistances in firstScanner:
        for secondScannersDistances in secondScanner:
            if len(firstScannersDistances.intersection(secondScannersDistances)) >= 11:
                total += 1
    return total


def get_transform_func(v0: Point, v1: Point) -> str:
    (x0, y0, z0) = v0
    (x1, y1, z1) = v1
    
    transform = '('
    if abs(x0) == abs(x1):
        if x0 // x1 < 0:
            transform += '-'
        transform += 'x,'
    elif abs(x0) == abs(y1):
        if 0 > x0 // y1:
            transform += '-'
        transform += 'y,'
    elif abs(x0) == abs(z1):
        if 0 > x0 // z1:
            transform += '-'
        transform += 'z,'
        
    if abs(y0) == abs(x1):
        if 0 > y0 // x1:
            transform += '-'
        transform += 'x,'
    elif abs(y0) == abs(y1):
        if 0 > y0 // y1:
            transform += '-'
        transform += 'y,'
    elif abs(y0) == abs(z1):
        if 0 > y0 // z1:
            transform += '-'
        transform += 'z,'
        
    if abs(z0) == abs(x1):
        if 0 > z0 // x1:
            transform += '-'
        transform += 'x'
    elif abs(z0) == abs(y1):
        if 0 > z0 // y1:
            transform += '-'
        transform += 'y'
    elif abs(z0) == abs(z1):
        if 0 > z0 // z1:
            transform += '-'
        transform += 'z'
    transform += ')'
    return transform


def transform(scanners: list[dict[str, Any]], idx: int, done: list[int]=[]) -> None:
    done.append(idx)
    for n in scanners[idx]['overlapping']:
        if n in done:
            continue
        overlapping = []
        for firstScannersId, firstScannersDistances in enumerate(scanners[idx]['metrics']):
            for secondScannersId, secondScannersDistances in enumerate(scanners[n]['metrics']):
                if len(firstScannersDistances.intersection(secondScannersDistances)) >= 11:
                    overlapping.append((firstScannersId, secondScannersId))
                if len(overlapping) >= 2:
                    break
            if len(overlapping) >= 2:
                break
            
        firstPoint:  Point = scanners[idx]['beacons'][overlapping[0][0]]
        secondPoint: Point = scanners[idx]['beacons'][overlapping[1][0]]
        v0: Point = (firstPoint[0] - secondPoint[0],
                     firstPoint[1] - secondPoint[1],
                     firstPoint[2] - secondPoint[2],)
        
        thirdPoint:  Point = scanners[n]['beacons'][overlapping[0][1]]
        fourthPoint: Point = scanners[n]['beacons'][overlapping[1][1]]
        v1: Point = (thirdPoint[0] - fourthPoint[0],
                     thirdPoint[1] - fourthPoint[1],
                     thirdPoint[2] - fourthPoint[2],)
        
        transform_func: str = get_transform_func(v0, v1)
        
        for i in range(len(scanners[n]['beacons'])):
            (x, y, z) = scanners[n]['beacons'][i]
            scanners[n]['beacons'][i] = eval(transform_func)
            
        (xo, yo, zo) = scanners[idx]['origin']
        (x0, y0, z0) = scanners[idx]['beacons'][overlapping[0][0]]
        (x1, y1, z1) = scanners[  n]['beacons'][overlapping[0][1]]
        
        scanners[n]['origin'] = (xo + x0 - x1, yo + y0 - y1, zo + z0 - z1)
        (xo, yo, zo) = scanners[n]['origin']
        
        transform(scanners, n, done)
        
        for i in range(len(scanners[n]['beacons'])):
            (x, y, z) = scanners[n]['beacons'][i]
            scanners[n]['beacons'][i] = (x + xo, y + yo, z + zo)


def solve(report: list[list[Point]]) -> int:
    scanners: list[dict[str, Any]] = []
    for b in report:
        s: dict[str, Any] = {}
        s['beacons'] = b
        s['metrics'] = calc_distances(b)
        s['origin'] = (0, 0, 0)
        s['overlapping'] = []
        scanners.append(s)
    for i in range(len(scanners)):
        for j in range(i + 1, len(scanners)):
            num = num_overlapping(scanners[i]['metrics'], scanners[j]['metrics'])
            if num:
                scanners[i]['overlapping'].append(j)
                scanners[j]['overlapping'].append(i)
    m: set[list[Point]] = set()
    transform(scanners, 0)
    for s in scanners:
        for b in s['beacons']:
            m.add(b)
            
    maxManhattanDistance: int = -1
    for firstScannerIndex, firstScanner in enumerate(scanners):
        (xi, yi, zi) = firstScanner['origin']
        for secondScanner in scanners[firstScannerIndex+1:]:
            (xj, yj, zj) = secondScanner['origin']
            currrentManhattanDistance = abs(xi - xj) + abs(yi - yj) + abs(zi - zj)
            maxManhattanDistance = max(maxManhattanDistance, currrentManhattanDistance)
    return maxManhattanDistance
    
def day19_part_2_main() -> int:
    with open('day 19/inputs.txt', 'r') as inFile:
        report: list[list[Point]] = []
        for scanReport in inFile.read().split("\n\n"):
            points: list[Point] = []
            for rawPoint in scanReport.splitlines()[1:]:
                points.append(tuple([int(rawCoord) for rawCoord in rawPoint.split(',')])) # type: ignore --- We can because of the input file's structure
            report.append(points)
        return solve(report)
    

if __name__ == '__main__':
    print(day19_part_2_main())
