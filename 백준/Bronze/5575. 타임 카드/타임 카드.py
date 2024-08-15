for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2
    work_seconds = end_time - start_time
    
    h = work_seconds // 3600
    m = (work_seconds % 3600) // 60
    s = work_seconds % 60
    
    print(h, m, s)
