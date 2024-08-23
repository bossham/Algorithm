dial = [
    'ABC',  
    'DEF', 
    'GHI', 
    'JKL', 
    'MNO',  
    'PQRS',
    'TUV',   
    'WXYZ'  
]
word = input()
total = 0

for char in word:
    for idx, group in enumerate(dial):
        if char in group:
            total += idx+3
            break
            
print(total)