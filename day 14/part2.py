def get_next_pairs(pairs: dict[tuple[str, str], int], rules: dict[tuple[str, str], str]) -> dict[tuple[str, str], int]:
    nextPairs: dict[tuple[str, str], int] = {}
    for pair in pairs:
        if pair in rules:
            if (pair[0], rules[pair]) in nextPairs:
                nextPairs[(pair[0], rules[pair])] += pairs[pair]
            else:
                nextPairs[(pair[0], rules[pair])]  = pairs[pair]
            if (rules[pair], pair[1]) in nextPairs:
                nextPairs[(rules[pair], pair[1])] += pairs[pair]
            else:
                nextPairs[(rules[pair], pair[1])]  = pairs[pair]
        elif pair in nextPairs:
            nextPairs[pair] += pairs[pair]
        else:
            nextPairs[pair]  = pairs[pair]
    return nextPairs
                
def get_count(pairs: dict[tuple[str, str], int]) -> dict[str, int]:
    count: dict[str, int] = {}
    for pair in pairs:
        if pair[0] in count:
            count[pair[0]] += pairs[pair]
        else:
            count[pair[0]]  = pairs[pair]
        if pair[1] in count:
            count[pair[1]] += pairs[pair]
        else:
            count[pair[1]]  = pairs[pair]
    return count            

def day13_part2_main() -> int:
    with open("day 14/inputs.txt", 'r') as inFIle:
        initSequence, rawRules  = inFIle.read().split("\n\n")
        initSequence = initSequence.strip()
        
        pairs: dict[tuple[str, str], int] = {}
        for i in range(len(initSequence)-1):
            pair: tuple[str, str] = (initSequence[i], initSequence[i+1])
            if pair in pairs:
                pairs[pair] += 1
            else:
                pairs[pair] = 1
        
        rules: dict[tuple[str, str], str] = {}
        for rawRule in rawRules.split("\n"):
            ruleIn, ruleOut = rawRule.split(" -> ")
            rules[(ruleIn[0], ruleIn[1])] = ruleOut
        
        for _ in range(40):
            pairs = get_next_pairs(pairs, rules)
        
        count: list[int] = list(get_count(pairs).values())
        
        return int(max(count)/2) - int(min(count)/2)+1
    
if __name__ == "__main__":
    print(day13_part2_main())