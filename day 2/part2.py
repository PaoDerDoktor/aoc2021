from typing import List, Tuple

def day2_part2_main():
    with open("day 2/inputs.txt", 'r') as inFile:
        moves: List[Tuple[str, int]] = [(_.split()[0], int(_.split()[1])) for _ in inFile.readlines()]
        
        aim: int = 0
        hPos: int = 0
        depth: int = 0
        
        for move in moves:
            if move[0] == "forward":
                hPos += move[1]
                depth += move[1]*aim
            elif move[0] == "down":
                aim += move[1]
            else:
                aim -= move[1]
        
        return hPos*depth
    
if __name__ == "__main__":
    print(day2_part2_main())