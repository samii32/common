#미로 탈출
import sys
from collections import deque
sys.stdin = open('in.txt')

#0은 못가는곳, 1은 갈수있는곳
n, m = map(int, input().split())

arr = [[int(x) for x in input()] for _ in range(n)]
for a in arr:
    print(a)