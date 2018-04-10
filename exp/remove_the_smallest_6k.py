arr = [-44, -3, 37, -65, -35, -88, -71, 49, -91, -34, 39, -10, 85, -43, -29, 58, 31, 85, 69, -77, 40, 70, -14, -34, -77, -83, 67, -15, -82, 43, 26, 89, -51]

n = 19


def remove_smallest(n, arr):

    array = list(arr)
    if (n <= 0):
        return array
    if (len(array) <= n):
        return []

    for i in range(0, n):
        x = min(array)
        for item in array:
            if (x == item):
                array.remove(item)
                break

    print(arr)

remove_smallest(n, arr)