f = open("input", "r")
changes = f.read()
changes = changes.splitlines()
f.close()

sum = 0
for change in changes:
    op = change[:1]
    value = int(change[1:])
    if op == '+':
        sum += value
    elif op == '-':
        sum -= value

print(sum)
