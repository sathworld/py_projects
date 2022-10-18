# 156C
def sortScore(lin):
    lin = lin.split(" ")
    return int(lin[2])


Fin = open("input.txt")
Fout = open("output.txt", "w")
a = []
counter = 0
while True:
    s = Fin.readline()
    if not s: break
    score = int(s.split()[2])
    if score > 80:
        
        a.append(s)
a.sort(key=sortScore, reverse=True)
for l in a:
    counter += 1
    l=l.split(" ")
    line = str(counter)+") "+ l[1][0] + ". " + l[0] + " " + l[2]
    Fout.write(line)
Fin.close()
Fout.close()
