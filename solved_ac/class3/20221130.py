"""
depth first search 
dfs는 stack 기반이다.
recursion 기반으로 작성 

조합을 찾을 때 for 문을 사용할 경우 N만큼 배수로 증가한다. 
그렇기 때문에 DFS를 이용해서 해야한다. 
2차원에서 위 아래 오른쪽 왼쪽 - depth에 늘어지는 것이다. 늘어지는 것이 for문에 들어가고 
재귀함수를 call하는 것은 depth가 된다. 

dfs나 bfs나 결국은 그래프 문제이다.
stack으로 구현도 가능할 수 있다.
"""

def dfs_py():
    N,e = map(int, input().split())
    visited = [False for _ in range(N)] # 노드수로 visited 를 설정
    graph = [[0 for _ in range(N)] for _ in range(N)] # 2차원 array 설정

    values = list(map(int, input().split()))

    for i in range(N):
        x,y = values[i*2], values[i*2+1]
        graph[x][y] = graph[y][x] = 1
    print(graph)
    dfs(0, N, graph, visited) # 만약 시작이 1번부터이면 dfs는 1번부터 탐색 시작이다.

def dfs(node, N, graph, visited): # N은 node의 개수를 의미한다.
    visited[node] = True
    print(node, end=' ')

    for next in range(N):
        if not visited[next] and graph[node][next]:
            dfs(next, N, graph, visited)



if __name__ =="__main__":

    D = ((-1,0), (1,0), (0,-1), (0,1))
    N = int(input())
    Board = [list(map(int,input().split())) for _ in range(N)]


    def flood_fill(sr, sc, color):
        visited = [[False for _ in range(N)] for _ in range(N)]
        stack = []
        stack.append((sr,sc))

        while stack:
            curr = stack.pop()
            if visited[curr[0]][curr[1]]: continue

            visited[curr[0]][curr[1]] = True
            Board[curr[0]][curr[1]] = color

            for i in range(4):
                nr = curr[0] + D[i][0]
                nc = curr[1] + D[i][1]
                if nr<0 or nr>N-1 or nc<0 or nc>N-1: continue
                if visited[nr][nc]: continue
                if Board[nr][nc] == 1: continue
                stack.append((nr,nc))


    sr,sc,color = map(int, input().split())
    flood_fill(sr,sc,color)

