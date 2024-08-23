pieces = [1,1,2,2,2,8]
found_pieces = list(map(int, input().split()))

result = [correct - found for correct, found in zip(pieces, found_pieces)]
print(*result)