file = open("read.txt", 'r')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()
