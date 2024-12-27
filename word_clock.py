import neopixel

class WordClock:
    def __init__(self, strip_configs, letter_to_led, letters):
        self.strips = [
            neopixel.NeoPixel(pin, num_pixels, brightness=0.1, auto_write=False)
            for pin, num_pixels in strip_configs
        ]
        self.letter_to_led = letter_to_led
        self.letters = letters
    def display_sentence(self, sentence, color=(255, 197, 80)):
        for strip in self.strips:
            strip.fill((0, 0, 0))

        for word in sentence.split():
            for row_idx, row in enumerate(self.letters):
                start_idx = row.find(word)
                if start_idx != -1:
                    for i in range(len(word)):
                        led_info = self.letter_to_led.get((row_idx, start_idx + i))
                        if led_info:
                            strip_index, led_number = led_info
                            self.strips[strip_index][led_number] = color

        for strip in self.strips:
            strip.show()
