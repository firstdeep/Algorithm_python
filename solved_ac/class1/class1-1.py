'''
덧셈, 나누기, 곱셈
- input 받는 방법
- eval 사용 법
'''
import sys


def sum():
    print(eval('+'.join(input())))
    # 변수 없이 합 구하기
    print(sum(map(int, input().split())))

def sub(): # eval 사용해서 빼는 방법 '-'만 하면 안된다.
    print(eval('+0-'.join(input())))

def str_len_ver1():
    s = input().split()
    print(len(s))

'''
input이 string type 일 때 
strip: 인자로 전달된 문자를 string이 왼쪽과 오른쪽에 제거한다. 
lstrip: 인자로 전달된 문자를 string이 왼쪽에서 제거한다. 
rstrip: 인자로 전달된 문자를 string이 오른쪽에서 제거한다. 
print 함수 자체에서 string을 출력할 때 자동으로 끝에 \n을 적용시켜 준다. 
'''
def str_len_ver2():
    # example
    s = input().strip()
    print(s.count(" ")+1)

# 효율 중시는 나중에 하고 정답 맞추는 방향으로
def check_alpha():
    s = input().strip().lower()
    s_uni = ''.join(dict.fromkeys((s))) # dic은 순서 보장
    # s_uni = ''.join(set(s)) # 순서 보장 하지 않음

    cnt_list = []
    for x in s_uni:
        cnt_list.append(s.count(x))

    if cnt_list.count(max(cnt_list)) > 1:
        print("?")
    else:
        max_idx = cnt_list.index(max(cnt_list))
        print(s_uni[max_idx].upper())

def change_score():
    import numpy as np

    n = int(input())
    a = list(map(int, input().split()))
    a = np.array(a[:n])
    a_max = max(a)

    a = a / a_max
    print(np.mean(a))

def print_star():
    a = int(input())

    for idx in range(1, a + 1):
        print("*" * idx)

def list_max():
    num_list = []
    for i in range(9):
        num_list.append(int(input()))

    print(max(num_list))
    print(num_list.index(max(num_list)) + 1)

if __name__ == "__main__":
    change_score()