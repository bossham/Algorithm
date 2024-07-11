def solution(order):
    price = 0
    for item in order:
        if 'americano' in item or item == 'anything':
            price += 4500
        elif 'latte' in item:
            price += 5000
    return price