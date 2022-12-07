
'''
bfs문제 breadth first search 
depth가 깊어지는 순서대로 진행된다. 
큐를 사용한다. deque
'''

from collections import deque
if __name__ =="__main__":
    N, M, V = map(int, input().split())
    visitied_d = [False for _ in range(N + 1)]
    graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visitied_d[0] = True


    for _ in range(M):
        a,b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1

    def dfs(node):
        visitied_d[node] = True
        print(node, end=' ')

        for next in range(N+1):
            if not visitied_d[next] and graph[node][next]:
                dfs(next)


    def bfs(node):
        visited_b = [False for _ in range(N+1)]
        visited_b[0] = True
        data = deque()
        visited_b[node] = True
        data.append(node)

        while data:
            curr = data.popleft()
            print(curr, end=' ')
            for next in range(N+1):
                if not visited_b[next] and graph[curr][next]:
                    visited_b[next] = True
                    data.append(next)
    dfs(V)
    print("")
    bfs(V)



