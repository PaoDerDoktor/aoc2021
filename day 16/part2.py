from math import prod

def pad(bitStr) -> str:
    while len(bitStr)%4 != 0:
        bitStr = "0"+bitStr
    return bitStr

def parse(packet: str) -> tuple[int, str]: # (version, following of the packet)
    version, packet = int(packet[:3], 2), packet[3:]
    typeId,  packet = int(packet[:3], 2), packet[3:]
    
    if typeId == 4:
        stop = False
        total: str = ""
        while not stop:
            if int(packet[0], 2) == 0:
                stop = True
            total += packet[1:5]
            packet = packet[5:]
        return int(total, 2), packet
    
    lengthType, packet = int(packet[0], 2), packet[1:]
    
    subPacketsList: list[int] = []
    if lengthType == 0:
        bitLength,  packet = int(packet[:15], 2), packet[15:]
        subPackets, packet = packet[:bitLength], packet[bitLength:]
        
        while subPackets:
            subValue, subPackets = parse(subPackets)
            subPacketsList.append(subValue)
    else:
        subsAmount, packet = int(packet[:11], 2), packet[11:]
        
        for _ in range(subsAmount):
            subValue, packet = parse(packet)
            subPacketsList.append(subValue)
    
    if typeId == 0:
        return sum(subPacketsList), packet
    elif typeId == 1:
        return prod(subPacketsList), packet
    elif typeId == 2:
        return min(subPacketsList), packet
    elif typeId == 3:
        return max(subPacketsList), packet
    # Skipping 4, already done
    elif typeId == 5:
        return int(subPacketsList[0] > subPacketsList[1]),  packet
    elif typeId == 6:
        return int(subPacketsList[0] < subPacketsList[1]),  packet
    else: # 7
        return int(subPacketsList[0] == subPacketsList[1]), packet
    
def day16_part1_main() -> int:
    with open("day 16/inputs.txt", 'r') as inFile:
        hexaSequence = inFile.read()
        bitSequence: str = bin(int(hexaSequence, 16))[2:]
        i: int = 0
        while hexaSequence[i] == "0":
            bitSequence = "0000"+bitSequence
            i += 1
        
        return parse(pad(bitSequence))[0]


if __name__ == "__main__":
    print(day16_part1_main())
        