from typing import List, Tuple

def day2_part1_main():
    with open("day 2/inputs.txt", 'r') as inFile:
        moves: List[Tuple[str, int]] = [(_.split()[0], int(_.split()[1])) for _ in inFile.readlines()]
        
        hPos: int = 0
        depth: int = 0
        
        for move in moves:
            if move[0] == "forward":
                hPos += move[1]
            elif move[0] == "down":
                depth += move[1]
            else:
                depth -= move[1]
        
        return hPos*depth
    
    
if __name__ == "__main__":
    print(day2_part1_main())