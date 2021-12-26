from copy import deepcopy


def get_pattern(instructions: list[str]) -> list[str]:
    pattern: list[str] = []
    first:   bool      = True
    for instruction in instructions:
        if instruction == instructions[0]:
            if first:
                first = False
            else:
                break
        pattern.append(instruction)
    return pattern

def split_instructions(instructions: list[str], patternLength: int) -> list[list[str]]:
    return [instructions[start:start+patternLength] for start in range(0, len(instructions), patternLength)]
    
def get_args(algorithms: list[list[str]]) -> list[tuple[int, int, int]]:
    args: list[tuple[int, int, int]] = []
    for algorithm in algorithms:
        args.append((int(algorithm[4].split()[2]), int(algorithm[5].split()[2]), int(algorithm[15].split()[2])))
    return args

def solve_blocks(numToTest: list[str], args: list[tuple[int, int, int]]) -> list[str]:
    zStack:  list[tuple[int, int]] = []
    numCopy: list[str]             = deepcopy(numToTest)
    for blockId, (arg1, arg2, arg3) in enumerate(args):
        digit: int = int(numCopy[blockId])
        if arg1 == 26:
            j, preAdd = zStack.pop()
            jDigit: int = int(numCopy[j])
            digit = jDigit + preAdd + arg2
            if digit >= 10:
                jDigit -= digit - 9
                digit = 9
            elif digit <= 0:
                jDigit += 1 - digit
                digit = 1
            numCopy[blockId] = str(digit)
            numCopy[j]       = str(jDigit)
        elif arg1 == 1:
            zStack.append((blockId, arg3))
    return numCopy
            
    

def day24_part1_main():
    with open("day 24/inputs.txt", 'r') as inFile:
        instructions: list[str] = inFile.read().split('\n')
        
        pattern: list[str] = get_pattern(instructions)
        assert len(instructions) % len(pattern) == 0
        
        algorithms: list[list[str]]             = split_instructions(instructions, len(pattern))
        args:        list[tuple[int, int, int]] = get_args(algorithms)
        
        startNumber: list[str] = ['9' for _ in range(14)]
        assert len(startNumber) == 14
        
        return int("".join(solve_blocks(startNumber, args)))
        
        
    
        

if __name__ == "__main__":
    print(day24_part1_main())
    
    #Coucou louloute <3 Je t'aime tres tres fort ma cherie ^^