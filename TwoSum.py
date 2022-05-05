def two_sum(numbers, target):
    # Creating an empty hashmap
    hashmap = {}
    for i in range(len(numbers)):
        # Evaluating the number at the chosen index
        n = numbers[i]
        # Difference between target and current number
        difference = target - n
        # Searching hashmap for key
        if difference in hashmap:
            # Returning the set of indices
            return i, hashmap[difference]
        else:
            # Adding a new item pair to the hashmap
            hashmap[n] = i
