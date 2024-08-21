def convert_unit(value, unit):
    if unit == 'kg':
        return f'{value * 2.2046:.4f} lb'
    elif unit == 'lb':
        return f'{value * 0.4536:.4f} kg'
    elif unit == 'l':
        return f'{value * 0.2642:.4f} g'
    elif unit == 'g':
        return f'{value * 3.7854:.4f} l'

T = int(input())

for _ in range(T):
    value, unit = input().split()
    value = float(value)
    print(convert_unit(value, unit))
    