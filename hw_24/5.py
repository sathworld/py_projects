Fin = open('input.txt')
Fout = open('output.txt', 'w')
a=[]
while True:
    s = Fin.readline()
    if s == '':
        break
    a.append(int(s))
a.sort()

for i in a:
    Fout.write(str(i)+"\n")
Fin.close()
Fout.close()
