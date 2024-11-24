#this is just the beginning

from collections import Counter

filename = ""
#text = open(filename)
text = "the quick brown fox jumped over the lazy dog"

specialChars = ".!?-][}{\"\'\\<>@#$%^&*()+=|,/ "

n = 2
counts = Counter()
window = []

exerpt = text.split()

for word in exerpt:
    clean_word = word.lower().strip(specialChars)
    if len(window) >= n:
        counts[tuple(window)] += 1
        window.pop(0)
    
    window.append(clean_word)
        
        
print(counts.most_common(5))