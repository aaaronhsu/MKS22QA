from math import log2

def explain(l):
    time = 0
    for i in range(l):
        time += i

    print("This solution took", int(l * log2(l)), "passes to solve")
    print("An brute force solution would've taken", time, "passes")
    

def search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        middle = (high + low) // 2

        if values[middle] > target: high = middle - 1
        elif values[middle] < target: low = middle + 1
        else: return True
    return False

def solve(values, sum):
    explain(len(values))

    max = sum / 2
    for i in range(len(values)):
        if i != 0 and values[i] == values[i - 1]: continue
        if values[i] > max: break
        if(search(values[i + 1:], sum - values[i])): return True
    return False

# when len > 6, this solution is faster under all circumstances
addends = [2]
final = 0
print(solve(addends, final))

