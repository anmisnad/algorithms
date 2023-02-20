def int_binary_search(sorted_list_length: int, item: int):

    sorted_list = [n for n in range(1, sorted_list_length)]

    low = 0
    high = len(sorted_list)-1
    step_counter = 0

    while low <= high:
        step_counter += 1
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == item:
            return mid, step_counter

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None, step_counter


def main():

    list_length = int(input('Input desired list length: '))
    search_item = int(input('Input number for which index should be found: '))

    index, step_count = int_binary_search(list_length, search_item)

    print(
        f"Found number {search_item} at index {index}."
        f"This took {step_count} steps."
    )


if __name__ == '__main__':
    main()
