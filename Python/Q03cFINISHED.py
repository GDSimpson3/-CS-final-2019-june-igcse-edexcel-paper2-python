# Q03c

# Write your code below this line

inputNumber = int(input('Please enter an Integer between 1 and 50 (inclusive): '))

while not (inputNumber < 1 or inputNumber > 50):
    print(f'Square of your number is: {inputNumber ** 2}')
    print (f'Cube of your number is: {inputNumber ** 3}')
    inputNumber = int(input('Please enter another number between 1 and 50 (inclusive) to find its square and cube: '))

