start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

for i in range(start, end):
    if i % 7 == 0:
        print(i)
