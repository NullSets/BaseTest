

#冒泡排序

def sort(menbers):

    for i in range(len(menbers) -1) :
        for j in range(len(menbers) -1  - i):
            if menbers[j] > menbers[j + 1]:
                menbers[j],menbers[j + 1] = menbers[j + 1],menbers[j]
                # a = menbers[j + 1]
                # menbers[j + 1] = menbers[j]
                # menbers[j] = a
            print(menbers)


if __name__ == "__main__":
    menbers = [23,12,9,15,6]
    sort(menbers)

