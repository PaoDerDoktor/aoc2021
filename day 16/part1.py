def pad(bitStr) -> str:
    while len(bitStr)%4 != 0:
        bitStr = "0"+bitStr
    return bitStr

def parse(packet: str) -> tuple[int, str]: # (version, following of the packet)
    print(f"{packet=}")
    version, packet = int(packet[:3], 2), packet[3:]
    typeId,  packet = int(packet[:3], 2), packet[3:]
    
    if typeId == 4:
        stop = False
        while not stop:
            if packet[0] == "0":
                stop = True
            packet = packet[5:]
        return version, packet
    
    lengthType, packet = int(packet[0], 2), packet[1:]
    
    if lengthType == 0:
        bitLength,  packet = int(packet[:15], 2), packet[15:]
        subPackets, packet = packet[:bitLength], packet[bitLength:]
        
        subTotal: int = 0
        while subPackets:
            subValue, subPackets = parse(subPackets)
            subTotal += subValue
        return version + subTotal, packet
    else:
        subsAmount, packet = int(packet[:11], 2), packet[11:]
        
        subTotal: int = 0
        for _ in range(subsAmount):
            subValue, packet = parse(packet)
            subTotal += subValue
        return version + subTotal, packet
    
def day16_part1_main() -> int:
    with open("day 16/inputs.txt", 'r') as inFile:
        bitSequence: str = pad(bin(int(inFile.read(), 16))[2:])
        return parse(bitSequence)[0]


if __name__ == "__main__":
    print(day16_part1_main())
        