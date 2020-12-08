import board
import neopixel
from time import sleep

# Welcome Message
print("Hello, Light Master!\n")

# Set Config Params
pixelCount = int(input("Enter number of pixels to modify: "))
brightness = float(input("Enter brightness of pixels (float between 0-1): "))

print("\nEnter the RGB data(int between 0-255).")
red = int(input("Red: "))
green = int(input("Green: "))
blue = int(input("Blue: "))

# Output user's config info
print("\nBeginning test light operation with perams: ")
print(f'Pixels: {pixelCount}')
print(f'Brightness: {brightness}')
print(f'\nColor Data: ({red}, {green}, {blue})')

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(board.D18, pixelCount, brightness=brightness)

# Clear any Existing color data
pixels.fill((0, 0, 0))
print("Cleared existing pixel info.")
sleep(2)
# Assign the new colors
pixels.fill((red, green, blue))
pixels.show()
print(f'Updated pixel color info to: ({red}, {green}, {blue}).')

# Notify user of script completion
print("\nFinished sending pixel instructions.")
