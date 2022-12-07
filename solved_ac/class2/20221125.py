
'''
나이가 같으면 먼저 온 순서대로
lambda쓰는 것은 알았는데... input에서 error가...
'''
def sort_first():
    N = int(input())
    # data = [list(input().split()) for i in range(N)]
    data = []

    for i in range(N):
        age, name = map(str, input().split())
        age = int(age)
        data.append((age, name))

    data.sort(key=lambda x : x[0])

    for idx in data:
        print(idx[0], idx[1])

from collections import Counter
def num_card():
    _ = int(input())
    data = list(map(int, input().split()))
    _ = int(input())
    search_data = list(map(int, input().split()))

    data = Counter(data)

    print(' '.join(f'{data[m]}' if m in data else '0' for m in search_data))

from collections import deque
def stack_function():
    N = int(input())
    q = deque()
    answer = []
    for _ in range(N):
        data = input()
        if data.split()[0] == 'push':
            q.append(int(data.split()[1]))
        elif data == 'pop':
            if len(q) != 0: answer.append(q.pop())
            else: answer.append(-1)
        elif data == 'size':
            answer.append(len(q))
        elif data == 'empty':
            if len(q)!=0: answer.append(0)
            else: answer.append(1)
        elif data == 'top':
            if len(q)!=0: answer.append(q[-1])
            else: answer.append(-1)

    for i in answer:
        print(i)

from collections import deque
def que():
    N = int(input())
    q = deque()
    answer = []
    for _ in range(N):
        data = input()
        if data.split()[0] == 'push':
            q.append(int(data.split()[1]))
        elif data == 'pop':
            if len(q) != 0: answer.append(q.popleft())
            else: answer.append(-1)
        elif data == 'size':
            answer.append(len(q))
        elif data == 'empty':
            if len(q)!=0: answer.append(0)
            else: answer.append(1)
        elif data == 'front':
            if len(q)!=0: answer.append(q[0])
            else: answer.append(-1)
        elif data == 'back':
            if len(q) != 0:answer.append(q[-1])
            else:answer.append(-1)

    for i in answer:
        print(i)

from collections import deque
def dque():
    N = int(input())
    q = deque()
    answer = []
    for _ in range(N):
        data = input()
        if data.split()[0] == 'push_front':
            q.appendleft(int(data.split()[1]))
        if data.split()[0] == 'push_back':
            q.append(int(data.split()[1]))
        elif data == 'pop_front':
            if len(q) != 0: answer.append(q.popleft())
            else: answer.append(-1)
        elif data == 'pop_back':
            if len(q) != 0: answer.append(q.pop())
            else: answer.append(-1)
        elif data == 'size':
            answer.append(len(q))
        elif data == 'empty':
            if len(q)!=0: answer.append(0)
            else: answer.append(1)
        elif data == 'front':
            if len(q)!=0: answer.append(q[0])
            else: answer.append(-1)
        elif data == 'back':
            if len(q) != 0:answer.append(q[-1])
            else:answer.append(-1)

    for i in answer:
        print(i)

'''
순서및 index 이동의 경우 
deque로 구현하면 된다...
list 로 구현 시 시간이 많이 걸릴 수 있음  
'''

def yoseop():
    n, m = map(int, input().split())
    data = deque([i+1 for i in range(n)])
    answer = []

    while data:
        for _ in range(m-1):
            data.append(data.popleft())
        answer.append(data.popleft())

    print(str(answer).replace('[', '<').replace(']', '>'))

'''sort가 핵심인데 data자체에서부터 sort를 하는 방법도 존재 '''
from collections import Counter
def static():
    N = int(input())
    data = [int(input()) for _ in range(N)]
    data.sort()
    data_count = Counter(data).most_common(2) # 이것만 알면 끝
    # data_count = sorted(data_count.items(), key=lambda x:x[1], reverse=True)

    print(round(sum(data)/len(data)))
    print(sorted(data)[int((len(data)-1)/2)])
    if len(data_count) > 1:
        if data_count[0][1] == data_count[1][1]:
            print(data_count[1][0])
        else:
            print(data_count[0][0])
    else:
        print(data_count[0][0])
    print(max(data)-min(data))

