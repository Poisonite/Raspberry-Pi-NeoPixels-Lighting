import board
import neopixel
from time import sleep

# Welcome Message
print("Hello, Light Master!")

# Set Config Params
print("Enter number of pixels to modify:")
pixelCount = input()
pixelCount = int(pixelCount)

print("Enter brightness of pixels (float between 0-1):")
brightness = input()
brightness = float(brightness)

print("Enter RGB data 1 by 1(int between 0-255).")
print("Red: ")
red = input()
red = int(red)
print("Green: ")
green = input()
green = int(green)
print("Blue: ")
blue = input()
blue = int(blue)

# Output user's config info
print("Beginning test light operation with perams: ")
print('Pixels: {pixelCount}')
print('Brightness: {brightness}')
print('Color: ({red}, {green}, {blue})')

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(board.D18, pixelCount, brightness=brightness)

# Clear any Existing color data
pixels.fill((0, 0, 0))
print("Cleared existing pixel info.")
sleep(2)
# Assign the new colors
pixels.fill((red, green, blue))
pixels.show()
print('Updated pixel color info to: ({red}, {green}, {blue}).')

# Notify user of script completion
print("Finished sending pixel instructions.")
