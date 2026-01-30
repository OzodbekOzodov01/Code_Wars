# Write a function which calculates the average of the numbers in a given array.

# Note: Empty arrays should return 0.

def find_average(numbers):
    sum = 0
    if not numbers:
        return 0
    
    for n in numbers:
        sum += n
    return sum / len(numbers)