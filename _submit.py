x = [1, 1, 1, 1, 1, 1, 1]
for i in x:
    if x.count(i) > 1:
        x.remove(i)

print(x)
