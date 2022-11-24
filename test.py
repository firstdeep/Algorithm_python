import sys
def find_decimal(N):
    arr = [True] * (N+1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(N))+1):
        if arr[i] == True:
            j = 2
            while (i*j) <= N:
                arr[i*j] = False
                j += 1

    return arr


if __name__ =="__main__":
    M, N = map(int, sys.stdin.readline().split())
    arr = find_decimal(N)
    for i in range(M,len(arr)):
        if arr[i] == True:
            print(i)