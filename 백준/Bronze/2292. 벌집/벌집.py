N = int(input())

if N == 1:
    print(1)
else:
    layer = 1
    current_layer = 1
    
    while N > current_layer:
        layer += 1
        current_layer += 6 * (layer-1)
        
    print(layer)