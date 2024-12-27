# edit
letters = [
    "ITLISASAMPM",
    "ACQUARTERDC",
    "TWENTYFIVEEX",
    "HALFSTENFTO",
]

led_indexes = [
    [90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70],
    [47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67],
    [44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22],
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
]

def create_letter_to_led_mapping():
    letter_to_led = {}
    strip_index = 1  # strip2
    for row_idx, row in enumerate(letters):
        for col_idx, letter in enumerate(row):
            if col_idx < len(led_indexes[row_idx]):
                led_number = led_indexes[row_idx][col_idx]
                letter_to_led[(row_idx, col_idx)] = (strip_index, led_number)
    return letter_to_led
