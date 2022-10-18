n = int(input("Enter N: "))
c = 0
for i in range(n):
    words = input().split(" ")
    if int(words[2]) > 100:
        c += 1
print(c)
