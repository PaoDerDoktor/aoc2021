from functools import cache
from sys import setrecursionlimit


class DiracDie:
    def __init__(self) -> None:
        self._player1Wins: int = 0
        self._player2Wins: int = 0
        self._values: list[int] = [1,2,3]
    
    def simulate(self, p1Start: int, p2Start: int) -> tuple[int, int]:
        return (
            self._simulate(p1Start, p2Start, 0, 0, True, 0, 0, 1),
            self._simulate(p1Start, p2Start, 0, 0, True, 0, 0, 2)
        )
    
    @cache
    def _simulate(self, p1Start: int, p2Start: int, p1Score: int, p2Score: int, isPlayer1sTurn: bool, rolls: int, rollsCount: int, winnerSearch: int) -> int:
        if rollsCount == 3:
            
            if isPlayer1sTurn:
                p1Start += rolls
                p1Start %= 10
                if p1Start == 0:
                    p1Start = 10
                p1Score += p1Start
                isPlayer1sTurn = False
            else:
                p2Start += rolls
                p2Start %= 10
                if p2Start == 0:
                    p2Start = 10
                p2Score += p2Start
                isPlayer1sTurn = True
            
            rolls = 0
            rollsCount = 0
            
            if (winnerSearch == 1 and p1Score >= 21) or (winnerSearch == 2 and p2Score >= 21):
                return 1
            elif (winnerSearch == 1 and p2Score >= 21) or (winnerSearch == 2 and p1Score >= 21):
                return 0
            
        return sum([self._simulate(p1Start, p2Start, p1Score, p2Score, isPlayer1sTurn, rolls+i, rollsCount+1, winnerSearch) for i in self._values])
                
            
            


def day21_part1_main():
    with open("day 21/inputs.txt", 'r') as inFile:
        die: DiracDie = DiracDie()
        p1Start: int = int(inFile.readline().strip().split(": ")[1])
        p2Start: int = int(inFile.readline().strip().split(": ")[1])
        
        print(p1Start, p2Start)
        
        sim = die.simulate(p1Start, p2Start)
        
        print(sim)
        return max(sim)
        
if __name__ == "__main__":
    setrecursionlimit(1500)
    print(day21_part1_main())