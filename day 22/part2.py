import re
from math import prod
from collections import Counter


Point = tuple[int, int, int]


class Cuboid:
    def __init__(self, on: bool, corner1: Point, corner2: Point) -> None:
        self.on: bool = on
        maxX: int = max(corner1[0], corner2[0])
        maxY: int = max(corner1[1], corner2[1])
        maxZ: int = max(corner1[2], corner2[2])
        self.maxCorner: Point = (maxX, maxY, maxZ)
        minX: int = min(corner1[0], corner2[0])
        minY: int = min(corner1[1], corner2[1])
        minZ: int = min(corner1[2], corner2[2])
        self.minCorner: Point = (minX, minY, minZ)
        
    def get_base_area(self) -> int:
        return (  self.maxCorner[0] - self.minCorner[0]
                * self.maxCorner[1] - self.minCorner[1]
                * self.maxCorner[2] - self.minCorner[2])
        
    def get_intersector(self, cuboid: 'Cuboid'):
        if (   self.maxCorner[0] < cuboid.minCorner[0] or cuboid.maxCorner[0] < self.minCorner[0]
            or self.maxCorner[1] < cuboid.minCorner[1] or cuboid.maxCorner[1] < self.minCorner[1]
            or self.maxCorner[2] < cuboid.minCorner[2] or cuboid.maxCorner[2] < self.minCorner[2]):
            return None
        else:
            intersector: Cuboid = Cuboid(
                cuboid.on,
                (
                    min(self.maxCorner[0], cuboid.maxCorner[0]),
                    min(self.maxCorner[1], cuboid.maxCorner[1]),
                    min(self.maxCorner[2], cuboid.maxCorner[2])
                ),
                (
                    max(self.minCorner[0], cuboid.minCorner[0]),
                    max(self.minCorner[1], cuboid.minCorner[1]),
                    max(self.minCorner[2], cuboid.minCorner[2])
                )
            )
            return intersector


def parse_input() -> list[Cuboid]:
    setup: list[Cuboid] = []
    with open("day 22/inputs.txt", 'r') as inFile:
        lines = inFile.readlines()
        for line in lines:
            isOnRaw, cubesRaw = line.strip().split(' ')
            ruleXRaw, ruleYRaw, ruleZRaw = cubesRaw.split(',')
            firstBoundX, secondBoundX = ruleXRaw[2:].split("..")
            firstBoundY, secondBoundY = ruleYRaw[2:].split("..")
            firstBoundZ, secondBoundZ = ruleZRaw[2:].split("..")
            
            isOn:   bool  = True if isOnRaw == "on" else False
            point1: Point = (
                int(firstBoundX), int(firstBoundY), int(firstBoundZ)
            )
            point2: Point = (
                int(secondBoundX), int(secondBoundY), int(secondBoundZ)
            )
            
            setup.append(Cuboid(isOn, point1, point2))
    return setup

def intersects(a, b):
    # Adapted from a reddit hint
    return all(a[i] <= b[i + 1] and a[i + 1] >= b[i] for i in range(0, 5, 2))

def get_intersection_area(a, b):
    # Adapted from a reddit hint
    return tuple((min if i & 1 else max)(a[i], b[i]) for i in range(6))

def get_area(area):
    # Adapted from a reddit hint
    return prod(area[i + 1] - area[i] + 1 for i in range(0, 5, 2))

def day22_part1_main() -> int:
    # Adapted from a reddit hint
    with open("day 22/inputs.txt", 'r') as inFile:
        instructions = [
            (line.split(' ')[0], tuple(map(int, re.findall(r'-?\d+', line))))
            for line in inFile
        ]

        print(instructions[0])

        areas = Counter()

        for instructionType, newArea in instructions:
            updated_areas = Counter()

            if (instructionType == 'on'):
                updated_areas[newArea] += 1

            for area, value in areas.items():
                if (intersects(newArea, area)):
                    intersection_area = get_intersection_area(newArea, area)
                    updated_areas[intersection_area] -= value

            areas.update(updated_areas)

        print(sum(get_area(area) * value for area, value in areas.items()))
        
        # Trying with Cuboids
    cuboids: list[Cuboid] = parse_input()
    
    areas = Counter()
    for newCuboid in cuboids:
        updated_areas = Counter()

        if newCuboid.on:
            updated_areas[newCuboid] += 1

        for area, value in areas.items():
            intersector = newCuboid.get_intersector(area) # problem should be here. Maybe Cuboid's equality
            if (isinstance(intersector, Cuboid)):
                updated_areas[intersector] -= value

        areas.update(updated_areas)
        
    return sum(area.get_base_area() * value for area, value in areas.items())
    
    
if __name__ == "__main__":
    print(day22_part1_main())