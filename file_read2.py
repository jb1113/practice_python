file = open("read.txt", 'r')
lines = file.readlines()
print(lines)
for line in lines:
    print(line)
file.close()
