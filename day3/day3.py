PATH = 'input.txt'

def part1(path=PATH):
    total_output = 0
    with open(path, 'r') as file:
        for line in file:
            bank = line.strip()
            # Find largest value that isn't the last digit (starting from right)
            maxValue = bank[0]
            maxIndex = 0
            for i in range(1, len(bank)-1, 1):
                val = bank[i]
                if val > maxValue:
                    maxValue = val
                    maxIndex = i
            # Find second largest value from that index onwards
            secondValue = bank[maxIndex+1]
            for i in range(maxIndex+1, len(bank), 1):
                val = bank[i]
                if val > secondValue:
                    secondValue = val
            # Turn that combined into integer value
            total_output += int(maxValue+secondValue)
    return total_output

def part2(path=PATH):
    total_output = 0
    with open(path, 'r') as file:
        for line in file:
            bank = line.strip()
            completeVal = ""
            prevIndex = -1
            for buffer in range (11, -1, -1):
                maxValue = '0'
                for i in range(prevIndex+1, len(bank)-buffer, 1):
                    val = bank[i]
                    if val > maxValue:
                        maxValue = val
                        prevIndex = i
                    if maxValue == '9':
                        break # Early out to run faster
                completeVal += maxValue
            total_output += int(completeVal)
    return total_output

def main():
    print(part1())
    print(part2())

main()