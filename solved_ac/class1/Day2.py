# 알고리즘 다지기 기초 백준 문제 추천
# https://covenant.tistory.com/224
# 2022.09.21
# pass 문제: 사탕게임, 단지번호붙이기

# '''
# 1789번
# S는 서로다른 N개의 자연수의 합이다.
# S의 범위는 1 ~ 42억까지
# 최대한 많은 자연수를 사용해서 S를 만들기 위해서는 서로 다른 자연수들이 최소가 되어야 한다.
# 만약 1+2+3+4 = 10 이고 1+2+3+4 = 15 즉 1씩 증가하면서 다 더해보면 결국에는 4개 이상의 자연수를 써야함 15이상을 표현할 수 있다는 뜻
# '''
# S = int(input())
#
# total = 0
# count = 0
#
# while True:
#     count+=1
#     total += count
#     if total > S:
#         break
# print(count-1)

# '''
# 3085번
# BF 문제 -> 완전탐색 문제
# - 2차원 할당하는 법
# - 파이썬 에서는 a, b = b, a를 통해서 swap이 가능하다.
# '''
#
# N = int(input())
# arr = [[0]*N for _ in range(N)]
#
# for i in range(N):
#     arr[i] = list(input())


# '''
# 2293번 - 1789와 동일한 맥락
# 순서는 상관없음, 구성당 1회임
# dynamic programming DP 문제이다.
# - 전체의 문제를 부분 문제로 잘 나누었는가?
# - 부분 문제들을 해결하면 얻는 값을 메모라이제이션 하는가?
# - 부분 문제의 점화식은 부분 문제들 사이의 관계를 빠짐없이 고려하였는가?
# - 위와 동일한 맥락인데 동전의 가치인 것 만큼이 추가되면 경우의 수가 추가하게 된다.
# '''
#
# n, k = map(int,input().split())
#
# # list안에서 한번에 받는 법
# arr = [int(input()) for i in range(n)] # 코인 종류
# dp = [0 for i in range(k+1)] # dp안에는 결국 해당 값을 만들때 사용되는 경우의 수가 들어있다.
# dp[0] = 1 # 동전을 1개만 사용할 때 경우의 수
#
# for i in arr:
#     for j in range(i,k+1):
#         if j-i >= 0:
#             dp[j] += dp[j-i]
#
# print(dp[k])

# '''
# 2294번
# 동전의 개수가 최소가 되도록 하는 것
# 2293번은 모든 경우의 수를 말하는 것이고 이것은 최소의 경우의 수를 의미하는 것
# 그러면 위와 동일한 프로세스로 진행하 되,
# 조건식만 달라지면 될 것 같은데
# 불가능한 경우는 -1을 출력
# 최소가 목적이다.
# '''
#
# n, k = map(int, input().split())
# arr = [int(input()) for _ in range(n)]
#
# dp = [99999 for i in range(k+1)]
# dp[0] = 0
#
# # for j in arr 부터 진행 하면 안된다.
# # 이걸 바꿔야 한다.
# for i in range(n):
#     for j in range(arr[i], k+1):
#         dp[j] = min(dp[j], dp[j-arr[i]]+1)
#
# if dp[k] != 99999:
#     print(dp[k])
# else:
#     print(-1)

# '''
# 2667번
# bf 문제라고 생각됨
# -정사각 행렬 초기화 하는 방법 익히기
# - 찾은 애가 몇단지 인지 정보를 저장해야 함
# - 한번에 십자가 형으로 확인해야 함
# - row는 +2씩 검사하기
#
# - bfs dfs 문제 ...
# '''
#
# N = int(input())
# arr = [[0]*N for _ in range(N)]
#
# for i in range(N):
#     arr[i] = list(map(int, input()))
#
# temp_list=[]
#
# for i in range(0,N,2):
#     for j in range(0,N):
#         if arr[i][j] == 1:
#


'''
1038번 감소하는 수
https://dkrnfls.tistory.com/350
'''