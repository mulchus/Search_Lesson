from random import sample


def s(numbers, target_):
    left, right = 0, len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] < target_:
            left = middle + 1
        elif numbers[middle] > target_:
            right = middle - 1
        else:
            return middle
    return


if __name__ == "__main__":
    numbers_len = 10
    rand_numbers = sorted(sample(range(0, 101, 2), numbers_len))  # 10 случайных четных числе по порядку.

    try:
        target = int(input('Pick a positive number between 0-100: '))

        if target > 100 or target < 0:
            print('Invalid input')

        target_index = s(rand_numbers, target)

        print(f'List: {rand_numbers}')
        if target_index:
            print(f'Found {target} in index {target_index}')
        else:
            print(f'Cannot find {target} in the list')
    except ValueError:
        print('Invalid input')
