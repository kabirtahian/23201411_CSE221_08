def sortingAgain(ids, marks, n):
    swap = 0

    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):

            if marks[j] == marks[j+1]:

                if ids[j] > ids[j+1]:

                    ids[j], ids[j+1] = ids[j+1], ids[j]
                    marks[j], marks[j+1] = marks[j+1], marks[j]
                    swapped = True
                    swap += 1

            elif marks[j] > marks[j+1]:

                ids[j], ids[j+1] = ids[j+1], ids[j]
                marks[j], marks[j+1] = marks[j+1], marks[j]
                swapped = True
                swap += 1 

        if not swapped:
            break

    print(f"Minimum swaps: {swap}")

    for k in range(n):
        print(f"ID: {ids[k]} Mark: {marks[k]}")


n = int(input())
ids = list(map(int, input().split(" ")))
marks = list(map(int, input().split(" ")))

sortingAgain(ids, marks, n)