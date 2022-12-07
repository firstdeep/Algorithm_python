# S = (1<<21) # 이게 의미하는 것이 1^20 만약에 1자릿수로 줄이면서 모두 1일 때는 -1 해주면 20자리에 모두 1이 된다.
# print(bin(S))
# S |=(1<<3)
# S |=(1<<1)
# print(bin(S))
# S = S & (1<<3)
# print(bin(S))
# print(S)

# # print(bin(~(1<<3)))
# print(bin(S))
# # print(bin(b))
#
#
# def bitcount(x):
#     if x==0: return 0
#     return x % 2 + bitcount(x//2)



import sys
def function():
    # 1이상 20이하 이기 때문에 bit 연산을 하기 위해서는 앞에 자리 빼고 0포함 총 21자리 필요
    S = (1<<21)
    for _ in range(int(input())):
        command = sys.stdin.readline().split()
        if command[0] == 'add': # 합집합으로 구현하면 됨, 원래 있었어도 1 없으면 추가하기 떄문에 1
            S |= (1<<int(command[1]))# 합집합이다.
            # print(bin(S))
        elif command[0] == 'check':
            # print(bin(S))
            # if S & (1<<int(command[1])) == 0: # 해당 부분과 나머지가 같지 않을 때 0이 나온다. 같으면 10진법 숫자가 나온다.
            #     print(0)
            if (S & (1<<int(command[1]))) == (1<<int(command[1])):
                print(1)
            else: print(0)
        elif command[0] == 'remove': # 특정 자리 값을 0으로 바꿔주는 것 이동시킨 다음 반전하여 and 연산한다.
            # print(bin(S))
            S &= ~(1<<int(command[1]))
        # elif a == 'toggle':
        elif command[0] == 'all':
            S = (1 << 21)
            S ^= ~S
            # print(bin(S))
            # 또는 모든 비트를 1로 만들기 위해서는 단수 -1하면 된다. S = (1<<21) -1
        elif command[0] == 'empty':
            S = (1<<21)
            # print(bin(S))
        elif command[0] == 'toggle':
            if S & (1<<int(command[1])) ==0: # 없다는 것인데 없으면 넣어주기
                S |= (1<<int(command[1]))
            else: S &= ~(1<<int(command[1]))

function()
