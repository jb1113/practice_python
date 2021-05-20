file = open("create.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄\n" % i
    file.write(data)

file.close()

