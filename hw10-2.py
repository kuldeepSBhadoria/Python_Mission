import string
counts = 0                          
dictionary_counts = dict()
relative_lst = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
            # Count each letter for relative frequencies
            #dictionary_counts[letter] = dictionary_counts.get(letter, 0) + 1
            counts += 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1

for key, val in list(dictionary_counts.items()):
    relative_lst.append((100 * (val / counts), key))  

relative_lst.sort(reverse=True)         

for key, val in relative_lst:
    print(key, val)
    
