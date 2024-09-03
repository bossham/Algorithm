t = int(input())

for _ in range(t):
    ps = input()
    stack = []
    is_vps = True
    
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
                
    if stack:
        is_vps = False
    if is_vps:
        print("YES")
    else:
        print("NO")