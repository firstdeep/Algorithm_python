'''
일반적인 큐와 동일하다 하지만
데이터를 삭제할 때 우선순위가 높은 데이터 가장 낮은 데이터 중 하나를 삭제한다.
- 핵심: 큐에서 최소값과 최대 값을 뺄 수 있어야 한다.
그러면 굳이 deque를 써야할 이유가 있을까?
max 값 찾고 index 값 찾은 후에 그것만 삭제해주면 된다.

heapq 사용하기
핵심은

분석 del 에서 O(N)으로 인해 시간 복잡도 문제가 생겼으며,
따라서 heap의 pop을 사용해야 한다. O(1)
'''
import heapq
import sys
def double_queue():
    T = int(sys.stdin.readline())
    for _ in range(T):
        K = int(sys.stdin.readline())
        heap = []
        for _ in range(K):
            a, b = map(str, sys.stdin.readline().split())
            if a =='I':
                heapq.heappush(heap, int(b))
            if a == 'D':
                if int(b) == 1:
                    if len(heap) != 0:
                        del heap[-1] # 여기서 빅O(N)이라 문제가 생기는 것 같다.

                if int(b) == -1:
                    if len(heap) != 0:
                        heapq.heappop(heap)

            # print(heap)

        if len(heap) == 0:
            print('EMPTY')
        else:
            print(max(heap), min(heap))

import sys,heapq
def double_re():
    R = sys.stdin.readline
    P = heapq.heappop
    H = heapq.heappush

    for _ in range(int(R())):
        min_temp=[]; max_temp=[]; V={}
        for i in range(int(R())):
            S = R().split()
            n = int(S[1])
            # dict에는 원래 들어가는 값을
            if S[0]=='I': H(min_temp, n); H(max_temp, -n); V.setdefault(n,0); V[n]+=1
            else:
                T=max_temp if n==1 else min_temp
                while len(T)!=0:
                    t = P(T)*(-1 if n==1 else 1)
                    if V[t]:V[t]-=1; print(V[t]); break
        V = [k for k,v in V.items() if v>0]; V.sort()
        print('EMPTY' if V==[] else '%d %d'%(V[-1], V[0]))

import sys, heapq
def min_heap():
    I = sys.stdin.readline
    Push = heapq.heappush
    Pop = heapq.heappop
    heap = []
    for _ in range(int(I())):
        num = int(I())
        if num == 0:
            if len(heap)==0: print('0')
            else: print(Pop(heap))
        else:
            Push(heap, num)

'''
3으로 나눠 지는지 
2로 나눠 지는지 확인 
count 선언하고 
시간제한이 0.15 이다. 최소 공배수 최대 공약수 이용해야 될 것 같다. 
다이나믹 프로그래밍 문제이다. 동적 계획법을 이용해 풀어야 하는 문제... 
그리디도 아니다. 그리디는 끝까지 반례없이 적용가능해야 한다. 
DP문제는 memorization기법 사용 
'''
import sys
def make_one():
    N = int(sys.stdin.readline())
    # dp에 저장되는 것은 최소값이 저장된다.
    dp = [0]*(N+1) # DP를 저장하는 list이다. memorizaiton기법을 사용하고 N이 의미하는 것은 N을 만들기 까지의 최소의 개수를 의미한다.
    for i in range(2, N+1): # 시간 복잡도는 O(N)으로 된다.
        dp[i] = dp[i-1] + 1
        if i%2 ==0:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i%4 ==0:
            dp[i] = min(dp[i], dp[i//3]+1)

    print(dp[N])


# dfs 및 bfs 둘다로 해결 가능하도록 해야 한다.
import sys
from collections import deque
def ice():
    global cnt
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    N,M = map(int, sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for i in range(N):
        data = list(map(int,input()))
        for j in range(M):
            if data[j] == 1: graph[i][j] = 1


    def dfs_re(x,y):
        global cnt
        visited[x][y] = True
        cnt+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny]==False and graph[nx][ny]==0:
                    dfs_re(nx,ny)

    def bfs(x,y):
        global cnt
        data=deque()
        data.append((x,y))
        visited[x][y] = True # 처음에 들어오자 마자 진행해 주고 재귀를 쓰지 않기 때문에 while에서도 진행
        while data:
            curr = data.popleft()
            for i in range(4):
                nx = curr[0] + dx[i]
                ny = curr[1] + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny] == False and graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        graph[nx][ny] = graph[curr[0]][curr[1]] + 1 # 최단 경로 구하는 방법
                        data.append((nx, ny))

    cnt = 0
    all_item = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j]==False:
                bfs(i,j)
                all_item.append(cnt)
                cnt = 0

    print(graph)


'''
2468번 문제 
https://www.acmicpc.net/problem/2468
dfs and bfs 모두 풀 수 있는 문제이다. 중요한 것은 꺽이지 않는 마음? 
각설하고 N의 크기가 100 이하면 제곱하면 10000제곱이 맞음? 
DFS로 작성해보고 BFS로 작성해보고 걸리는 시간을 파악해 보자 
DFS로 가기로 하자 
- 그래프의 모든 정점을 방문해야될 때는 어떤 것도 상관없음 
- 경로의 특징을 저장해야 되는 문제 (가는 길에 뭐보다 작은 것이 있으면 안된다 할떄는 DFS를) 
- 최단 거리 찾는 문제 미로 찾기 등은 BFS 
- 검색 대상 그래프가 크다면 DFS를 고려하기 

문제 잘 읽기 안전한 영역의 최대 개수를 출력해야 한다. 따라서 max를 구해서 해당 부분까지 계속 dfs를 통해 구해줘야 한다. 
'''
import sys
sys.setrecursionlimit(15000)
def safe():
    N = int(input())
    graph = []

    for i in range(N):
        graph.append(list(map(int, input().split())))
    max_num = max(sum(graph, []))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def dfs(x,y,h):
        visited[x][y] = True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==False and graph[nx][ny]>=h: #부등호.....
                    # visited[x][y] = True
                    dfs(nx,ny,h)

    temp = 0
    for h in range(1,max_num+1):
        cnt = 0
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j]==False and graph[i][j]>=h:
                    # visited[i][j] = True
                    dfs(i,j,h)
                    cnt +=1

        temp = max(temp, cnt)

    print(temp)


if __name__=="__main__":
    safe()