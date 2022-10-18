#117C
def createWord(word, letters, n):
    if n < 1:
        if len(set(list(word)))<len(list(word)):
            print(word)
        return
    for c in letters:
        createWord(word+c, letters, n - 1)

k = int(input('Enter K\n'))
letters = ["Ы", "Ш", "Ч", "О"]

createWord("", letters, k)
