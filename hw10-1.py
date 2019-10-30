hours= dict()
l = list()

fname = input('Enter file name : ')
try:
    fh = open(fname)
except FileNotFoundError:
    print('File not found ')
    quit()

for line in fh:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    #print(words[5])
    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    #print(hour)
    #hours[hour] = hours.get(words,0) + 1
    if hour not in hours:
        hours[hour] = 1
    else:
        hours[hour] += 1

for key,val in list(hours.items()):
    l.append((key,val))
l.sort()

for key,val in l:
    print(key , val)
    
