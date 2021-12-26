Cube = tuple[int, int, int]


def clamp(lower: int, value: int, upper: int) -> int:
    return max(lower, min(value, upper))

def constricted_range(lower: int, upper: int) -> range:
    if lower >= 50:
        lower = 0
        upper = 0
    elif upper <= -49:
        lower = 0
        upper = 0
    else:
        lower = clamp(-50, lower, 50)
        upper = clamp(-50, upper, 51)
    return range(lower, upper)

def parse_input() -> list[tuple[bool, range, range, range]]:
    setup: list[tuple[bool, range, range, range]] = []
    with open("day 22/inputs.txt", 'r') as inFile:
        lines = inFile.readlines()
        for line in lines:
            isOnRaw, cubesRaw = line.strip().split(' ')
            ruleXRaw, ruleYRaw, ruleZRaw = cubesRaw.split(',')
            firstBoundX, secondBoundX = ruleXRaw[2:].split("..")
            firstBoundY, secondBoundY = ruleYRaw[2:].split("..")
            firstBoundZ, secondBoundZ = ruleZRaw[2:].split("..")
            
            isOn:   bool  = True if isOnRaw == "on" else False
            rangeX: range = constricted_range(
                min(int(firstBoundX), int(secondBoundX)),
                max(int(firstBoundX), int(secondBoundX))+1)
            rangeY: range = constricted_range(
                min(int(firstBoundY), int(secondBoundY)),
                max(int(firstBoundY), int(secondBoundY))+1)
            rangeZ: range = constricted_range(
                min(int(firstBoundZ), int(secondBoundZ)),
                max(int(firstBoundZ), int(secondBoundZ))+1)
            
            setup.append((isOn, rangeX, rangeY, rangeZ))
    return setup

def apply_setup_instruction(instruction: tuple[bool, range, range, range], onCubes: set[Cube]) -> None:
    print(instruction)
    for x in instruction[1]:
        for y in instruction[2]:
            for z in instruction[3]:
                if instruction[0] == True:
                    onCubes.add((x,y,z))
                else:
                    onCubes.discard((x,y,z))

def day22_part1_main() -> int:
    setup: list[tuple[bool, range, range, range]] = parse_input()
    onCubes: set[Cube] = set()
    
    for setupInstruction in setup:
        apply_setup_instruction(setupInstruction, onCubes)
    
    return len(onCubes)

if __name__ == "__main__":
    print(day22_part1_main())