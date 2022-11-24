# 준비운동 PART1. 튼튼한 기본기
# https://covenant.tistory.com/224

import sys
import math

# '''
# 2501번
# 약수 중 b번째 index를 찾는 방법
# input을 아래와 같이 map으로 진행해주면 된다.'''

# a, b = map(int, sys.stdin.readline().rstrip().split())
#
# list_temp = []
#
# ''' '''
# for i in range(1,int(a)+1):
#     if int(a)%i == 0:
#         list_temp.append(i)
#
# if len(list_temp) < b:
#     print("0")
# else:
#     print(list_temp[int(b)-1])
####################################################################################

# '''
# 3460번
# 양의 정수 n이 주어 졌을 때 1의 위치를 모두 찾는 프로그램
# - list 변수 생성하지 말고 바로 출력하는 쪽으로 print쪽에 end를 사용하면 띄어쓰기 없이 출력 가능하다.
# - list 안의 값만 출력하고 싶을 때는 *사용하면 된다.
# - 값의 몫과 나머지를 출력할 떄는 math의 divmod를 쓰면 된다.
# - 이진법은 bin으로 하면 출력된다. 하지만 앞에 ob100와 같이 ob가 붙기 때문에 이를 제거하기 위해서 slicing 기법 사용함
# '''
# from more_itertools import locate
#
# a = int(input())
# count = 0
# for _ in range(a): # 사용하지 않는 변수는 _ 사용하기
#     b = bin(int(input()))[2:]
#     for i in range(len(b)):
#         if b[-i-1] == '1':
#             print(i, end=' ')
####################################################################################

# '''
# 2460번
# '''
#
# max_temp = 0
# in_train = 0
# for _ in range(10):
#     a,b = map(int, input().split())
#     in_train = in_train - a
#     in_train = in_train + b
#     if max_temp < in_train:
#         max_temp = in_train
#
# print(max_temp)

# '''
# 10870번
# 피보나치
# '''
# n = int(input())
#
# def fibo(idx):
#     if idx == 0:
#         return 0
#     elif idx == 1 or idx == 2:
#         return 1
#     else: return fibo(idx-1) + fibo(idx-2)
#
# print(fibo(n))


# '''
# 2309 번
# 핵심은 2명이 sub 합을 가지는 것을 찾는 것.
# 순열? 조합?
# - 브루트 포스 유형문제
# - Brute(짐승 같은자) Force(힘) 즉 노가다.
# - array에 input 한번에 받는 법 --> 숙지하기
# - arr[int(input()) for _ in range(n)]
# '''
#
# list_temp = [int(input()) for _ in range(9)]
#
# list_temp = sorted(list_temp)
# total = sum(list_temp)
# check = 0
# for i in range(len(list_temp)-1):
#     for j in range(i+1, len(list_temp)):
#         if (total-100) == list_temp[i] + list_temp[j]:
#             a = list_temp[i]
#             b = list_temp[j]
#             list_temp.remove(a)
#             list_temp.remove(b)
#             check = 1
#             break
#     if check == 1: break
#
# for i in list_temp:
#     print(i)

# '''
# 2609번
# 최대공약수
# 최소공배수 문제 math 이용하기
# 개념: input 2개를 곱하는 것이, 최대공약수 * 최소공배수 이다.
# '''
# import math
#
# a, b = map(int, input().split())
# print(math.gcd(a,b))
# print((a*b//math.gcd(a,b)))

# '''
# 2693번
# N번째 큰수
# '''
# n = int(input())
#
# for _ in range(n):
#     arr = list(map(int, input().split()))
#     arr = sorted(arr)
#     print(arr[-3])

# '''
# 1978번
# - 1은 소수가 아니다.
# - 2부터 모든 수를 나누었을 때 나눠지는 것이 즉 나머지가 0인 것이 하나라도 있으면 소수가 아니다.
# '''
# n = int(input())
# arr = list(map(int, input().split()))
#
# count = 0
#
# for i in arr:
#     flag = 0
#     for j in range(2,i):
#         if i % j == 0:
#             flag = 1
#     if i == 1:
#         flag = 1
#
#     if flag != 1:
#         count = count + 1
#
# print(count)

# '''
# 1292번
# - key 는 input 의 구간을 보고 결국 array가 어떻게 생성될 것인지 확인하는 것
# - array를 만들어 놓으면 되는 문제
# - array를 안만들고 input으로만 문제를 해결하려고 했던 것이 문제였음...
# - 때로는 무식하게 코딩하는 것도 도움 됨
# - slice 할 때 끝에는 항상 내가 생각했던 index + 1 하기
# '''
#
# a, b = map(int, input().split())
#
# arr = []
# for i in range(46):
#     for j in range(i):
#         arr.append(i)
#
# print(sum(arr[a-1:b]))


# '''
# 2581번
# - for문 중첩으로 인해 시간 소요가 많이 될 것 같은데 일단은 알고있는 방식으로 진행
# '''
# a = int(input())
# b = int(input())
#
# def check(num):
#     if num == 1:
#         return False
#     for i in range(2,num):
#         if num%i == 0:
#             return False
#     return True
#
# list_temp = []
#
# for i in range(a, b+1):
#     if check(i):
#         list_temp.append(i)
#
# if len(list_temp)==0:
#     print('-1')
#
# else:
#     print(sum(list_temp))
#     print(list_temp[0])

'''
1700번 
그리디 알고리즘 개념 문제 
- 일단은 제한된 정보안에서 사용순서를 알아냈고 목적을 최소화 하려고함 
# 값이 없을 떄는 뒤로 멀티탭의 개수 -1 만큼 확인해야 한다.
# 집합으로 차집합을 구하는 방법
'''

N, K = map(int, input().split())
multitap = list(map(int, input().split()))

min_count = 0
adapter = [0] * N #콘센트 코드 갯수만큼 초기화

for idx, i in enumerate(multitap):

    if i in adapter: # 어댑터에 있으면 pass
        pass
    elif 0 in adapter: # 어댑터에 0이 있으면 자리가 비어있다는 것 따라서 0 index에 값 할당
        adapter[adapter.index(0)] = i
    else: # 해당 기기가 adapter에 없으므로 실행 뒤쪽 순서를 확인해야함
        far_other = 0
        temp = 0
        for j in adapter:
            if j not in multitap[idx:]:
                temp = j
                break
            elif multitap[idx:].index(j)>far_other:
                far_other = multitap[idx:].index(j)
                temp = j
        adapter[adapter.index(temp)] = i
        min_count = min_count + 1
print(min_count)
