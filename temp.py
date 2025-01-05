from led_controller import control_leds

def main():
    try:
        # Get the LED numbers from the mapping
        strip1_leds = [90, 88, 84, 82, 2, 4, 6, 8]
        strip2_leds = [136, 134, 132, 130, 47, 49, 51, 53, 55]

        # Control LEDs with the obtained LED indices
        control_leds(strip1_leds, strip2_leds)

    except ValueError as e:
        print(f"Error processing time: {e}")

if __name__ == "__main__":
    main()


