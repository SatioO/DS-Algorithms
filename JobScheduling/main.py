import argparse
import json


def quick_sort_helper(data, start, end):
    # 1. set pivot element
    pivot_element = data[start]
    # 2. set start and end marks
    leftmark = start + 1
    rightmark = end
    #3. flag for status
    done = False

    while not done:
        while data[leftmark]['profit'] <= pivot_element['profit'] and leftmark <= rightmark:
            leftmark = leftmark + 1

        while rightmark >= leftmark and data[rightmark]['profit'] >= pivot_element['profit']:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[start]
    data[start] = data[rightmark]
    data[rightmark] = temp
    return rightmark


def quick_sort(data, start, end):
    if start < end:
        partition = quick_sort_helper(data, start, end)
        quick_sort(data, start, partition - 1)
        quick_sort(data, partition + 1, end)
    print(data)


def main(args):
    with open(args.data) as f:
        data = json.loads(f.read())

    quick_sort(data, 0, len(data) - 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-data", type=str, default="data.json", help="Document name")
    args = parser.parse_args()
    main(args)