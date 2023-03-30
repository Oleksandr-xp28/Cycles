# Description: Cycles
# Version: 1.0

if __name__ == "__main__":
    try:
        begin = int(input('Enter a begin: ')) 
        end = int(input('Enter an end: '))

        for i in range(begin, end+1):
            if i % 3 == 0 and i % 5 == 0:
                print("Fizz Buzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    except ValueError:
        print("Please enter a valid number")
