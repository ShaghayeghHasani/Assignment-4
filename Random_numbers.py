import random
n = int(input("Enter a number between 0 and 100: "))

numbers =[]
for i in range(n):
    num = random.randint(0,100)
    while num in numbers:
        num = random.randint(0,100)

    numbers.append(num)

print(numbers)