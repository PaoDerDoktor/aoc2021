class DeterministicDie:
    def __init__(self) -> None:
        self._rollsAmount: int = 0
    
    def get_rolls_amount(self) -> int:
        return self._rollsAmount
    
    def __next__(self) -> int:
        self._rollsAmount += 1
        return self._rollsAmount%100
    
    def __repr__(self) -> str:
        return f"DeterministicDie[rolls amount={self._rollsAmount}]"

class Player:
    def __init__(self, startPos: int) -> None:
        self._pos:   int = startPos
        self._score: int = 0
        
    def get_position(self) -> int:
        return self._pos
    
    def get_score(self) -> int:
        return self._score
    
    def move(self, amount: int) -> None:
        self._pos = (self._pos+amount)%10
        if self._pos == 0:
            self._pos = 10
        self._score += self._pos
    
    def __repr__(self) -> str:
        return f"Player[score={self._score}, position={self._pos}]"

class Game:
    def __init__(self, player1: Player, player2: Player, die: DeterministicDie) -> None:
        self._player1     : Player           = player1
        self._player2     : Player           = player2
        self._die         : DeterministicDie = die
        self._activePlayer: Player           = player1
    
    def get_player1_pos(self) -> int:
        return self._player1.get_position()
    
    def get_player1_score(self) -> int:
        return self._player1.get_score()
    
    def get_player2_pos(self) -> int:
        return self._player2.get_position()
    
    def get_player2_score(self) -> int:
        return self._player2.get_score()
    
    def get_dice_rolls_amount(self) -> int:
        return self._die.get_rolls_amount()
    
    def get_active_player(self) -> Player:
        return self._activePlayer
    
    def get_winner(self) -> Player|None:
        if self._player1.get_score() >= 1000:
            return self._player1
        elif self._player2.get_score() >= 1000:
            return self._player2
        else:
            return None
    
    def get_loser(self) -> Player|None:
        winner: Player|None = self.get_winner()
        if winner == None:
            return None
        elif winner == self._player1:
            return self._player2
        else:
            return self._player1
        
    def _switch_active_players(self) -> None:
        if self._activePlayer == self._player1:
            self._activePlayer = self._player2
        else:
            self._activePlayer = self._player1
    
    def _roll_dices(self) -> int:
        return next(self._die) + next(self._die) + next(self._die)
    
    def _move_active_player(self) -> None:
        self._activePlayer.move(self._roll_dices())
        self._switch_active_players()
        
    def __repr__(self) -> str:
        return f"Game[die={self._die}, player1={self._player1}, player2={self._player2}]"
    
    # GAME LOOP
    
    def game_loop(self) -> None:
        while self.get_winner() == None:
            self._move_active_player()

def day21_part1_main():
    with open("day 21/inputs.txt", 'r') as inFile:
        game: Game = Game(Player(int(inFile.readline().strip().split(": ")[1])),
                          Player(int(inFile.readline().strip().split(": ")[1])),
                          DeterministicDie())
        
        print(game)
        
        game.game_loop()
        
        print(game)
        
        return game.get_dice_rolls_amount()*game.get_loser().get_score() # type: ignore --- As the game is ended, we know loser won't be None
        
if __name__ == "__main__":
    print(day21_part1_main())