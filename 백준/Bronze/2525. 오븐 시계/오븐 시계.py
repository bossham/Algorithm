A, B = map(int, input().split())
C = int(input())
total = A*60 + B + C

end_H = (total//60)%24
end_M = total%60
print(end_H, end_M)