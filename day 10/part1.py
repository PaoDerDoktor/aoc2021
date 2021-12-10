OPEN:   list[str]      = ["(",      "[",      "{",       "<"]
CLOSE:  list[str]      = [")",      "]",      "}",       ">"]
PAIRS:  dict[str, str] = {"(": ")", "[": "]", "{":"}",   "<": ">"}
SCORES: dict[str, int] = {")": 3,   "]": 57,  "}": 1197, ">": 25137}

def check_illegal(string: str) -> str:
    """Check wether a string is illegal or not

    Args:
        string (str): The string to test

    Returns:
        str: The first illegal character encountered, or an empty string if they were none.
    """
    
    openedStack: list[str] = []
    for char in string:
        if char in OPEN:
            openedStack.append(char)
        elif char != PAIRS[openedStack[-1]]:
            return char
        else:
            openedStack.pop()
    return ''

def day10_part1_main() -> int:
    with open("day 10/inputs.txt", 'r') as inFile:
        total: int = 0
        for line in inFile.readlines():
            illegalChar: str = check_illegal(line.strip())
            if illegalChar != '':
                total += SCORES[illegalChar]
        return total
    
if __name__ == "__main__":
    print(day10_part1_main())