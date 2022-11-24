import sys

'''
오늘의 지식 한잔 
1. sort는 값 자체를 변경 , sorted는 기존 값은 놔두고 sort된 새로운 값을 return 
'''
def suger_delivery():
    N = int(input())

    arr = []

    x, _ = divmod(N,5)
    y, _ = divmod(N,3)

    for i in range(x+1):
        for j in range(y+1):
            if 5*i + 3*j == N:
                arr.append((i+j))
    if len(arr) == 0:
        print(-1)
    else:
        print(min(arr))

def coordicate_sort(): # 11650
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    data.sort()

    for i in range(N):
        print(*data[i])


def escape_rectangle():
    data = list(map(int, input().split()))

    temp = []
    temp.append(min(data[0],data[2]-data[0]))
    temp.append(min(data[1],data[3]-data[1]))

    print(min(temp))


def alphabet_sort():
    N = int(input())
    data = []

    for _ in range(N):
        str_input = input()
        data.append(str_input)

    # 중복되는 것 filtering
    data = list(set(data))
    data.sort()
    data.sort(key=len)

    for i in data:
        print(i)


def reverse_same():
    while True:
        N = int(input())
        N_list = list(map(int, str(N)))
        if N ==0:
            break
        else:
            count = 0
            a,_ = divmod(len(N_list),2)
            for i in range(a):
                if N_list[i] == N_list[len(N_list)-1-i]:
                    count +=1
            if count == a:
                print('yes')
            else:
                print('no')

'''BF 문제인데 for문으로 다 돌려서 하나하나 찾아본다는 것인데...'''
def movie():
    N = int(input())
    name = 666
    cnt = 0
    while True:
        if "666"in str(name):
            cnt+=1
            if cnt == N: print(name);break

        name +=1





if __name__=="__main__":
    cutting_lan()