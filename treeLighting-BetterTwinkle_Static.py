import random
import board
import neopixel
from time import sleep

# Welcome Message
print("Hello, Light Master!")

# Output config info
print("\nBeginning test light operation with perams: ")
print(f'Pixels: 100')
print(f'Brightness: 0.5')
# print(f'Twinkle Speed: 1 second(s)')
print(f'\nColor One: (255, 0, 0)')
print(f'Color Two: (0, 255, 0)')

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(board.D18, 1000, brightness=0.75, auto_write=False)

# Clear any Existing color data
pixels.fill((0, 0, 0))
print("Cleared existing pixel info.")
sleep(2)

# Infinity loop so pattern continues to change
# runs = 0
pixels.fill((50, 190, 0))
while True:

    i = random.randint(0, 999)
    pixels[i] = (200, 200, 215)

    # pixels.show()

    j = random.randint(0, 999)
    pixels[j] = (200, 200, 215)

    # pixels.show()

    k = random.randint(0, 999)
    pixels[k] = (200, 200, 215)

    # pixels.show()

    l = random.randint(0, 999)
    pixels[l] = (200, 200, 215)

    # pixels.show()

    m = random.randint(0, 999)
    pixels[m] = (200, 200, 215)

    # pixels.show()

    n = random.randint(0, 999)
    pixels[n] = (200, 200, 215)
    pixels.show()
    pixels[i] = (50, 190, 0)
    pixels[k] = (50, 190, 0)
    pixels[l] = (50, 190, 0)
    pixels[m] = (50, 190, 0)
    pixels[n] = (50, 190, 0)
    pixels[j] = (50, 190, 0)
    pixels.show()

# pixels.show()
print(f'Updated pixel color info to:\n(255, 0, 0) and (0, 255, 0).')

# Notify user of script completion
print("\nFinished sending pixel instructions.")
