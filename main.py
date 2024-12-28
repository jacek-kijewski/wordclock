from led_controller import control_leds
from led_mapping import get_led_numbers
from time_calculator import time_to_words
import time

def main():
    # Get current time
    current_time = time.localtime()  # Get the current local time
    time_str = time.strftime("%H:%M", current_time)  # Format time as "HH:MM"

    # Convert the current time to words
    time_in_words = time_to_words(time_str)
    print(f"Current time: {time_str} -> {time_in_words}")

    try:
        # Get the LED numbers from the mapping
        strip1_leds, strip2_leds = get_led_numbers(time_in_words)

        # Control LEDs with the obtained LED indices
        control_leds(strip1_leds, strip2_leds)

    except ValueError as e:
        print(f"Error processing time: {e}")

if __name__ == "__main__":
    main()


