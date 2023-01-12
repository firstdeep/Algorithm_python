# 전체적인 목표는 누적합에 대해서 진행하였음
# 1차원 2차원 모두 진행할 수 있어야 된다. 대부분 직접 array를 구현하는 것이 아니다.
# 범위를 정해놓고 한번에 sum해야 효율성 측면에서 좋다.

'''
누적합 계산 시간 복잡도는 O(N)인데
부분합을 이용하면 O(1)로 줄일 수 있다.
'''

# 백준 구간 합 구하기 4 - 기초
import sys

def pre_sum():
    input = sys.stdin.readline
    n,m = map(int, input().split())
    data = list(map(int, input().split()))
    sum = [0 for _ in range(n+1)]

    # 누적합 구헤서 저장 하기
    for i in range(1, len(data)+1): # 가장 기본적인 방법 하나씩 accumulator 하는 것은 배열이 1차원 일때는 상관없지만 많은 수가 지속적으로 진행되면 수정 필요하다.
        sum[i] = data[i-1] + sum[i-1]

    for _ in range(m):
        start, finish = map(int, input().split())
        print(sum[finish] - sum[start-1])


'''
2차원 누적합 구하기 
'''
def sum_2darr():
    arr = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    m=4
    n=3

    sum_arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1] # 이게 핵심
            # 채울곳을 기준으로 좌우 값을 더한 후에 대각선 깞을 빼준다. 그 후 중복해서 빠진 값을 원래 데이터로 더해준다.
    print(sum_arr)

    # 2차원 구간에서 구간별 합 구하기 실제 array 기준 (0,1)에서 (1,3)까지
    result = sum_arr[2][4] - sum_arr[0][4] - sum_arr[2][1] + sum_arr[0][1] # 정해진 부분 끼리의 부분 함 구하는 방법
    # 찾고자 하는 것 + 1씩 한것에다가 0,1 기준으로 x,y빼고 이후 해당 값의 sum값만 다시 더해준다. 중복해서 빠진 부분을 더해주는 것이다.
    print(result)

'''
기본적인 생각으로는 N,M을 모두 search하면 효율성 테스트에서 통과가 불가능하다. 
누구나 생각할 수 있는 생각... 
누적합 컨셉인데 -> board에 한번만 적용할 수 있는 함수를 만드는 것 이 초점이다. 그러면 한번의 연산만으로 0(1) 시간 복잡도를 가질 수 있음 
그러면 누적합을 어떻게 만들 것인가?에 대한 고찰이 필요하며 
거기서 start와 finish를 생성하는 것에 초점을 맞춘다. 
'''
def destroy_building():
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

    answer = 0
    temp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]

    for type, r1, c1, r2, c2, degree in skill:
         temp[r1][c1] += degree if type==2 else -degree
         temp[r2+1][c2+1] += degree if type==2 else -degree
         temp[r1][c2+1] += -degree if type==2 else degree
         temp[r2+1][c1] += -degree if type==2 else degree

    # 행끼리 더하기
    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i][j+1]+=temp[i][j]

    # 열끼리 더하기
    for j in range(len(temp[0])-1):
        for i in range(len(temp)-1):
            temp[i+1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if board[i][j] >0: answer += 1
    # print(answer)
    return answer

from collections import Counter
import sys, itertools

def dog_bug():
    # 문제 컨셉: 누적합을 이용한다. 먼저 배열을 만들어 놓고 행으로 더하기를 하여 count를 진행한다.
    # 첫번째 시도 메모리 초과.. 2차원 배열을 무작정 만들면 N^2나온다. 
    # 배열 한개만 있어도 된다... 바로바로 누적 합 이용
    # 다시 시간 초과 발생
    # 숫자가 있으면 첫번째에 1을 할당하고 마지막 부분에 -1을 할당한다. = 정답 맞았음 즉

    N,H = map(int, input().split())
    data = [int(input()) for _ in range(N)]

    temp = [0 for _ in range(H)]

    for idx, i in enumerate(data):
        if idx % 2 == 0:
            temp[H-i] +=1
        else:
            temp[0] +=1
            temp[i]-=1

    temp = list(itertools.accumulate(temp))
    c = Counter(temp) # 최소값만 뽑기위해 sort 진행
    min_value = list(sorted(c.keys()))[0]
    print(min_value, c[min_value])

def test_pref():
    arr = [0,1,0,0,-1]
    result = list(itertools.accumulate(arr))
    print(result)



if __name__=="__main__":
    dog_bug()