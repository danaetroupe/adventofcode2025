PATH = 'input.txt'
TEST = 'test.txt'

def part1(path=PATH):
    positions = set()
    timesSplit = 0
    with open(path, 'r') as file:
        for line in file:
            pos = line.find('S')
            positions.add(pos)
            break
        for line in file:
            newPositions = set()
            discardPositions = []
            for pos in positions:
                if line[pos] == '^':
                    discardPositions.append(pos)
                    timesSplit += 1
                    if pos > 0 and line[pos-1] != '^':
                        newPositions.add(pos-1)
                    if pos < len(line) and line[pos+1] != '^':
                        newPositions.add(pos+1)
            for pos in newPositions:
                positions.add(pos)
            for pos in discardPositions:
                positions.discard(pos)
                        
    print(timesSplit)

def split(pos, lines):
    timesSplit = 0
    for index, line in enumerate(lines):
        if line[pos] == '^':
            if pos > 0 and line[pos-1] != '^':
                timesSplit += split(pos-1, lines[index+1:])
            if pos < len(line) and line[pos+1] != '^':
                timesSplit += split(pos+1, lines[index+1:])
            timesSplit += 1
            break
    return timesSplit
    
# def part2(path = PATH):
#     lines = []
#     with open(path, 'r') as file:
#         pos = 0
#         for line in file:
#             pos = line.find('S')
#             break
#         for line in file:
#             lines.append(line)
#         print(split(pos, lines)+1)
        
part1()
# part2()

"""algorithm
keep a list of all downward positions.
for each line, keep track of where splitters are.
for each line, if splitter location is on downward position, add a new line -1 and +1 IF there is no splitter there
add +1 for each splitter touched
check next line 
"""