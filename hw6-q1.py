try:
    fhand = open('mbox-short.txt')
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()
    
for line in fhand:
    y = line.upper()
    print(y)
