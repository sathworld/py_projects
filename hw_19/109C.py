#109C
roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabic = [1, 5, 10, 50, 100, 500, 1000]
romArab = dict(zip(roman, arabic))
def toArab(romVal):
    arabVal = 0
    for i in range(len(romVal)):
        if i > 0 and romArab[romVal[i]] > romArab[romVal[i - 1]]:
            arabVal += romArab[romVal[i]] - 2 * romArab[romVal[i - 1]]
        else:
            arabVal += romArab[romVal[i]]
    return arabVal

def repAllRoman(line):
    words = line.split(" ")
    for i in range(len(words)):
        if set(words[i]).issubset(roman):
            words[i]=str(toArab(words[i]))
    return " ".join(words)

line = input("Input a string with roman numerals:\n")
line = repAllRoman(line)
print(line)

