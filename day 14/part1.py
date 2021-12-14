def day13_part1_main() -> int:
    with open("day 14/inputs.txt", 'r') as inFIle:
        initSequence, rawRules  = inFIle.read().split("\n\n")
        initSequence = initSequence.strip()
        
        rules: dict[tuple[str, str], str] = {}
        for rawRule in rawRules.split("\n"):
            ruleIn, ruleOut = rawRule.split(" -> ")
            rules[(ruleIn[0], ruleIn[1])] = ruleOut
        
        sequence: str = initSequence
        for _ in range(10):
            nextSequence: list[str] = []
            for i in range(len(sequence)-1):
                inElements: tuple[str, str] = (sequence[i], sequence[i+1])
                nextSequence.append(sequence[i])
                if inElements in rules:
                    nextSequence.append(rules[inElements])
            nextSequence.append(sequence[-1])
            sequence = "".join(nextSequence)
        
        mostFrequentCount:  int = sequence.count(max(set(sequence), key=sequence.count))
        leastFrequentCount: int = sequence.count(min(set(sequence), key=sequence.count))
        
        return mostFrequentCount - leastFrequentCount
    
if __name__ == "__main__":
    print(day13_part1_main())