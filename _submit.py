
sum = 0
past = 250
for i in range(100):
    sum += past
    past /= (5/2)

print(sum)