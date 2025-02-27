LETTERS = [
    ['I', 'T', 'L', 'I', 'S', 'X', 'S', 'A', 'M', 'P', 'M'],
    ['X', 'C', 'Q', 'U', 'A', 'R', 'T', 'E', 'R', 'D', 'C'],
    ['T', 'W', 'E', 'N', 'T', 'Y', 'F', 'I', 'V', 'E', 'X'],
    ['H', 'A', 'L', 'F', 'S', 'T', 'E', 'N', 'F', 'T', 'O'],
    ['P', 'A', 'S', 'T', 'E', 'R', 'U', 'N', 'I', 'N', 'E'],
    ['O', 'N', 'E', 'S', 'I', 'X', 'T', 'H', 'R', 'E', 'E'],
    ['F', 'O', 'U', 'R', 'F', 'I', 'V', 'E', 'T', 'W', 'O'],
    ['E', 'I', 'G', 'H', 'T', 'E', 'L', 'E', 'V', 'E', 'N'],
    ['S', 'E', 'V', 'E', 'N', 'T', 'W', 'E', 'L', 'V', 'E'],
    ['T', 'E', 'N', 'S', 'E', 'O', 'C', 'L', 'O', 'C', 'K'],
]

LED_INDEXES = [
    [101, 99, 97, 95, 93, 91, 89, 87, 85, 83, 81],  # strip 1
    [58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78],  # strip 1
    [55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35],  # strip 1
    [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],  # strip 1
    [136, 134, 132, 130, 128, 126, 124, 122, 120, 118, 116],  # strip 2
    [93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113],  # strip 2
    [90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70],  # strip 2
    [47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67],  # strip 2
    [44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24],  # strip 2
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],  # strip 2
]

STRIP_SEPARATOR_ROW = 4


def get_led_numbers(sentence):
    """
    Traverse the grid once to extract LED numbers for the given sentence by matching continuous words.

    :param sentence: Input string (e.g., "IT IS FIVE PAST TEN").
    :return: Two lists: (strip1_leds, strip2_leds).
    :raises ValueError: If any word cannot be matched.
    """
    # Normalize the sentence
    words = sentence.upper().split()  # Split into words

    # Initialize LED lists
    strip1_leds = []
    strip2_leds = []

    # Traverse the LETTERS grid until all words are matched
    for row_idx, row in enumerate(LETTERS):
        row_string = ''.join(row)  # Combine row into a single string
        search_start = 0
        while words:  # Process as long as there are words left

            if search_start >= len(row_string):
                break

            word = words[0]  # Look at the first word
            start_index = row_string.find(word, search_start)  # Search for the word in the current row

            if start_index != -1:  # If the word is found
                # Map LEDs for the word
                for char_idx in range(start_index, start_index + len(word)):
                    led = LED_INDEXES[row_idx][char_idx]
                    if row_idx < STRIP_SEPARATOR_ROW:
                        strip1_leds.append(led)
                    else:
                        strip2_leds.append(led)

                search_start = start_index + len(word)
                words.pop(0)  # Remove the matched word
            else:
                break  # Move to the next row if the word isn't found in the current row

        if not words:  # Break early if all words are matched
            break

    # If there are unmatched words
    if words:
        raise ValueError(f"Cannot match words: {' '.join(words)}")

    return strip1_leds, strip2_leds

#
# strip1, strip2 = get_led_numbers("IT IS QUARTER TO TEN")
# print('{}, {}'.format(strip1, strip2))
