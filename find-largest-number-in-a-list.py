arr = [10, 4, 5, 5, 6, 8]


def find_max(arr_list: list[int]) -> str:
    largest = arr_list[0]

    for n in arr_list:
        if (n > largest):
            largest = n

    return largest


if (len(arr) > 0):
    maximum = find_max(arr)
    print(maximum)

    new_arr = [n for n in arr if n != maximum]
    runner_up = find_max(new_arr)

    print(runner_up)
