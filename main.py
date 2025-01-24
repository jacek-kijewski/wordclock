from led_controller import control_leds
from led_mapping import get_led_numbers
from time_calculator import time_in_words
import time

def main():
    # Get current time
    current_time = time.localtime()  # Get the current local time
    time_str = time.strftime("%H:%M", current_time)  # Format time as "HH:MM"
    current_hours = current_time.tm_hour % 12  # Convert to 12-hour format
    current_minutes = current_time.tm_min
    # Convert the current time to words

    time_words = time_in_words(current_hours, current_minutes)


    print(f"Current time: {time_str} -> {time_words}")

    try:
        # Get the LED numbers from the mapping
        strip1_leds, strip2_leds = get_led_numbers(time_words)

        print(f"LEDs for strip 1: {strip1_leds}")
        print(f"LEDs for strip 2: {strip2_leds}")
        # Control LEDs with the obtained LED indices
        control_leds(strip1_leds,strip2_leds)

    except ValueError as e:
        print(f"Error processing time: {e}")

if __name__ == "__main__":
    main()


