filehandle = open('mbox.txt')
count = 0
for line in filehandle:
    count= count +1
print('Line count: ', count)
