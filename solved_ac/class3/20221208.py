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

    dd = [0, 0, 1, 2, 3]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    def bfs():
        q = deque()
        q.append([fx-1,fy-1,dd[fd],0])
        visited = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]
        visited[fx - 1][fy - 1][dd[fd]] = True
        while q:
            x,y,dir,cnt = q.popleft()
            if x == tx - 1 and y == ty - 1 and dir == dd[td]:
                return cnt

            ax, ay = x, y
            for _ in range(3): # 직진 먼저 진행
                ax += dx[dir]
                ay += dy[dir]
                if 0 <= ax < N and 0 <= ay < M and graph[ax][ay] == 0:
                    if visited[ax][ay][dir] == False:
                        visited[ax][ay][dir] = True
                        q.append([ax, ay, dir, cnt + 1])
                else:
                    break

            for i in range(4):
                if visited[x][y][i] == False and dir != i:
                    visited[x][y][i] = True
                    a = 1
                    if (i == 0 and dir == 1) or (i == 1 and dir == 0) or (i == 2 and dir == 3) or (i == 3 and dir == 2):
                        a = 2
                    elif (i==dir): a=0
                    q.append([x, y, i, cnt + a])


    print(bfs())
if __name__=="__main__":
    robot()