# Description: Cycles
# Version: 1.0
# Task 2 - Cycles - Part 1 - 1. All numbers in the range.

if __name__ == "__main__":
    try:
        start = int(input("Enter the start value: "))
        end = int(input("Enter the end value: "))

        for i in range(start, end+1):
                print(i)
    except ValueError:
        print("Please enter a valid number")