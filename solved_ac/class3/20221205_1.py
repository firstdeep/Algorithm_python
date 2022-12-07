'''
dfs 혹은 bfs를 이용하던지
상화좌우를 확인한다. 거기서 다시 한번
1을 발견할 때 마다 cnt를 +1 해주는 대신 1과 인접한 모든 것을 0으로 바꿔 버린다.

'''
from collections import deque
def organic_cabbage():

    T = int(input())
    D = ((-1,0), (1,0), (0,-1), (0,1))
    answer = []
    for _ in range(T):
        count = 0
        M, N, K = map(int, input().split())
        visited = [[0 for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            a,b = map(int, input().split())
            visited[b][a] = 1

        def bfs(visited, b, a):
            data = deque()
            data.append((b,a))
            visited[b][a] = 0

            while data:
                curr = data.popleft()
                for i in range(4):
                    nr = curr[0] + D[i][0]
                    nc = curr[1] + D[i][1]
                    if (0<=nr<N) and (0<=nc<M):
                        if visited[nr][nc]==1:
                            visited[nr][nc] = 0
                            data.append((nr,nc))


        for b in range(N):
            for a in range(M):
                if visited[b][a] == 1:
                    bfs(visited, b, a)
                    count += 1
        answer.append(count)

    for i in answer:
        print(i)

# 배열을 만들면 시간초가 난다.
# 재귀 함수 혹은 divide and conquer를 해야 된다.
def z_score():
    N,r,c = map(int, input().split())
    data = [i for i in range(0,(2**N)**2)]
    print(data)

# 그리디 문제? NO
# 브루트 force 문제이다. BF문제
# 조합 쓰고 조합을 sort해서 가장 큰 수 pick
from itertools import combinations
def remote():
    current_num = 100
    key = [i for i in range(10)]
    N = int(input())
    M = int(input())
    if M>0:
        broken = list(map(int, input().split()))
        for i in broken:
            key.remove(i)
    else:
        broken = []

    min_count = abs(current_num - N)

    for temp in range(1000000):
        num = str(temp)
        for i in range(len(num)):
            if int(num[i]) in broken: break
            elif i == len(num)-1:
                min_count = min(min_count, abs(N-temp)+len(num))

    print(min_count)

#2178 # bfs 이용하여 문제 풀이
from collections import deque
def miro():
    D = ((-1,0), (1,0), (0,-1), (0,1))
    N,M = map(int, input().split())
    graph = [list(input()) for _ in range(N)]

    def bfs(sr,sc, dr,dc):
        visited = [[False for _ in range(M)] for _ in range(N)]
        data = deque()
        data.append((sr, sc, 1))
        visited[sr][sc] = True

        while data:
            curr = data.popleft()
            if curr[0] == dr and curr[1]==dc: return curr[2]
            for i in range(4):
                nr = curr[0]+D[i][0]
                nc = curr[1]+D[i][1]
                if 0<=nr<N and 0<=nc<M:
                    if not visited[nr][nc] and graph[nr][nc] == '1':
                        visited[nr][nc] = True
                        data.append((nr,nc,curr[2]+1))



    print(bfs(0,0,N-1,M-1))

# 순열 문제이기 때문에 무조건 순환 한다는 가정하에 진행된다.
# 재귀 문제시에 최대 재귀를 늘려줘야 한다?.. 해당 부분 찾아보기

import sys
sys.setrecursionlimit(2000)
def cycle():
    T = int(input())
    for _ in range(T):
        answer = 0
        N = int(input())
        data = [0] + list(map(int, input().split()))
        visited = [True] + [False]*N

        def dfs(node):
            visited[node] = True
            next = data[node]
            if not visited[next]:
                dfs(next)


        for i in range(1, N+1):
            if not visited[i]:
                dfs(i)
                answer +=1

        print(answer)

def recycle():
    A, P = map(int, input().split())
    nums = [A]
    while True:
        temp = 0
        for s in str(nums[-1]):
            temp += int(s) ** P
        if temp in nums:
            break

        nums.append(temp)

    print(nums.index(temp))

# DFS 문제로 풀기로
def apart():
    global cnt
    # n의 개수, graph, visited 정의
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    # 입력값을 graph에 기입
    for i in range(n):
        line = input()
        for j, b in enumerate(line):
            graph[i][j] = int(b)

    # 상하좌우 이동 설정
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    # dfs 정의
    def dfs(x, y):
        global cnt  # cnt를 사용하기 위해 global 선언
        visited[x][y] = True
        if graph[x][y] == 1:
            cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    dfs(nx, ny)

    cnt = 0
    housing = []

    # 정의된 dfs를 가지고 graph를 탐색
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                housing.append(cnt)
                cnt = 0

    # 문제 답 도출
    housing.sort()  # 오름차순 정렬
    print(len(housing))
    for i in housing:
        print(i)

if __name__ =='__main__':
    apart()