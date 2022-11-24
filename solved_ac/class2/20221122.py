"""
백준 연구소 문제
DFS 분류
핵심 포인트1: 안전 영역의 최댓값 출력
핵심 포인트2: 값 저장 하는 법
핵심 포인트3: BF를 통해 3개 벽을 세울 수 있는 모든 경우 고려
핵심 포인트4: BFS를 통해 바이러스의 총 개수를 구한다.
"""
import math
from itertools import combinations, chain
import copy

def research():
    n,m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    zero = []

    # zero가 있는 index 찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                zero.append((i,j))

    # combination 으로 모든 조합 구하기
    # combination을 적용했으면 list로 변경해 주어야 한다.
    combi = list(combinations(zero, 3))

    def safe(change, graph2):
        q = []
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        result = 0
        for x, y in change:
            graph2[x][y] = 1 # 조합에서 값을 찾아으니 해당 값을 1로 변경한 후에 2를 퍼트려야 한다.
        for nn in range(n):
            for mm in range(m):
                if graph2[nn][mm] == 2: # 저장되 있는 2를 Q에 담에 두고
                    q.append((nn, mm))
                    while q: # 해당 Q를 반복한다.
                        xx, yy = q.pop() # Q가 pop되면서
                        for i in range(4):
                            nx = xx + dx[i]
                            ny = yy + dy[i]
                            if 0<= nx < n and 0<= ny < m and graph2[nx][ny] == 0:
                                graph2[nx][ny] = 2
                                q.append((nx, ny))
        for k in range(n):
            result += graph2[k].count(0)

        a = list(chain.from_iterable(graph2)).count(0) # 위와 동일한 맥락
        b = sum(graph2, []).count(0) # 위와 동일한 맥락

        return result

    answer = 0
    for i in combi:
        temp = safe(i, copy.deepcopy(graph))
        if answer < temp:
            answer = temp

    print(answer)


'''
Class2
랜선 자르기 1654 
핵심 포인트: 이진탐색 문제? 반으로 잘라서 확인한다. 끝 
현재는 시간초과 시간 초과하는 것을 for 문에서 많이 잡아먹고 있다는 건데.... 
'''
import sys
def cutting_lan():
    K, N = map(int, input().split())
    lan = [int(sys.stdin.readline()) for _ in range(K)]

    min_value = 1
    max_value = max(lan)

    while min_value <=max_value:
        mid = (min_value + max_value) // 2
        cnt = 0
        for i in lan:
            cnt += i // mid

        if cnt>=N:
            min_value = mid + 1
        else:
            max_value = mid - 1

    return max_value


def stack_sort():
    N = int(input())
    in_data = [int(input()) for _ in range(N)]

    count = 1
    flag = 0
    stack = []
    answer = []

    for idx in in_data:
        while count <= idx:
            stack.append(count)
            count = count + 1
            answer.append('+')

        if stack[-1] == idx:
            stack.pop()
            answer.append('-')
        else:
            print('NO')
            flag = 1
            break

    if flag == 0:
        for i in answer:
            print(i)

'''
시간복잡도 문제 가장 중요하다. 
python 에서 list는 시간복잡도는 O(N) 
set은 시간복잡도가 O(1)이다... 
이것을 고려해야 한다. 
https://wiki.python.org/moin/TimeComplexity
'''
def find_number():
    N = int(input())
    a_data = list(map(int, input().split())) # list 를 set으로 바꿔줘야 한다. 어차피 대상은 a_data에서 찾는 것 이기 때문에
    M = int(input())
    b_data = list(map(int, input().split()))

    '''sys를 이용한 입력 받기'''
    # N = int(sys.stdin.readline())
    # a_data = set(map(int, sys.stdin.readline().split()))
    # m = int(sys.stdin.readline())
    # b_data = list(map(int, sys.stdin.readline().split()))

    for idx in b_data:
        if a_data.__contains__(idx):
            print('1')
        else:
            print('0')

'''
소수를 찾는 문제의 경우 범위가 넓을 때 
모두 검사해야 된다면 이중 for 문이 발생할 수 있음 

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1): # 제곱근을 이용하여 소수 찾는 방법 
        if n % i ==0:
            return False
    return True

'''
#에라토스테네스의 체 방법론
import sys, math
def find_decimal(N):
    arr = [True] * (N+1) # 0부터 시작함으로
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(N))+1):
        if arr[i] == True:
            j = 2
            while (i*j) <= N:
                arr[i*j] = False
                j += 1

    return arr


'''
복습 필요 
'''
from collections import deque
def print_q():
    N = int(input())
    answer = []

    for _ in range(N):
        a, b = map(int, input().split())
        q = deque(list(map(int, input().split())))
        idx = deque(list(range(a)))
        cnt = 0

        while q:
            if q[0] == max(q):
                cnt += 1
                q.popleft()
                if idx.popleft() == b:
                    print(cnt)
            else:
                q.append(q.popleft())
                idx.append(idx.popleft())


if __name__ =="__main__":
    print_q()