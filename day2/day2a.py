f = open("input", "r")
changes = f.read()
changes = changes.splitlines()
f.close()

def inputHasElementWithNoOfOccurences(input, count):
    input = list(input)
    return len(set([x for x in input if input.count(x) == count])) > 0

noOfTwoOccurences = 0
noOfThreeOccurences = 0
for input in changes:
    if(inputHasElementWithNoOfOccurences(input, 3)):
        noOfThreeOccurences += 1
    if(inputHasElementWithNoOfOccurences(input, 2)):
        noOfTwoOccurences += 1

print(noOfTwoOccurences*noOfThreeOccurences)
