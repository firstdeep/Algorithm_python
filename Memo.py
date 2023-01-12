'''
조건1 앞으로는 1,2,3만큼 밖에 움직이지 못한다.
조건2 방향은 상하좌우 4방향으로 꺽을 수 있다.

안되는 것이 무엇인가?
해결해야 될 문제점:
'''
from collections import deque
def robot():
    N,M = map(int,input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    fx, fy, fd = map(int,input().split())
    tx, ty, td = map(int, input().split())
    fx, fy, fd = fx-1, fy-1, fd-1
    tx, ty, td = tx-1, ty-1, td-1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    def direction_change_count(pre, post):
        if pre==post:
            return 0
        elif (pre==0 and post==1) or (pre==1 and post==0):
            return 2
        elif (pre==2 and post==3) or (pre==3 and post==2):
            return 2
        else: return 1


    def bfs():
        q = deque()
        q.append([fx,fy,fd,0])
        visited = [[[False for _ in range(4)] for _ in range(M)]for _ in range(N)]
        visited[fx][fy][fd] = True
        while q:
            x,y,dir,cnt = q.popleft()
            if x == tx and y == ty:
                return cnt + direction_change_count(dir, td)
            for i in range(1,4): # 여기서 먼저 직진 check i가 곱해지는 것이기 때문에 1부터 시작
                nx = x + dx[dir] * i # dx에 해당 방향에 있는 것이 들어가야 한다.
                ny = y + dy[dir] * i
                if 0<=nx<N and 0<=ny<M:
                    if visited[nx][ny][dir]==False and graph[nx][ny]==0:
                        visited[nx][ny][dir] = True
                        q.append([nx,ny,dir,cnt+1])
                else:
                    break

            for i in range(4):
                if i!=dir and visited[x][y][i] == False:
                    visited[x][y][i] = True
                    q.append([x,y,i,cnt+direction_change_count(dir,i)])
            print(q)

    print(bfs())

if __name__=="__main__":
    robot()