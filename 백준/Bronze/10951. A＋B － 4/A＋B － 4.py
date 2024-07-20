import sys
input = sys.stdin.read

data = input().strip().split('\n')

for line in data:
    A,B = map(int, line.split())
    print(A+B)