def bfs(graph: dict[str, list[str]], source: str, target: str) -> list[list[str]]:
    pathsQueue: list[list[str]] = [[source]]
    finalPaths: list[list[str]] = []
    
    while len(pathsQueue) != 0:
        currentPath = pathsQueue.pop()
        
        if currentPath[-1] == target:
            finalPaths.append(currentPath)
            continue # ?
        
        for neighbor in graph[currentPath[-1]]:
            if (neighbor.isupper()) or (neighbor.islower() and not neighbor in currentPath):
                pathsQueue.append(currentPath[:]+[neighbor])
    
    return finalPaths

def day12_part1_main() -> int:
    with open("day 12/inputs.txt", 'r') as inFile:
        graph: dict[str, list[str]] = dict()
        for line in inFile.readlines():
            lineStart, lineEnd = line.strip().split('-')
            if not lineStart in graph:
                graph[lineStart] = [lineEnd]
            else:
                graph[lineStart].append(lineEnd)
            if not lineEnd in graph:
                graph[lineEnd] = [lineStart]
            else:
                graph[lineEnd].append(lineStart)
        
        paths: list[list[str]] = bfs(graph, "start", "end")
        
        return len(paths)
    
if __name__ == "__main__":
    print(f"\n{day12_part1_main()=}")