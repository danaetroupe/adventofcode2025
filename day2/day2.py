# Parse each line and get the range of ids
# For each line of input, divide length by 2.
# Only even numbers can be invalid
# Generate all invalid numbers starting from the first valid id and stop if it exceeds
# Add to final code
# Return final code

PATH = 'input.txt'

def part1(path):
    final_code = 0
    with open(path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            for value in values:
                nums = value.split('-')
                startNum = int(nums[0])
                endNum = int(nums[1])
                
                for i in range(startNum, endNum + 1, 1):
                    string = str(i)
                    if len(string) % 2 == 1:
                        continue
                    subset = int(len(string) / 2)
                    if string[0:subset] == string[subset:]:
                        final_code += i 
        
    return final_code

def part2(path):
    final_code = 0
    with open(path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            for value in values:
                nums = value.split('-')
                startNum = int(nums[0])
                endNum = int(nums[1])
                
                for i in range(startNum, endNum + 1, 1):
                    string = str(i)
                    subset = 1
                    while(subset <= int(len(string) / 2)):
                        lastVal = string[0:subset]
                        # Divide up equal parts
                        isEqual = True
                        # Determine if it is equal subsets
                        for j in range(subset,len(string)-subset+1, subset):
                            val = string[j:j+subset]
                            isEqual = val == lastVal
                            if isEqual:
                                lastVal = val
                            else:
                                break
                        if isEqual:
                            final_code += i # Add qualifying number
                            print(i)
                            break # No need to continue checking
                        subset += 1
                        while((len(string) % subset) != 0):
                            subset += 1
                        
    return final_code

def main(path = PATH):
    print(part1(path))
    print(part2(path))    
        
main()