
def find_smallest(list):
    smallest_index = 0

    for i, item in enumerate(list):
        if item < list[smallest_index]:
            smallest_index = i

    return smallest_index


def main():
    list = [5, 3, 6, 2, 10]
    newArr = []

    for i in range(len(list)):
        smallest = find_smallest(list)
        newArr.append(list.pop(smallest))

    print(newArr)


if __name__ == "__main__":
    main()
