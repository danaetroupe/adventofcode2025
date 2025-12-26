PATH = 'input.txt'
FOUR = 4

def part1(path=PATH, lines = FOUR):
    numbers = []
    operations = []
    with open(path, 'r') as file:
        for index, line in enumerate(file):
            if index != lines:
                numbers.append(line.split())
            else:
                operations = line.split()
    answer = 0
    for index, operation in enumerate(operations):
        tempAnswer = int(numbers[0][index])
        for number in numbers[1:]:
            if operation == '*':
                tempAnswer *= int(number[index])
            else:
                tempAnswer += int(number[index])
        answer += tempAnswer
    print(answer)

def part2(path=PATH, numLines = FOUR):
    lines = []
    operations = []
    with open(path, 'r') as file:
        for index, line in enumerate(file):
            if index != numLines:
                lines.append(line.rstrip('\n'))
            else:
                operations = line
    answer = 0
    numbers = []
    currOperation = None
    for i in range(len(lines[0])):
        if operations[i] != ' ': # Reset
            if len(numbers) > 0:
                tempAnswer = int(numbers[0])
                for number in numbers[1:]:
                    if currOperation == '*':
                        tempAnswer *= number
                    else:
                        tempAnswer += number
                answer += tempAnswer
            numbers = []
            currOperation = operations[i]
        number = ''
        for line in lines:
            if line[i] != ' ':
                number += line[i]
        if number != '':
            numbers.append(int(number))
    if len(numbers) > 0:
        tempAnswer = int(numbers[0])
        for number in numbers[1:]:
            if currOperation == '*':
                tempAnswer *= number
            else:
                tempAnswer += number
        answer += tempAnswer
    print(answer)
        
part1()
part2()