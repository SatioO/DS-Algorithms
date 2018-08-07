# open boxes problem
print("open boxes problem")
print("-------------")


def open(box):
    print(box)
    if box == 0:
        return

    open(box - 1)


open(8)


# factorial problem
print("\nfactorial problem")
print("-------------")


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(3))

# sumation
print("\nsumation problem")
print("-------------")


def sum(arr):
    current_index = len(arr) - 1

    if current_index == 0:
        return arr[current_index]

    return arr[current_index] + sum(arr[:current_index])


print(sum([5, 3, 10, 2]))
