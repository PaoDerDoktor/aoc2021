SEGMENTS: tuple[str,  str,  str,  str,  str,  str,  str]  = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

def day8_part1_main() -> int:
    with open("day 8/inputs.txt", 'r') as inFile:
        displayPatterns: list[list[set[str]]] = []
        displayOutputs:  list[list[set[str]]] = []
        
        outputsList: list[int] = []
        
        for line in inFile.readlines():
            rawPatterns, rawOutputs = line.split(" | ")
            displayPatterns.append([set(i) for i in rawPatterns.split()])
            displayOutputs.append([set(i)  for i in rawOutputs.split()])
        
        for displayId in range(len(displayPatterns)):
            patterns: list[set[str]] = displayPatterns[displayId]
            outputs : list[set[str]] =  displayOutputs[displayId]
            
            match: dict[int, int] = {}
            
            for patternId, pattern in enumerate(patterns): # Easy to get
                if len(pattern) == 2:
                    match[1] = patternId
                elif len(pattern) == 3:
                    match[7] = patternId
                elif len(pattern) == 4:
                    match[4] = patternId
                elif len(pattern) == 7:
                    match[8] = patternId

            while len(match) != 10: # ensuring work order
                for patternId, pattern in enumerate(patterns): # Need easy ones
                    if len(pattern) == 5:
                        if not 3 in match and patterns[match[1]].issubset(pattern):
                            match[3] = patternId
                        elif not 5 in match and len(patterns[match[4]].intersection(pattern)) == 3:
                            match[5] = patternId
                        elif 5 in match and 3 in match and patternId != match[5] and patternId != match[3]:
                            match[2] = patternId
                    elif len(pattern) == 6:
                        if not 9 in match and 3 in match and patterns[match[3]].issubset(pattern):
                            match[9] = patternId
                        elif (not 6 in match and 9 in match and 5 in match and
                              patterns[match[5]].issubset(pattern) and not patterns[match[1]].issubset(pattern)) :
                            match[6] = patternId
                        elif 9 in match and 6 in match and patternId != match[9] and patternId != match[6]:
                            match[0] = patternId
            
            for number, patternId in match.items():
                for number2, patternId2 in match.items():
                    if number == number2:
                        continue
                    elif patternId == patternId2:
                        print('found a fucking double nique sa mère', number, number2)
            
            outputStr: str = ""
            
            for output in outputs:
                for number, pattern in match.items():
                    if output == patterns[pattern]:
                        outputStr += str(number)
                        break

            outputsList.append(int(outputStr))
        
        print(outputsList)
        return sum(outputsList)

if __name__ == "__main__":
    print(day8_part1_main())