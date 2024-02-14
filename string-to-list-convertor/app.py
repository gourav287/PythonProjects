myl = []
with open("input.txt", "r") as data:
    myl = list(data.read().split('\n'))
    myl.sort()
    print(f"Total number of strings: {len(myl)}")
    for i in range(1, len(myl)+1):
        print("'", myl[i-1], "'", sep = "", end=', ')
        if i%20 == 0:
            print()
