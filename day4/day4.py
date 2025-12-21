PATH = 'input.txt'
VALUE = '@'

def part2(path = PATH):
    count = 0
    matrix = []
    with open(path, 'r') as file:
        for line in file:
            # Read in file
            row = line.strip()
            matrix.append(str(row))
    tempCount = cleanMatrix(matrix)
    while tempCount > 0:
        count += tempCount
        tempCount = cleanMatrix(matrix)
    return count
    
def cleanMatrix(matrix):
    count = 0
    columnLength = len(matrix[0])
    rowLength = len(matrix)
    rowNum = 0
    colNum = 0
    while rowNum < rowLength:
        colNum = 0
        while colNum < columnLength:
            if matrix[rowNum][colNum] == VALUE:
                adjacent = 0
                # 1
                if rowNum > 0 and colNum > 0 and matrix[rowNum-1][colNum-1] == VALUE:
                    adjacent += 1
                # 2
                if rowNum > 0 and matrix[rowNum-1][colNum] == VALUE:
                    adjacent += 1
                # 3
                if rowNum > 0 and colNum < columnLength - 1 and matrix[rowNum-1][colNum+1] == VALUE:
                    adjacent += 1
                # 4
                if colNum > 0 and matrix[rowNum][colNum-1] == VALUE:
                    adjacent += 1
                # 5
                if colNum < columnLength - 1 and matrix[rowNum][colNum+1] == VALUE:
                    adjacent += 1
                # 6
                if rowNum < rowLength - 1 and colNum > 0 and matrix[rowNum+1][colNum-1] == VALUE:
                    adjacent += 1
                # 7
                if rowNum < rowLength - 1 and matrix[rowNum+1][colNum] == VALUE:
                    adjacent += 1
                # 8
                if rowNum < rowLength - 1 and colNum < columnLength - 1 and matrix[rowNum+1][colNum+1] == VALUE:
                    adjacent += 1
                if adjacent < 4:
                    value = matrix[rowNum]
                    matrix[rowNum] = value[:colNum] + '.' + value[colNum+1:]
                    count += 1
            colNum += 1
        rowNum += 1
    return count
        
def main():
    print(part2())
    
main()