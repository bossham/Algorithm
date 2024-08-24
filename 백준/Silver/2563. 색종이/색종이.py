paper_size = 100
square_size = 10

paper = [[0]* paper_size for _ in range(paper_size)]

n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x, x+square_size):
        for j in range(y, y+square_size):
            paper[i][j] = 1
            
black_area = sum(sum(row) for row in paper)
print(black_area)