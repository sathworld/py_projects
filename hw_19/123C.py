#123C
names=[]
name = input("Enter up to 20 full names:\n")
count = 0
while name and count < 20:
    count+=1
    names.append(name)
    if count == 20:
        break
    name = input()
names.sort(key=lambda x:x[5:])
print("Alphabet sorted names:")
for i in names:
    print(i)

