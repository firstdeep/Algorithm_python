# 그리디 문제 - 탐색(BFS, DFS) - 동적 프로그래밍 문제
# https://www.acmicpc.net/workbook/view/4380

'''
시간복잡도는
for 문 만큼만 영향을 받는다.
18185번
항상 반례를 생각해야 된다.
4
1 2 1 1 의 최소 는 12이다.
'''

def buy_triple(idx):
    global total_count
    k = min(arr[idx: idx + 3])
    arr[idx] -= k
    arr[idx + 1] -= k
    arr[idx + 2] -= k
    total_count += 7 * k


def buy_double(idx):
    global total_count
    k = min(arr[idx: idx + 2])
    arr[idx] -= k
    arr[idx + 1] -= k
    total_count += 5 * k


def buy_each(idx):
    global total_count
    total_count += 3 * arr[idx]

N = int(input())
arr = list(map(int, input().split())) +[0,0]

total_count = 0

for i in range(0,N):
    if arr[i+1]>arr[i+2]:
        k = min(arr[i], arr[i+1]-arr[i+2])
        arr[i] -= k
        arr[i+1] -= k
        total_count += 5*k

        buy_triple(i)
    else:
        buy_triple(i)
        buy_double(i)
    buy_each(i)

print(total_count)
