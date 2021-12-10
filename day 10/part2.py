OPEN:   list[str]      = ["(",      "[",      "{",     "<"]
CLOSE:  list[str]      = [")",      "]",      "}",     ">"]
PAIRS:  dict[str, str] = {"(": ")", "[": "]", "{":"}", "<": ">"}
SCORES: dict[str, int] = {")": 1,   "]": 2,   "}": 3,  ">": 4}

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

def autocomplete(string: str) -> str:
    """Checks wether a string must be autocompleted and do it if so

    Args:
        string (str): The string to test

    Returns:
        str: The autocompleting sequence
    """
    
    openedStack: list[str] = []
    for char in string:
        if char in OPEN:
            openedStack.append(char)
        else:
            openedStack.pop()
    return "".join([PAIRS[char] for char in openedStack[::-1]])

def get_autocomplete_score(string: str) -> int:
    """Get the score of an autocompletion sequence

    Args:
        string (str): The autocompletion sequence

    Returns:
        int: The score of the autocompletion sequence
    """
    
    total: int = 0
    
    for char in string:
        total *= 5
        total += SCORES[char]
    
    return total

def day10_part2_main() -> int:
    with open("day 10/inputs.txt", 'r') as inFile:
        lines = [line.strip() for line in inFile.readlines()]
        lines = [line for line in lines if check_illegal(line) == '']
        scores: list[int] = [get_autocomplete_score(autocomplete(line)) for line in lines]
        
        scores = sorted(scores)
        
        print(scores)
        
        return scores[int(len(scores)/2)]
    
if __name__ == "__main__":
    print(day10_part2_main())