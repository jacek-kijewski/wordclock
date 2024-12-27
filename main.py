import board
from led_mapping import create_letter_to_led_mapping, letters
from word_clock import WordClock

if __name__ == "__main__":
    strip_configs = [
        (board.D12, 138),  # strip1
        (board.D10, 91),   # strip2
    ]

    letter_to_led = create_letter_to_led_mapping()

    clock = WordClock(strip_configs, letter_to_led, letters)

    clock.display_sentence("IT IS FIVE")
