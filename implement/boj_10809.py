words=list(map(str,input()))
alphabet_position=[-1 for i in range(26) ]

for i in range(len(words)):
    value = ord(words[i]) - ord('a')

    if alphabet_position[value] < 0:
        alphabet_position[value] = i


for num in alphabet_position:
    print(num)

