arr = [5,4,3,2,1]

def quick_sort(arr, start, end):
    if start >= end: # arr의 길이가 1일 경우 stop
        return
    # 변수 설정
    pivot = start
    left = start + 1
    right = end

    while(left <= right): # 초기 세팅은 right의 index가 크다. 따라서 left의 index가 right의 index보다 크거나 같으면 stop
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if(left > right): # 이미 엇갈렸음
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았으면 left와 right를 바꾼다.
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

def quick_python(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quick_python(left_side) + [pivot] + quick_python(right_side)

# quick_sort(arr, 0, len(arr)-1)
print(*quick_python(arr))