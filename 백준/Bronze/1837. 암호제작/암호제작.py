def is_bad_key(P,K):
    K = int(K)
    
    for i in range(2, K):
        if P % i == 0:
            return f"BAD {i}"
    return "GOOD"

P, K = input().split()
P = int(P)
print(is_bad_key(P,K))