Board = list[list[int]]
Mask = Board

def is_mask_wining(mask: Board) -> bool:
    for i in range(len(mask)):
        if sum(mask[i]) == len(mask):
            return True
        count: int = 0
        for j in range(len(mask[0])):
            count += mask[j][i]
        if count == len(mask[0]):
            return True
    return False

def mark(board: Board, mask: Mask, toMark: int) -> Mask:
    for lineID, line in enumerate(board):
        for colID, val in enumerate(line):
            if val == toMark :
                mask[lineID][colID] = 1
    return mask

def day4_part2_main():
    with open("day 4/inputs.txt", 'r') as inFile:
        markedsNums: list[int] = [int(_) for _ in inFile.readline().split(',')]
        inFile.readline() # Skipping empty line
        boards: list[Board] = [[[int(num) for num in line.split()] for line in block.split('\n')] for block in inFile.read().split("\n\n")]
        boardsMasks: list[Mask] = [[[0 for i in range(len(boards[0][0]))] for j in range(len(boards[0]))] for k in range(len(boards))]
        
        lastWinningBoardID: int = -1
        hasBeenMarked: list[int] = []
        
        winningIDs: set[int] = set()
        
        for markedId, marked in enumerate(markedsNums):
            for boardID, board in enumerate(boards):
                boardsMasks[boardID] = mark(board, boardsMasks[boardID], marked)
                if markedId > 4:
                    if not boardID in winningIDs and is_mask_wining(boardsMasks[boardID]):
                        winningIDs.add(boardID)
                    if len(winningIDs) == len(boards):
                        lastWinningBoardID = boardID
                        break
                        
            hasBeenMarked.append(marked)
            if lastWinningBoardID != -1:
                break
        
        lastWinningBoard: Board = boards[lastWinningBoardID]
        checksum: int = 0
        
        for lineID, line in enumerate(lastWinningBoard):
            for colID, value in enumerate(line):
                if not value in hasBeenMarked:
                    checksum += value
                    
        print(hasBeenMarked[-1], lastWinningBoardID)
        
        return checksum * hasBeenMarked[-1]
        
        
        
        
if __name__ == '__main__':
    print(day4_part2_main())