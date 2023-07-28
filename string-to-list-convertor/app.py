myl = []
with open("input.txt", "r") as data:
    myl = list(data.read().split('\n'))
    myl.sort()
    print(myl)