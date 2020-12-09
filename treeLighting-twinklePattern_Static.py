import board
import neopixel
from time import sleep

# Welcome Message
print("Hello, Light Master!")

# Output config info
print("\nBeginning test light operation with perams: ")
print(f'Pixels: 100')
print(f'Brightness: 0.5')
print(f'Twinkle Speed: 1 second(s)')
print(f'\nColor One: (255, 0, 0)')
print(f'Color Two: (0, 255, 0)')

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(board.D18, 100, brightness=0.5)

# Clear any Existing color data
pixels.fill((0, 0, 0))
print("Cleared existing pixel info.")
sleep(2)

# Infinity loop so pattern continues to change
runs = 0
while runs >= 0:
    # Runs a delay before the next change happens
    sleep(1.5)

    # Changes which pattern is used depending on what was used in the last run
    if (runs % 2) == 0:
        # Assign the new colors
        for i in range(100):
            if (i % 2) == 0:
                pixels[i] = (255, 0, 0)
            else:
                pixels[i] = (0, 255, 0)
    else:
        # Assign the new colors
        for i in range(100):
            if (i % 2) == 0:
                pixels[i] = (0, 255, 0)
            else:
                pixels[i] = (255, 0, 0)

pixels.show()
print(f'Updated pixel color info to:\n(255, 0, 0) and (0, 255, 0).')

# Notify user of script completion
print("\nFinished sending pixel instructions.")
