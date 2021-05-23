data = ""
file1 = open("test.txt", 'r')
lines = file1.readlines()
for line in lines:
    if "java" in line:
        data = data + line.replace("java", "python")
    else:
        data = data + line
file1.close()

file2 = open("test.txt", 'w')
file2.write(data)
file2.close()

