count = 0
numbers = []
for num in range(100, 1000):
    if num % 17 == 0:
        count += 1
        numbers.append(num)
for i in numbers:
    print(i,end=' ')
print()
print("Количество трехзначных чисел, делящихся на 17:", count)