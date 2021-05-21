file = open("append.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄\n" % i
    file.write(data)

file.close()
