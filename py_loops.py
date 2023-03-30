# Description: Cycles
# Version: 1.0
# Task 2 - Cycles - Part 1 - 3. All numbers in multiples of 7.

if __name__ == "__main__":
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        for i in range(start, end+1):
            if i % 5 == 0:
                print(i)
        print("The end")
    except ValueError:
        print("Please enter a valid number")