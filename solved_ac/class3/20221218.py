from collections import deque



N, M, R, C = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0
all = 0

def bfs(start):
    visited = [[False for _ in range(M)] for _ in range(N)]
    global result, all
    q = deque()
    q.append([start[0],start[1], 0])
    visited[start[0]][start[1]] = True
    while q:
        # print(q)
        x,y, cnt = q.popleft()
        if x == N-1 and y==M-1:
            result += 1
            all = cnt
            print(result)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny]==False:
                    visited[nx][ny] = True
                    temp = cnt+1
                    q.append([nx, ny, temp])

bfs([0,0])

print(all)
print(result)