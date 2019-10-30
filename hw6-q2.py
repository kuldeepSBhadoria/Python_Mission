count = 0 # Initialize variables
total = 0
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()

for line in fhand:    
    if line.startswith('X-DSPAM-Confidence:'):     
        str1 = line
        index = str1.find(':')
        total += float(str1[index+1:])
        count = count + 1
        

average = total / count
print('Average spam confidence: ', average)
