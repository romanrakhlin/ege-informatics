# Определите максимальное количество идущих подряд символов,
# среди которых нет символов G, W, P.

with open("24.txt") as f:
    data = f.readline()

count = 0
countMax = 0
err = "GWP"

for i in data:
    if i not in err:
        count += 1
    else:
        if count > countMax:
            countMax = count
        count = 0

print(countMax)

# Ответ: 83