def div_sum():
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        nums = list(map(int, str(i)))
        result = sum(nums) + i
        if result == n:
            print(i)
            break
        if i == n:
            print(0)

# 이분탐색으로 찾기
# 높이를 통해서 힌트 얻기
def tree():
    n, h = map(int, input().split())
    data = list(map(int, input().split()))
    start, end = 1, max(data)

    while start<=end:
        mid = (start + end) // 2
        answer = 0
        for tree in data:
            if tree > mid:
                answer +=tree - mid
        if answer >=h:
            start = mid + 1
        else:
            end = mid - 1

    print(end)

def str_check():

    while True:
        N = str(input())
        answer = []

        if N =='.':
            break

        for idx in N:
            if idx == '(' or idx == '[':
                answer.append(idx)
            elif idx ==')':
                if len(answer) !=0 and answer[-1] == '(':
                    answer.pop()
                else:
                    answer.append(idx)
                    break
            elif idx ==']':
                if len(answer) !=0 and answer[-1] == '[':
                    answer.pop()
                else:
                    answer.append(idx)
                    break

        if len(answer)!=0:
            print("no")
        else:
            print("yes")


def ceo():
    N = int(input())
    for _ in range(N):
        data = [int(input()) for _ in range(2)]
        f0 = [x for x in range(1, data[1]+1)]
        for x in range(data[0]):
            for y in range(1,data[1]):
                f0[y] += f0[y-1]

        print(f0[data[1]-1])

def snail_up():
    a, b, V = map(int, input().split())
    k = (V-b)/ (a-b)
    print(int(k) if k==int(k) else int(k)+1)


# 출력으로 시간과 높이
# 그냥 구현인가? BF
from collections import Counter
import sys
def mine():
    n, m, inven = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    height, time = 0, sys.maxsize

    data = sum(data,[])
    min_h = min(data)
    max_h = max(data)
    _sum = sum(data)
    data = dict(Counter(data))

    # 나는 기존에
    for i in range(min_h, max_h+1): # 각 층을 기준으로 time을 계산한 후에 가장 작은 time을 return 해주는 쪽으로
        if _sum+inven >= i*n*m:
            curr_time = 0
            for key in data:
                if key>i: # 현재 가져온 key 보다 큰 경우
                    curr_time += (key-i) * data[key] * 2
                elif key<i:
                    curr_time += (i-key) * data[key]
            if curr_time <=time:
                time = curr_time
                height = i
    print(time, height)

'''
아스키코드 값변경하는 것 int -> char: chr
char -> int: ord 
'''
def Hashing():
    N = int(input())
    input_str = list(str(input()))
    r, M = 31, 1234567891

    total = 0
    init = ord('a')-1

    for idx, item in enumerate(input_str):
        total += (ord(item)-init) * (r**idx)

    print(divmod(total, M)[1])


def coordinate_sort2():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data = sorted(data, key=lambda x:x[0])
    data = sorted(data, key=lambda x:x[1])
    for item in data:
        print(*item)

def zero():
    N = int(input())
    arr = []
    for _ in range(N):
        num = int(input())
        if num ==0:
            arr.pop()
        else:
            arr.append(num)
    print(sum(arr))

'''
input output 범위 보고 BF문제인지 추축하기 
sort등을 하면 오히려 일단 모든 코딩을 간단하게 구현해 놓고 
세부적인 내용 생각하기 
'''
def big_guy():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    for i in data:
        rank = 1
        for j in data:
            if i[0]<j[0] and i[1]<j[1]:
                rank +=1
        print(rank, end=' ') # 엔터 없이 출력하는 방법

if __name__ == '__main__':
    big_guy()