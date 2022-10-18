#155A
Fin = open("input.txt")
Fout = open("output.txt", "w")
while True:
    s = Fin.readline()
    if not s: break
    score = int(s.split()[2])
    if score > 80:
        Fout.write(s)
Fin.close()
Fout.close()
