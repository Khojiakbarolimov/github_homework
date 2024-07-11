n = int(input("elementlar soni: "))
numbers = []

for i in range(n):
    numbers.append(int(input("Son kiriting: ")))

for i in range(1, len(numbers)):
    if numbers[i-1] > 0 and numbers[i] > 0:
        print(numbers[i-1], numbers[i])
    elif numbers[i-1] < 0 and numbers[i] < 0:
        print(numbers[i-1], numbers[i])
    elif numbers[i-1] == 0 and numbers[i] == 0:
        print(numbers[i-1], numbers[i])