
outfile = open("e:\\phones.txt", "a")
outfile.write("yayaya1\n")
outfile.write("yayaya2\n")
outfile.write("yayaya3\n")
outfile.close()

infile = open("e:\\phones.txt", "r")
for line in infile:
    line=line.rstrip()
    print(line)
infile.close()
Z
