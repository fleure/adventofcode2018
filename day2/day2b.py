from itertools import permutations

f = open("input", "r")
changes = f.read()
changes = changes.splitlines()
f.close()

for tuple in list(permutations(changes,2)):
    answer_phrase = ''
    mismatches = 0
    for i, phrase in enumerate(tuple[0]):
        if(tuple[1][i] == phrase):
            answer_phrase += phrase
        else:
            mismatches += 1

    if(mismatches == 1):
        print(answer_phrase)
            
