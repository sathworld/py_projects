def two_sum(numbers, target):
    # Sifting through all numbers until we find a pair
    for i in range(len(numbers)):
        try:
            j = numbers.index(target - numbers[i])
            if i == j:
                continue
            else:
                return i, j
        except ValueError:
            # Do nothing
            continue
