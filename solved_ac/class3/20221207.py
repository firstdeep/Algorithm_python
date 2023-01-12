'''
문제: DFS 및 BFS 테마 문제이고 - BFS로 풀어보자
가장 넓은 방과 성의 방의 개수는 BFS구현으로 쉽게 알 수 있음

해결해야 하는 것
1. 숫자가 주어졌을 때 벽이 어디에 있는지 확인 1번째로 풀어야함
1.1 BFS를 이용하여
2. 벽을 파악했다면 해당 벽을 제거하여 가장 큰 방 찾기
2.1 첫번째 시도: BF로 찾아보자
비트마스킹을 이용하여 성벽의 유무를 찾을 수 있음 비트마스킹이란 무엇인가?...
'''
from collections import deque
def castle():
    N,M = map(int, input().split())
    graph = [list(map(int,input().split()))for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    def bfs(x,y):
        cnt=1
        visited[x][y] = True
        dq = deque()
        dq.append((x,y))
        while dq:
            curr = dq.popleft()
            for idx in range(4): # 여기서는 벽 세우기 해야 함
                nx = curr[0] + dx[idx]
                ny = curr[1] + dy[idx]
                if 0 <= nx < M and 0 <= ny < N and visited[nx][ny]==False: # 아닐 때 들어온다는 것이다.
                    if idx == 0: # 비트 연산자로 교집합을 했을 때 0이 나온다는 것은 포함이 안되어있다는 것이다.
                        if 1 & graph[curr[0]][curr[1]]: continue
                    elif idx == 1:
                        if 2 & graph[curr[0]][curr[1]]: continue
                    elif idx == 2: #
                        if 4 & graph[curr[0]][curr[1]]: continue
                    elif idx == 3:
                        if 8 & graph[curr[0]][curr[1]]: continue
                    visited[nx][ny] = True
                    dq.append((nx,ny))
                    cnt+=1
        return cnt

    result1 = 0
    result2 = 0
    result3 = 0
    # make room partition
    for i in range(M):
        for j in range(N):
            if visited[i][j]==False:#여기서 중요한 것 visited check 해야 된다.
                result1 += 1
                result2 = max(result2, bfs(i,j))

    # BF문제?
    # BF가 맞네...
    # 하나를 뺐을 때 부터 모든 것을 찾아야 하기 때문에 visited를 여기서 선언한다.
    for i in range(M):
        for j in range(N):
            num = 1
            while num <9:
                if num & graph[i][j]: # 비트 연산을 통해서 벽인지 아닌지를 확인한다.
                    visited = [[False] * N for _ in range(M)]
                    graph[i][j]-=num # 빼주고 BFS통해서 찾았으면 다시 더해줘야 한다.
                    result3 = max(result3, bfs(i,j))
                    graph[i][j] += num
                num*=2


    print(result1)
    print(result2)
    print(result3)

'''
bin()은 10진수를 2진수로 변경할 수 있도록 한다. 
or "0b" 붙이기 
print(int(a,2)) 뒤에 숫자가 2를 의미한다. a가 문자열이여도 가능하고 ob가 포함되어 있어도 가능하다. 
a = '1000110'
print(int(a,2))
b = '0b101010'
print(int(b,2)) 2진수로 변환 해서 나오는 output은 10진수로 나오긴 한다. 
'''
import sys
def bit_mask():
    # 1이상 20이하 이기 때문에 bit 연산을 하기 위해서는 앞에 자리 빼고 0포함 총 21자리 필요
    S = (1<<21)
    for _ in range(int(input())):
        command = sys.stdin.readline().split()
        if command[0] == 'add': # 합집합으로 구현하면 됨, 원래 있었어도 1 없으면 추가하기 떄문에 1
            S |= (1<<int(command[1]))# 합집합이다.
            # print(bin(S))
        elif command[0] == 'check':
            # print(bin(S))
            # if S & (1<<int(command[1])) == 0: # 해당 부분과 나머지가 같지 않을 때 0이 나온다. 같으면 10진법 숫자가 나온다.
            #     print(0)
            if (S & (1<<int(command[1]))) == (1<<int(command[1])):
                print(1)
            else: print(0)
        elif command[0] == 'remove': # 특정 자리 값을 0으로 바꿔주는 것 이동시킨 다음 반전하여 and 연산한다.
            S &= ~(1<<int(command[1]))
        # elif a == 'toggle':
        elif command[0] == 'all':
            S = (1 << 21)
            S ^= ~S
            # print(bin(S))
            # 또는 모든 비트를 1로 만들기 위해서는 단수 -1하면 된다. S = (1<<21) -1
        elif command[0] == 'empty':
            S = (1<<21)
            # print(bin(S))
        elif command[0] == 'toggle':
            if S & (1<<int(command[1])) ==0: # 없다는 것인데 없으면 넣어주기
                S |= (1<<int(command[1]))
            else: S &= ~(1<<int(command[1]))


# 아래와 같은 방법도 있긴 하지만 쉽게하는 방법
# 10진수를 받으면 bin()을 이용해서 2진수로 변경
# slicing 이용 bin(num)[2:].count('1') 카운팅 가능하다.
def bitcount(x):
    if x==0: return 0
    return x&2 + bitcount(x//2)




if __name__=="__main__":
    castle()