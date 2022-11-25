import sys, math
from collections import deque

def card2():
    N = int(input())
    q = deque(list(x+1 for x in range(N)))

    cnt = 0
    while len(q)!=1:
        if cnt%2==0:
            q.popleft()
            cnt+=1
        else:
            q.append(q.popleft())
            cnt += 1
    print(*list(q))

'''
요구사항: 카드 합 21이 넘지 않으면서도 카드의 합을 최대한 크게 만드는 것 
조합을 이용해서 가능한 모든 경우의 수를 찾고 
sum을 해서 가까운 값을 찾는다.  
'''
from itertools import combinations
def blackjack():
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    all_data = list(combinations(data, 3))
    all_sum = [sum(i) for i in all_data if sum(i)<=M]
    print(max(all_sum))

def rectangle():
    while True:
        data = list(map(int, input().split()))
        if sum(data)==0:
            break
        else:
            max_data = max(data)
            data.remove(max_data)
            if max_data**2 == data[0]**2 + data[1]**2:
                print("right")
            else:
                print('wrong')

'''
이항계수 
N과 k 를 이용할때 공식 사용 
'''
import math
def binomial():
    n, k = map(int, input().split())
    answer = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
    print(answer)

'''
1~12 
예외 케이스도 
'''
def ACM_hotel():
    N = int(input())
    for _ in range(N):
        h, w, temp = map(int, input().split())
        a,b = divmod(temp, h)
        answer = '%d%.2d'%(b,(a+1))
        # 예외 처리가 핵심 이거 생각하면 무난
        if b == 0:
            answer = '%d%.2d' % (h, a)
        print(answer)


'''
이것도 예외 처리 신경 
list 값 삭제하는 법 
'''
def PS():
    N = int(input())
    for _ in range(N):
        data = list(input())
        idx = 0
        while True:
            if data[idx] =='(' and data[idx+1] ==')' and idx<len(data)-1:
                del data[idx:idx+2]
                if len(data) == 0:
                    print("YES")
                    break
                if len(data) ==1:
                    print("NO")
                    break
                idx = 0
            else:
                idx += 1
                if len(data)-1==idx:
                    print("NO")
                    break

"""
Gold: 2048(EASY)...
최대 5번을 했을 때 가장 많은 값을 가지는 것을 출력 
분류: 시뮬레이션 
- 큐 이용 
- 재귀함수 이용 
- 
"""
from collections import deque
def game_2048():
    N = int(input())
    # 한줄로 2D array 생성하기
    data = [list(map(int, input().split())) for _ in range(N)]
    answer, q = 0, deque()



if __name__ == "__main__":
    game_2048()
