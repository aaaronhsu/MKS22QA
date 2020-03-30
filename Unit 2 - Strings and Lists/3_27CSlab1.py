# classwork
def part1():
    l = ["Apple", "Pear", "Orange", "Peach", "Cherry", "Banana", "Strawberry"]

    l.append(input("Input a fruit: "))
    print(l)

    print(l[int(input("Input an index to see a fruit: "))])

    l.insert(0, input("Input another fruit to add to the beginning: "))
    print(l)

    l.remove(l[-1])
    print(l)

    print(l.index(input("Input a fruit to find position: ")) + 1)

    part2(l)

def part2(l):
    for i in l:
        if i[0] == "P":
            print(i)

    for i in range(len(l) - 1, -1, -1):
        l.insert(i, "Apple")
    print(l)

    for i in range(len(l)):
        if l[i] == "Pear":
            l[i] = "Orange"
    print(l)

    disliked = []
    for i in range(len(l)):
        if not disliked.count(l[i]):
            user = input("Do you like " + l[i] + "?: ")

        while not(user == "yes" or user == "no"):
            print("Answer 'yes' or 'no'")
            user = input("Do you like " + l[i] + "?: ")

        if user == "no":
            disliked += [l[i]]
    for i in disliked:
        for a in range(l.count(i)):
            l.remove(i)
    print(l)

    part3()

def part3(l):
    revl = l.copy()
    for i in range(len(revl)):
        revl[i] = revl[i][::-1]

    l.pop(len(l) - 1)
    print(l)

    revl.pop(2)
    print(revl)

    for i in range(len(l) - 1, -1, -1):
        if l.count(l[i]) > 1:
            l.pop(i)
    print(l)

    l.sort()
    print(l)

part1()
