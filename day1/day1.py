INPUT = 'input.txt'

def main():
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')

def part1(path=INPUT):
    password = 0
    dial = 50
    with open(path, 'r') as file:
        for line in file:
            # parse
            code = line.strip()
            direction = code[0].upper()
            # determine direction
            multipler = 1 if direction == 'R' else -1
            # move dial
            num = int(code[1:]) * multipler
            dial = (dial + num) % 100
            dial = dial if dial >= 0 else dial + 100
            if dial == 0:
                password += 1
    
    return password

def part2(path=INPUT):
    password = 0
    dial = 50
    with open(path, 'r') as file:
        for line in file:
            # parse
            code = line.strip()
            print(code)
            direction = code[0].upper()
            # determine direction
            multipler = 1 if direction == 'R' else -1
            # move dial
            num = int(code[1:]) * multipler
            
            # Count how many times the dial lands on 0
            large_dial = dial + num
            print(f'Large dial: {large_dial}')
            if large_dial > 99:
                # Add to password the amount of times it is divisible by 100
                password += large_dial // 100
            elif large_dial <= 0:
                # Add one to password for touching 0
                # Absolute value of large_dial to find how many times it crosses 0
                # Divide by 100 to find how many times it crosses 0
                password += (-large_dial // 100)
                if dial != 0: # If it starts on 0, don't add an extra
                    password += 1
                
            print(f'Password: {password}')
            # Calculate new dial
            dial = large_dial % 100
            dial = dial if dial >= 0 else dial + 100
            print(f'New dial: {dial}\n')
            
    return password

main()
            