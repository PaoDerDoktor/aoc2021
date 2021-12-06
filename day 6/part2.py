def pad(width: int, s: str) -> str:
    paddedS: str = s
    for _ in range(width-len(s)):
        paddedS = " "+paddedS
    return paddedS

def display_fishes(fishes: dict[int, int]) -> str:
    representation: str = ""
    maxLength = -1
    for value in fishes.values():
        maxLength = max(maxLength, len(str(value)))
    for i in range(9):
        representation += pad(maxLength, str(i))+" "
    representation += "\n"
    for i in range(9):
        representation += pad(maxLength, str(fishes[i]))+" "
    return representation
    

def day6_part1_main() -> int:
    with open("day 6/inputs.txt", 'r') as inFile:
        fishesInput: list[int] = [int(_) for _ in inFile.readline().split(',')]
        fishes: dict[int, int] = {_:fishesInput.count(_) for _ in range(9)}
        iterations: int   = 256 # Yes, that's the only change
        
        for _ in range(iterations):
            newFishes: dict[int, int] = {}
            for cycle in range(1,9):
                newFishes[cycle-1] = fishes[cycle]
            newFishes[8]  = fishes[0]
            newFishes[6] += fishes[0]
            fishes = newFishes
            
        
        return sum(fishes.values())
        
if __name__ == '__main__':
    print(day6_part1_main())