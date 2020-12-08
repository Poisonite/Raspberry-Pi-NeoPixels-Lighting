import board
import neopixel
from time import sleep

# Welcome Message
print("Hello, Light Master!")

# Better input Syntax:
# num = int(input("Enter a number: ")

# Set Config Params
print("Enter number of pixels to modify:")
pixelCount = input()
pixelCount = int(pixelCount)

print("Enter brightness of pixels (float between 0-1):")
brightness = input()
brightness = float(brightness)

print("Enter RGB data for color one(int between 0-255).")
print("Red: ")
red1 = input()
red1 = int(red1)
print("Green: ")
green1 = input()
green1 = int(green1)
print("Blue: ")
blue1 = input()
blue1 = int(blue1)

print("Enter RGB data for color two(int between 0-255).")
print("Red: ")
red2 = input()
red2 = int(red2)
print("Green: ")
green2 = input()
green2 = int(green2)
print("Blue: ")
blue2 = input()
blue2 = int(blue2)

# Output user's config info
print("Beginning test light operation with perams: ")
print('Pixels: {pixelCount}')
print('Brightness: {brightness}')
print('Color One: ({red1}, {green1}, {blue1})')
print('Color Two: ({red2}, {green2}, {blue2})')

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(board.D18, pixelCount, brightness=brightness)

# Clear any Existing color data
pixels.fill((0, 0, 0))
print("Cleared existing pixel info.")
sleep(2)
# Assign the new colors
for i in range(pixelCount):
    print(i)

# pixels.fill((red, green, blue))
pixels.show()
print('Updated pixel color info to: ({red}, {green}, {blue}).')

# Notify user of script completion
print("Finished sending pixel instructions.")
