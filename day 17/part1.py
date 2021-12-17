def day17_part1_main() -> int:
    with open("day 17/inputs.txt", 'r') as inFile:
        rawRanges: str = inFile.read()[13:]
        xRawRange, yRawRange = rawRanges.split(', ')
        yRange: list[int] = list(range(int(yRawRange.split('..')[0][2:]), int(yRawRange.split('..')[1]))) + [int(yRawRange.split('..')[1])]
        
        return int(yRange[0]*(yRange[0]+1)/2)
        
        

if __name__ == "__main__":
    print(day17_part1_main())