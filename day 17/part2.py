def shoot_lands(xStartVelocity, yStartVelocity, xRange, yRange) -> bool:
    position: tuple[int, int] = (0,0)
    
    xVelocity: int = xStartVelocity
    yVelocity: int = yStartVelocity
    
    while position[0] <= max(xRange) and position[1] >= min(yRange):
        position = (position[0]+xVelocity, position[1]+yVelocity)
        if position[0] in xRange and position[1] in yRange:
            return True
        if position[0] > max(xRange) or position[1] < min(yRange):
            return False
        if xVelocity != 0:
            xVelocity -= 1
        yVelocity -= 1
    return False


def day17_part1_main() -> int:
    with open("day 17/inputs.txt", 'r') as inFile:
        rawRanges: str = inFile.read()[13:]
        xRawRange, yRawRange = rawRanges.split(', ')
        xRange: list[int] = list(range(int(xRawRange.split('..')[0][2:]), int(xRawRange.split('..')[1]))) + [int(xRawRange.split('..')[1])]
        yRange: list[int] = list(range(int(yRawRange.split('..')[0][2:]), int(yRawRange.split('..')[1]))) + [int(yRawRange.split('..')[1])]
        
        velocities: set[tuple[int, int]] = set()
        total: int = 0
        for xStartVelocity in range(1, max(xRange)+1):
            for yStartVelocity in range(min(yRange), int((yRange[0]+2)/4)+1000):
                if shoot_lands(xStartVelocity, yStartVelocity, xRange, yRange):
                    velocities.add((xStartVelocity, yStartVelocity))
                    total += 1
        
        print(velocities)
        print(f"{total=}")
        return len(velocities)
        
        

if __name__ == "__main__":
    print(day17_part1_main())