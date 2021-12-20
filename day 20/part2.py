from sys import maxsize
from copy import deepcopy


Map = list[list[str]]


def get_map_repr(map: Map) -> str:
    minJ: int = 0
    maxJ: int = len(map)
    minI: int = 0
    maxI: int = len(map[0])
    
    mapRepr: str = ''
    for j in map:
        for i in j:
            mapRepr += i
        mapRepr += "\n"
    
    return f"{minJ} <= j < {maxJ} --- {minI} <= i < {maxI}\n" + mapRepr

def pad_map(map: Map, step: int, enhanceAlgorithm: str) -> Map:
    padTop:    bool = '#' in map[ 0]
    padBottom: bool = '#' in map[-1]
    padLeft:   bool = False
    padRight:  bool = False
    
    padChar: str = ''
    if step == 0:
        padChar = '.'
    else:
        padChar = enhanceAlgorithm[0] if step%2 != 0 else enhanceAlgorithm[-1]
    
    for line in map:
        if line[ 0] == '#':
            padLeft = True
        if line[-1] == '#':
            padRight = True
    
    resultMap: Map = []
    if padTop:
        dotsAmount: int = len(map[0])
        if padLeft:
            dotsAmount += 1
        if padRight:
            dotsAmount += 1
        resultMap.append([padChar for _ in range(dotsAmount)])
    
    for line in map:
        lineToPaste: list[str] = deepcopy(line)
        if padLeft:
            lineToPaste = [padChar]+lineToPaste
        if padRight:
            lineToPaste = lineToPaste+[padChar]
        resultMap.append(lineToPaste)
    
    if padBottom:
        dotsAmount: int = len(map[0])
        if padLeft:
            dotsAmount += 1
        if padRight:
            dotsAmount += 1
        resultMap.append([padChar for _ in range(dotsAmount)])

    return resultMap
            
def get_new_pixel_values(map: Map, step: int, enhanceAlgorithm: str) -> Map:
    paddedMap: Map = pad_map(map, step, enhanceAlgorithm)
    resultMap: Map = []
    for lineId, line in enumerate(paddedMap):
        resultLine: list[str] = []
        for colId, col in enumerate(line):
            bitString: str= ''
            for a in range(lineId-1, lineId+2):
                for b in range(colId-1, colId+2):
                    if a < 0 or a >= len(paddedMap) or b < 0 or b >= len(line):
                        bitChar: str = ''
                        if step == 0:
                            bitChar == '.'
                        else:
                            bitChar = enhanceAlgorithm[0] if step%2 != 0 else enhanceAlgorithm[-1]
                        bitString += '1' if bitChar == '#' else '0'
                        continue
                    else:
                        bitString += '1' if paddedMap[a][b] == '#' else '0'
            resultLine.append(enhanceAlgorithm[int(bitString, 2)])
        resultMap.append(resultLine)
    return resultMap
                        
def enhance(map: Map, enhancementAlgorithm: str, iterations: int) -> Map:
    returnMap = deepcopy(map)
    for it in range(1, iterations+1):
        returnMap = get_new_pixel_values(returnMap, it-1, enhancementAlgorithm)
    return returnMap
    
def get_lit_amount(map: Map) -> int:
    total: int = 0
    for line in map:
        total += sum([1 for col in line if col=='#'])
    return total

def day20_part1_main():
    with open("day 20/inputs.txt", 'r') as inFile:
        inFilesLines: list[str] = inFile.readlines()
        enhancementAlgorithm: str = inFilesLines[0].strip()
        
        map: Map = []
        for j, line in enumerate(inFilesLines[2:]):
            map.append([])
            for i, col in enumerate(line.strip()):
                map[-1].append(col)
                
        map = enhance(map, enhancementAlgorithm, 50)
        
        return get_lit_amount(map)

if __name__ == "__main__":
    print(day20_part1_main())