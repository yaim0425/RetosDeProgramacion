previous, next = 0, 1
for i in range(50):
    print(previous, end=' ')
    previous, next = next, previous + next
print()
