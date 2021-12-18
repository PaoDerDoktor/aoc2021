from __future__ import annotations
from math import floor, ceil, inf

class BinNode:
    def __init__(self, left: int|list, right: int|list, depth: int = 0, prev: BinNode|None = None):
        if type(left) == int:
            self.left: int = left # type: ignore -- Already tested in `if-else` statement right before
        else:
            self.left: BinNode = BinNode(left[0], left[1], depth+1, self) # type: ignore -- Already tested in `if-else` statement right before
            self.left.prev = self # type: ignore - avoiding None conflict
            self.left.depth = depth+1
            
        if type(right) == int:
            self.right: int = right # type: ignore -- Already tested in `if-else` statement right before
        else:
            self.right: BinNode = BinNode(right[0], right[1], depth+1, self) # type: ignore -- Already tested in `if-else` statement right before
        
        self.prev:  BinNode|None = prev
        self.depth: int          = depth
    
    def __repr__(self) -> str:
        return f"[{repr(self.left)}, {repr(self.right)}]"
    
    def __eq__(self, otherBinNode: object) -> bool:
        if isinstance(otherBinNode, self.__class__):
            return (self.left == otherBinNode.left
                    and self.right == otherBinNode.right)
        return False
    
    def __ne__(self, otherBinNode: object) -> bool:
        return not self == otherBinNode
    
    def _make_explode(self) -> bool:
        if self.depth == 4:
            currentNode: BinNode|None = self.prev
            previousNode: BinNode = self
            left:  int = self.left  # type: ignore
            right: int = self.right # type: ignore --- We know at this depth that left and right can't be sublists
            isLeftAdded: bool = False
            isRightAdded: bool = False
            while not currentNode == None:
                if not currentNode.left is previousNode and not isLeftAdded:
                    if type(currentNode.left) == int:
                        currentNode.left += left # type: ignore --- Again, pylance not checking conditions :/
                    else:
                        nextNode = currentNode.left
                        while type(nextNode.right) != int:
                            nextNode = nextNode.right
                        nextNode.right += left # type: ignore --- We know nextNode.right is an int because of the while just before
                    isLeftAdded = True
                if not currentNode.right is previousNode and not isRightAdded:
                    if type(currentNode.right) == int:
                        currentNode.right += right # type: ignore --- Again, pylance not checking conditions :/
                    else:
                        nextNode = currentNode.right
                        while type(nextNode.left) != int:
                            nextNode = nextNode.left
                        nextNode.left += right # type: ignore --- We know nextNode.left is an int because of the while just before
                    isRightAdded = True
                previousNode = currentNode
                currentNode = currentNode.prev
            if self.prev.left is self:  # type: ignore --- avoiding None conflict
                self.prev.left = 0  # type: ignore --- wtf pylance
            if self.prev.right is self: # type: ignore --- avoiding None conflict
                self.prev.right = 0 # type: ignore --- wtf pylance
            return True
        return False
                    
    def explode(self) -> bool:
        path = [_ for _ in (self.right, self.left) if type(_) != int]
        while len(path) > 0:
            currentNode = path.pop()
            if currentNode._make_explode():
                return True
            path += [_ for _ in (currentNode.right, currentNode.left) if type(_) != int]
        return False

    def split(self) -> bool:
        didSplit: bool = False
        if type(self.left) != int:
            didSplit = self.left.split()  # type: ignore --- PYLANCE......
        if type(self.left) == int and self.left >= 10: # type: ignore --- ...
            self.left = BinNode(floor(self.left/2), ceil(self.left/2), self.depth+1, self) # type: ignore --- I really need to understand how `|` works
            return True
        
        if type(self.right) != int and not didSplit:
            didSplit = self.right.split() # type: ignore --- Pylance at it YET AGAIN
        if type(self.right) == int and self.right >= 10 and not didSplit: # type: ignore --- ...
            self.right = BinNode(floor(self.right/2), ceil(self.right/2), self.depth+1, self) # type: ignore --- I really need to understand how `|` works
            return True
            
        return didSplit
    
    def reduce(self):
        didSomething: bool = True
        while didSomething:
            didSomething = False
            didSomething = self.explode()
            if didSomething:
                continue
            didSomething = self.split()
    
    def get_magnitude(self) -> int:
        if type(self.left) == int and type(self.right) != int:
            return 3*self.left + 2*self.right.get_magnitude() # type: ignore --- pylance
        if type(self.left) != int and type(self.right) == int:
            return 3*self.left.get_magnitude() + 2*self.right # type: ignore --- pylance
        if type(self.left) == int and type(self.right) == int:
            return 3*self.left + 2*self.right # type: ignore --- pylance
        else:
            return 3*self.left.get_magnitude() + 2*self.right.get_magnitude()
    
def load(numberStr: str):
    return eval(numberStr)

def list_to_tree(num: list, depth: int = 0, prev: None|BinNode = None) -> BinNode:
    return BinNode(num[0], num[1], depth, prev)

def day18_part1_main() -> int:
    with open("day 18/inputs.txt", 'r') as inFile:
        numList = [load(_.strip()) for _ in inFile.readlines()]
        
        print("first print =",numList)
        node: BinNode = list_to_tree(numList.pop(0))
        node.reduce()
        while len(numList) > 0:
            node = list_to_tree(load(f"[{repr(node)}, {repr(numList.pop(0))}]"))
            node.reduce()
        return node.get_magnitude()
        
        
if __name__ == "__main__":
    print(day18_part1_main())