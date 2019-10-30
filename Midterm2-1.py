#Display name of the sneder of all emails 
Total_count = 0
fname = 'mail.txt'

try:
    fh = open(fname)
except FileNotFoundError:
    print('File not found ')
    quit()

for line in fh:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        Total_count = Total_count + 1
        neww = words[1].split('@')
        print(neww[0].replace('.', ' '))
        

print(Total_count)

    
