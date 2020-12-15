import sys
sys.stdin = open('in.txt')
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS로 특정한 노드 방문후 연결된 모든 노드 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우 즉시 종료
    if x<0 or x>=n or y<0 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1

print(result)

         