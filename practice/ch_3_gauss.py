# This program calculates the sum of numbers from 0 to upperNumber using a loop.
upperNumber = int(input('Add up to what number? '))
total = 0
for num in range(upperNumber + 1):
    total = total + num
    print('num is:', num, 'total is:', total)
print(total)  