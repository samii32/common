# BFS 아이스크림의 갯수
import sys
from collections import deque

sys.stdin = open('in.txt')
r, c = map(int,input().split())

arr = [[int(x) for x in input()] for _ in range(r)]
dr = [[-1,0],[0,-1],[1,0],[0,1]]
visited=[[False for _ in range(c)] for _ in range(r)]

#0인부분의 갯수를 센다.
def bfs(x,y):
    Q = deque()
    visited[x][y]=True
    Q.append([x,y])

    while Q:
        cx, cy = Q.popleft()

        for d in range(4):
            nx, ny = cx+dr[d][0], cy+dr[d][1]
            if nx<0 or ny<0 or nx>=r or ny>=c: continue

            if not visited[nx][ny] and not arr[nx][ny]:
                visited[nx][ny]=True
                Q.append([nx,ny])

ans = 0
for i in range(r):
    for j in range(c):
        if not arr[i][j] and not visited[i][j]:
            bfs(i,j)
            ans +=1 
           
print(ans)

#입력예시
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111