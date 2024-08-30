import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))
rank = {x: i for i, x in enumerate(sorted_arr)}
print(*[rank[x] for x in arr])