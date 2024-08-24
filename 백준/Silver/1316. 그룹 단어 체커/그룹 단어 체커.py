N = int(input()) 
group_word_count = 0

for _ in range(N):
    word = input().strip()
    is_group_word = True
    
    for i in range(len(word) - 1):
        if word[i] != word[i + 1] and word[i] in word[i + 1:]:
            is_group_word = False
            break

    if is_group_word:
        group_word_count += 1

print(group_word_count)
