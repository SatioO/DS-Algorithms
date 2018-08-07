
def main(arr, item):
    low = 0  # #0 #0 #0 #0 #0
    high = len(arr) - 1  # #7 #6 #5 #4 #3

    while low <= high:  # #0 < 7 #0 < 6 #0 < 5 #0 < 4 #0 < 3
        mid = (low + high) / 2  # #3 #3 #2 #2 #1
        guess = arr[mid]  # #4 #4 #3 #3 #2

        if guess == item:  # 2 == 2
            return mid

        if guess > item:  # #4 > 2 #4 > 2 #3 > 2 #3 > 2
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    print(main(arr, 2))
