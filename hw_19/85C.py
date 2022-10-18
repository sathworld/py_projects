#85C
def maxlen(x):
    return len(x)
words = input("Enter a string:\n").split(" ")
maxlenword = max(words, key = maxlen)
print("The longest word is:",maxlenword,", its' length is",len(maxlenword))
