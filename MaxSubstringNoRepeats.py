# Returns the length of the max substring that does not contain repeating characters
def max_substring_no_repeats(string):
    # Define starting variables
    # Index of the left boundary of the sliding window
    left_boundary = 0
    # Contents of the sliding window
    characters = set()
    # The set of length of results, 0 is pre-included to deal with an empty string
    results = {0}

    # Sliding the window right
    for right_boundary in range(len(string)):
        # While the new character already exists in the window:
        while string[right_boundary] in characters:
            # Remove the leftmost character from the window
            characters.remove(string[left_boundary])
            # Shift the leftmost boundary right
            left_boundary += 1
        # Add the new character to the window
        characters.add(string[right_boundary])
        # Add the length of the window to the set of results
        results.add(right_boundary - left_boundary + 1)
    # Return the max length of the window
    return max(results)
