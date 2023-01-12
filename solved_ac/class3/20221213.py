'''
알고리즘 문제를 풀면서 단순하게 구현이 가능하다면
단순 구현이 방법일 수 있다.
아래 ATM문제를 보고 DP를 예상했지만 그냥 단순하게 접근하는 것이 더 좋을 수 있다.
'''
def ATM():
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()
    sum = 0
    total = 0
    for i in data:
        sum+=i
        total += sum
    print(total)

'''
DP 문제
- 최적 부분 구조 (optimal substructure)
    - 큰 문제를 작은 문제로 나누고 작은 문제의 답을 오마 큰 문제를 해결
- 중복되는 부분 문제 (overlapping subproblem)
    - 동일한 작은 문제를 반복적으로 해결
    - 단순 재귀로 피보나치 수열 (지수 시간 복잡도를 가진다.)
        f(2)가 계속적으로 수행되기 때문이다. 따라서 f(2)를 값으로 가지고 있으면 시간 복잡도를 잡을 수 있다.

'''
d = [0] * 100

def dp_fibo(x):
    if x ==1 and x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x] = dp_fibo(x-1) + dp_fibo(x-2)
    return d[x]



if __name__=="__main__":
    sum_123()