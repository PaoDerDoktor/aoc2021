Flags =   tuple[bool, bool, bool, bool, bool, bool, bool] # 7-digit-display as flags for `a`, `b`, `c`, `d`, `e`, `f` and `g`.

SEGMENTS: tuple[str,  str,  str,  str,  str,  str,  str]  = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

def day8_part1_main() -> int:
    with open("day 8/inputs.txt", 'r') as inFile:
        displays: list[list[Flags]] = []
        for line in inFile.readlines():
            _, rawOutputs = line.split(' | ')
            outputs: list[Flags] = []
            for digit in rawOutputs.split():
                outputs.append(tuple([True if seg in digit else False for seg in SEGMENTS])) # type: ignore --- Pylance considers length as underterminable
            displays.append(outputs)
        
        counter: dict[int, int] = {1:0, 4:0, 7:0, 8:0}
        
        print(displays)
        
        for display in displays:
            for digit in display:
                if sum(digit) == 2:
                    counter[1] += 1
                elif sum(digit) == 4:
                    counter[4] += 1
                elif sum(digit) == 3:
                    counter[7] += 1
                elif sum(digit) == 7:
                    counter[8] += 1
                    
        return sum(counter.values())
    
if __name__ == "__main__":
    print(day8_part1_main())