from collections import deque
import math
def wall():
    # 해당 방법은 시간초과 발생
    N,M = map(int, input().split())
    graph = [list(map(int,input()))for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(x,y):
        q = deque()
        q.append([x,y,1])
        visited = [[False]*M for _ in range(N)]
        visited[x][y] = True
        while q:
            xx,yy,cnt = q.popleft()
            if xx==N-1 and yy==M-1:
                return cnt
            for i in range(4):
                nx = xx + dx[i]
                ny = yy + dy[i]
                if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and graph[nx][ny]==0:
                        visited[nx][ny] = True
                        q.append([nx,ny,cnt+1])

    result = math.inf
    bfs_output = bfs(0,0) # 1을 제거하지 않고 시도
    if bfs_output is not None:
        result = min(result, bfs_output)

    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                graph[i][j]=0
                bfs_output = bfs(0, 0)  # 1을 제거하지 않고 시도
                if bfs_output is not None:
                    result = min(result, bfs_output)
                graph[i][j]=1

    if result == math.inf:
        print(-1)
    else:
        print(result)

from collections import deque
def wall_re():
    N, M = map(int, input().split())
    graph = [list(map(int, input())) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs():
        q = deque()
        q.append([0,0,0])
        visited = [[[0]*2 for i in range(M)] for _ in range(N)]
        visited[0][0][0] = 1
        while q:
            x,y,crash = q.popleft()
            if x == N-1 and y == M-1:
                return visited[x][y][crash]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 0 and visited[nx][ny][crash] == 0:
                        q.append([nx,ny,crash])
                        visited[nx][ny][crash] = visited[x][y][crash] + 1
                    if graph[nx][ny] == 1 and crash ==0: # 딱 한번만 해야 하니까 다음과 같이 구성
                        q.append([nx,ny,crash+1])
                        visited[nx][ny][crash+1] = visited[x][y][crash] + 1
        return -1

    print(bfs())

if __name__ =="__main__":
    wall_re()
