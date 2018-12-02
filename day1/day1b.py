f = open("input", "r")
changes = f.read()
changes = changes.splitlines()
f.close()

sum = 0
index = 0
frequencies = set()
while(True):
    op = changes[index][:1]
    value = int(changes[index][1:])
    if op == '+':
        sum += value
    elif op == '-':
        sum -= value

    if sum in frequencies:
        print(sum)
        break
    else:
        frequencies.add(sum)

    index += 1
    if(index == len(changes)):
        index = 0
