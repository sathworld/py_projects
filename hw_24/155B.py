# 155B
Fin = open("input.txt")
Fout = open("output.txt", "w")
count = 1
while True:
    s = Fin.readline()
    l = s.split(" ")
    if not s: break
    score = int(l[2])
    if score > 80:
        line = str(count) + " " + l[1][0] + ". " + l[0] + " " + l[2]
        Fout.write(line)
        count += 1
Fin.close()
Fout.close()
