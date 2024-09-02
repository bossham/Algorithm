import sys

input = sys.stdin.read
commands = input().splitlines()[1:]
stack = []

for command in commands:
    if command.startswith('push'):
        _, value = command.split()
        stack.append(int(value))
    elif command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if stack else 1)
    elif command == 'top':
        print(stack[-1] if stack else -1)