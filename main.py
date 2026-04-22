# SearchSortLab.py
# Name:Devyn Conaway
# Date:4/21/2026
# Assignment: Lab 13 – Searching and Sorting


def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""
    numlist = len(data)
    # TODO: implement linear search
    for i in range(numlist):
        if data[i] == target:
            return i
    return -1


def bubbleSort(data):
    """Sort the list using bubble sort and return the sorted list."""
    numberlist = len(data)
    # TODO: implement bubble sort
    for i in range(numberlist):
        for list in range(0, numberlist - i - 1):
            if data[list] > data[list + 1]:
                data[list], data[list + 1] = data[list + 1], data[list]
    return data


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 10 in randomList:", linearSearch(randomList, 10))

    # Test sorting
    print("Sorted list:", bubbleSort(sortedList.copy()))
    print("Reversed list sorted:", bubbleSort(reversedList.copy()))
    print("Random list sorted:", bubbleSort(randomList.copy()))


if __name__ == "__main__":
    main()
