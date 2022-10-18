Fin = open('input.txt')
Fout = open('output.txt', 'w')
summ = 0
count = 0

while True:
    s = Fin.readline()
    if s == '':
        break
    summ += int(s)
    count += 1
Fout.write(str((summ/count)))
Fin.close()
Fout.close()
