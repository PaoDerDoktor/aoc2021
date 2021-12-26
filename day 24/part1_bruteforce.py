"""
So, I originally was overhyped by the puzzle.
The input really reminded me of 2019's Intcode, a gimmick I REALLY loved
But yeah, after implementing the ALU I realized (actually tbh I knew it
way sooner but didn't want to admit it) that iit would be really too much long
to process :/

So yeah, still keeping it because I like that ALU class !
"""


from enum import StrEnum
from math import floor
from copy import deepcopy


class Opcode(StrEnum):
    INP = "inp",
    ADD = "add",
    MUL = "mul",
    DIV = "div",
    MOD = "mod",
    EQL = "eql",
    
    INIT = "initial"

Arities: dict[Opcode, int] = {
    Opcode.INP: 1,
    Opcode.ADD: 2,
    Opcode.MUL: 2,
    Opcode.DIV: 2,
    Opcode.MOD: 2,
    Opcode.EQL: 2,
    
    Opcode.INIT: 0
}

Instruction = tuple[Opcode, list[str|int]]


class ALU:
    def __init__(self, inputs: list[str]) -> None:
        self.w: int = 0
        self.x: int = 0
        self.y: int = 0
        self.z: int = 0
        
        self.inputs: list[str] = inputs
        
        self.opcode: Opcode        = Opcode.INIT
        self.args  : list[str|int] = []
    
    def _load(self, var: str) -> int:
        if var == 'w':
            return self.w
        elif var == 'x':
            return self.x
        elif var == 'y':
            return self.y
        elif var == 'z':
            return self.z
        return  -999999
    
    def _write(self, var: str, value: int) -> None:
        if var == 'w':
            self.w = value
        elif var == 'x':
            self.x = value
        elif var == 'y':
            self.y = value
        elif var == 'z':
            self.z = value
    
    def _inp(self) -> None:
        if isinstance(self.args[0], str):
            self._write(self.args[0], int(self.inputs.pop(0)))
    
    def _add(self) -> None:
        if isinstance(self.args[0], str):
            if isinstance(self.args[1], str):
                self._write(self.args[0], self._load(self.args[0])+self._load(self.args[1]))
            else:
                self._write(self.args[0], self._load(self.args[0])+self.args[1])
    
    def _mul(self) -> None:
        if isinstance(self.args[0], str):
            if isinstance(self.args[1], str):
                self._write(self.args[0], self._load(self.args[0])*self._load(self.args[1]))
            else:
                self._write(self.args[0], self._load(self.args[0])*self.args[1])
                
    def _div(self) -> None:
        if isinstance(self.args[0], str):
            if isinstance(self.args[1], str):
                self._write(self.args[0], floor(self._load(self.args[0])/self._load(self.args[1])))
            else:
                self._write(self.args[0], floor(self._load(self.args[0])/self.args[1]))
                
    def _mod(self) -> None:
        if isinstance(self.args[0], str):
            if isinstance(self.args[1], str):
                self._write(self.args[0], self._load(self.args[0])%self._load(self.args[1]))
            else:
                self._write(self.args[0], self._load(self.args[0])%self.args[1])
                
    def _eql(self) -> None:
        if isinstance(self.args[0], str):
            if isinstance(self.args[1], str):
                self._write(self.args[0], int(self._load(self.args[0])==self._load(self.args[1])))
            else:
                self._write(self.args[0], int(self._load(self.args[0])==self.args[1]))
    
    def _fetch_decode(self, instructionRaw: str) -> None:
        self.args = []
        tokens: list[str] = instructionRaw.strip().split()
        self.opcode = Opcode(tokens[0]) # type: ignore
        for arg in tokens[1:]:
            try:
                self.args.append(int(arg))
            except:
                self.args.append(arg)
    
    def _execute(self) -> None:
        if self.opcode == Opcode.INP:
            self._inp()
        elif self.opcode == Opcode.ADD:
            self._add()
        elif self.opcode == Opcode.MUL:
            self._mul()
        elif self.opcode == Opcode.DIV:
            self._div()
        elif self.opcode == Opcode.MOD:
            self._mod()
        elif self.opcode == Opcode.MOD:
            self._mod()
        elif self.opcode == Opcode.EQL:
            self._eql()
            
    def execute_instruction(self, instructionRaw: str) -> None:
        self._fetch_decode(instructionRaw)
        self._execute()
        
        
def str_to_list(s: str) -> list[str]:
    res: list[str] = []
    for c in s:
        res.append(c)
    return res
    
def day24_part1_main_bf():
    with open("day 24/inputs.txt", 'r') as inFile:
        instructions: list[str] = inFile.read().split('\n')
        
        numStrToValidate: str = ""
        for _ in range(14):
            numStrToValidate += '9'
        numToValidate: int = int(numStrToValidate)
        
        biggestYet: int = numToValidate
        while len(numStrToValidate) < 15:
            if not '0' in numStrToValidate:
                listToValidate: list[str] = str_to_list(numStrToValidate)
                instructionsCopy: list[str] = deepcopy(instructions)
                alu: ALU = ALU(listToValidate)
                for instruction in instructionsCopy:
                    alu.execute_instruction(instruction)
                if alu.z == 0:
                    biggestYet = numToValidate
                    print("foundNewBiggest :", biggestYet)
                    return biggestYet
                else:
                    print("not biggest :", numToValidate)
            numToValidate -= 1
            numStrToValidate  = str(numToValidate)
        
        return biggestYet
  
    
if __name__ == "__main__":
    print(day24_part1_main_bf())
