N, K, R = map(int, input().split())
length = N
count = 1
while length < R:
    length += length * K / 100
    count += 1

print(count)