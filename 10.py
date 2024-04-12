count = 0
prev_temp = 0

while True:
    temp = float(input())
    if temp == 0:
        break
    if prev_temp != 0 and temp < prev_temp:
        count += 1
    prev_temp = temp

print(count)