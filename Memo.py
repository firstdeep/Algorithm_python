import sys

# n, c = map(int, sys.stdin.readline().rstrip().split())
n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    current = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] >= current + mid:
            count += 1
            current = array[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)

