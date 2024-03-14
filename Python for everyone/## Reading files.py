## Reading files
#what is a handle?
 ## handle = open(filename,mode)
## file name is a string, mode is r (read) or w (write)
## This is the assign a designated handle or name which opens the delegated file in order to read or write it
## this returns the encoding which is the character set 
filehandle = open('mbox.txt') # assigns the handle 'filehandle' to '.healer.txt'
count = 0   
for line in filehandle: ### for loop of every line in the 'filehandle' 
    count = count + 1    #### it will increase the count by 1
print('Line Count: ', count) ### outputs the amount of lines by displaying the count