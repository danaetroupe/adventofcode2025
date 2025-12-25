PATH = 'input.txt'

def mergeElements(element, index, list):
    oldElement = list[index]
    lowerBound = element[0] if element[0] < oldElement[0] else oldElement[0]
    upperBound = element[1] if element[1] > oldElement[1] else oldElement[1]
    list[index] = [lowerBound, upperBound]
    
def inRange(element, r):
    return True if element >= r[0] and element <= r[1] else False
    
def part1(path=PATH):
    fresh = 0
    id_ranges = []
    with open(path, 'r') as file:
        for line in file: # Insertion sort
            if line.find('-') >= 0:
                element = line.split('-')
                element = [int(element[0]), int(element[1])]
                beenInserted = False
                for index, r in enumerate(id_ranges):
                    # check if upper bound is less than lower bound
                    if element[1] < r[0]:
                        # if yes, insert at index below
                        id_ranges.insert(index, element)
                        beenInserted = True
                        break
                    # check if lower bound is greater than upper bound
                    elif element[0] > r[1]:
                        # if yes, continue checking until first condition is true
                        continue
                    else:
                        # if two conditions above aren't true, merge the elements
                        mergeElements(element, index, id_ranges)
                        beenInserted = True
                        break
                # if we reach the end and we have not inserted, insert at end of list
                if not beenInserted:
                    id_ranges.append(element)
            else:
                break
        for line in file:
            low = 0
            high = len(id_ranges) - 1
            target = int(line)

            while low <= high:
                # Calculate middle index (integer division)
                mid = (low + high) // 2
                midValue = id_ranges[mid]
                
                # Check if target is lower than lower bound
                if target < midValue[0]:
                    high = mid - 1
                elif target > midValue[1]:
                    low = mid + 1
                else:
                    fresh += 1
                    break
    return fresh

def part2(path=PATH):
    fresh = 0
    id_ranges = []
    with open(path, 'r') as file:
        for line in file: # Insertion sort
            if line.find('-') >= 0:
                element = line.split('-')
                element = [int(element[0]), int(element[1])]
                beenInserted = False
                for index, r in enumerate(id_ranges):
                    if inRange(element[0], r) or inRange(element[1], r):
                        mergeElements(element, index, id_ranges)
                        beenInserted = True
                        break
                    # check if upper bound is less than lower bound
                    elif element[1] < r[0]:
                        # if yes, insert at index below
                        id_ranges.insert(index, element)
                        beenInserted = True
                        break
                # if we reach the end and we have not inserted, insert at end of list
                if not beenInserted:
                    id_ranges.append(element)
            else:
                break
    # Loop through and merge agian
    index = 0
    length = len(id_ranges)
    while index < length - 1:
        currValue = id_ranges[index]
        nextValue = id_ranges[index+1]
        if (currValue[1] >= nextValue[0]):
            mergeElements(nextValue, index, id_ranges)
            del id_ranges[index+1]
            length = len(id_ranges)
        else:
            index += 1
    for r in id_ranges:
        fresh += (r[1]-r[0]) + 1
    return fresh

print(part1())
print(part2())
"""
ALGORITHM
- We want to sort the id ranges first, combining like terms (if there is any overlap between upper and lower)
- We want to use insertion sort by first indexing the middle and going up or down from there
- Implement this algorithm for building the initial array
- Binary search for finding correct ids
- Once we get to the ids, first index the middle then if it's below lower go down, if it's above upper go up and if it's between divide index by half 

QUESTIONS:
- What do we do if length is odd? ANSWER: Turn index into integer and it should round down. 
- How do we make sure we don't check repeats. ANSWER: Track upper and lower bounds. If they are the same, continue
- How can we test? ANSWER: Make sample dataset and make sure values are expected. Split this into 1) sorting id ranges and 2) checking ids

TEST:
expected ranges:
[3-5][10-20]

valid ids:
5, 11, 17

amount fresh: 3
"""