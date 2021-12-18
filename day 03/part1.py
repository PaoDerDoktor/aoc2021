def day3_part1_main():
    with open("day 3/inputs.txt", 'r') as inFile:
        report: list[str] = inFile.read().splitlines()
        byteLength: int = len(report[0])
        
        gammaStr: str = ""
        epsilonStr: str = ""
        
        for bitPos in range(byteLength):
            zeroes: int = sum([1 for byte in report if byte[bitPos]=="0"])
            gammaStr+=str(int(zeroes>len(report)/2))
            epsilonStr+=str(int(zeroes<=len(report)/2))
        
        return int(gammaStr, 2)*int(epsilonStr, 2)

if __name__ == '__main__':
    print(day3_part1_main())
    