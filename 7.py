number = int(input())
flag = True

while number > 1:
    if number % 2 != 0:
        flag = False
        break
    number //= 2

if flag:
    print("верно")
else:
    print("неверно")