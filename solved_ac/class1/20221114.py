import math, sys

"""
체스판 칠하기 
point1: 2차원 chess판 만들기 
point2: 8*8을 어디서 선택할 것인지 --> sliding window concept으로 하나씩 다 검사하기 
point3: 최소값을 찾는 알고리즘 진행  
point4: 처음 W를 시작하는 것과 B로 시작하는 것 중에서도 min max를 따져야 한다. 

list control skill = data = [x**2 for x in data]
list 역순 list[::-1] or reverse() 사용 

아스키코드값으로 알파벳 나타내기 
alphabet = list(range(97,123)) # 아스키코드 값 
여기서 끝이 아니라 
chr(x) 를해주면 아스키코드 숫자를 문자로 변경해준다. 
문자를 아스키코드로 바꾸는 것은 ord 


list에서 index찾는 것은 .find 사용 

import sys 확인해보기 
sys.stdin.readline() 
"""

def chess_re_colorization():
    h, w = map(int, input().split())
    arr = []
    count = []
    for _ in range(h):
        arr.append(list(map(str, input())))

    for a in range(h-7):
        for b in range(w-7):
            index1 = 0
            index2 = 0
            for i in range(a, a+8):
                for j in range(b, b+8):
                    if (i + j) % 2 == 0:
                        if arr[i][j] != 'W':
                            index1 += 1
                        if arr[i][j] != 'B':
                            index2 += 1
                    else:
                        if arr[i][j] != 'B':
                            index1 += 1
                        if arr[i][j] != 'W':
                            index2 += 1
            count.append(min(index1, index2))

    print(min(count))

def morning_clock():
    h, m = map(int, input().split())
    if m-45 <0:
        m = 60 + (m - 45)
        if h ==0:
            h = 23
        else:
            h = h-1
    else:
        m = m-45

    print("%d %d"%(h,m))

def print_start():
    N = int(input())
    for i in range(N):
        print(" "*(N-1-i)+"*"*(i+1))

def bee():
    # 6의 배수만 control 하면 easy
    N = int(input())
    if N==1:
        print('1')
    else:
        total = 1
        for i in range(1, N):
            total += 6*i
            if total >= N:
                print(i+1)
                break

if __name__ =="__main__":
    import sys
    N = int(input())
    data = [int(sys.stdin.readline()) for _ in range(N)]
    for i in sorted(data):
        print(i)