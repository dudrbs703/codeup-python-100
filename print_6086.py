# print_6086.py

n = int(input())
count = 0
result = 0
while True:
    count += 1
    result += count
    if result >= n:
        break

print(result)
