from copy import deepcopy

def day3_part1_main():
    with open("day 3/inputs.txt", 'r') as inFile:
        report: list[str] = inFile.read().splitlines()
        byteLength: int = len(report[0])
        
        co2: list[str] = deepcopy(report)
        oxy: list[str] = deepcopy(report)
        
        while len(co2) + len(oxy) != 2:
            for bitPos in range(byteLength):
                if len(co2)>1:
                    zeroesCO2: int = sum([1 for byte in co2 if byte[bitPos]=="0"])
                    leastCommonCO2: str = str(int(zeroesCO2>len(co2)/2))
                    co2 = [byte for byte in co2 if byte[bitPos] == leastCommonCO2]
                if len(oxy)>1:
                    zeroesOxy: int = sum([1 for byte in oxy if byte[bitPos]=="0"])
                    mostCommonOxy: str = str(int(zeroesOxy<=len(oxy)/2))
                    oxy = [byte for byte in oxy if byte[bitPos] == mostCommonOxy]

    return int(co2[0], 2)*int(oxy[0], 2)
        
if __name__ == '__main__':
    print(day3_part1_main())