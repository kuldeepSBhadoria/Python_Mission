#Display Dictonary and print who sent how many emails

dictionary_counts = dict()

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
        dictionary_counts[words[1]] = dictionary_counts.get(words[1], 0) + 1
        

for k, v in dictionary_counts.items():
    print(k, v)
    
