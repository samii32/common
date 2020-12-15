# 시간기준으로 이분탐색.
# 비트연산자
# <<n 2의 n제곱: 왼쪽으로 쉬프트이동하면 곱이된다.
# >>n 2를 n번 나눔: 오른쪽으로 쉬프트이동하면 나눗셈이된다.

n = 4
times = [2,3,10]

def binarySearch(l, r, n, times):

    mid = (l+r)>>1
    cnt = 0 #통과한 사람
    #해당 mid시간을 기준으로 몇명이 통과했는지 확인해본다.
    for time in times:
        cnt += mid//time
    #통과한 사람이 n보다 작으면 이분탐색 다시 수행       
    if l>r:
        return l    
    if cnt<n:
        return binarySearch(mid+1,r,n,times)
    elif cnt>=n:
        return binarySearch(l,mid-1,n,times)
    
def solution(n, times):
    l = 0
    r = (max(times)*n)//len(times)
    answer = binarySearch(l,r, n, times)
    return answer

print(solution(n,times))