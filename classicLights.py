# Python core imports
import random
from time import sleep

# Import GPIO ref and pixel instructions
import board
import neopixel

# Base Settings
pixelCount = 2000
brightness = 0.4

# Color Settings
baseColor1 = (190, 60, 0)
baseColor2 = (255, 189, 109)
twinkleColor = (255, 250, 236)

# Prod Twinkle Settings
twinkleCountMin = 10
twinkleCountMax = 50
twinkleTimeMin = 0.05
twinkleTimeMax = 0.3

# Welcome Message
print("Hello, Light Master!\n")
print("Beginning the classic light show!")

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(
    board.D18, pixelCount, brightness=brightness, auto_write=False, pixel_order=neopixel.RGB)

# Clear any Existing color data
pixels.fill((0, 0, 0))
pixels.show()
print("Cleared existing pixel info")
sleep(0.5)

# Set Base color
print("Setting base color per pixel")
for i in range(pixelCount):
    if (i % 2) == 0:
        pixels[i] = baseColor1
    else:
        pixels[i] = baseColor2
pixels.show()     

# Begin twinkle
print("Start twinkle pattern")
while True:
    # Store the pixels which will be changed
    my_pixels = {}
    i = 0

    # Get pixel list
    for i in range(random.randint(twinkleCountMin, twinkleCountMax)):
        # Define important info for the pixel to be changed
        pixelNum = random.randint(0, pixelCount-1)
        pixelColor = pixels[pixelNum]
        my_pixels[pixelNum] = pixelColor

    # Set twinkle pixels to twinkle color
    for pixel in my_pixels.keys():
        pixels[pixel] = twinkleColor

    # Output the finished set of changes and wait
    pixels.show()
    sleep(random.uniform(twinkleTimeMin, twinkleTimeMax))

     # Set twinkle pixels back to org
    for pixel in my_pixels.keys():
        pixels[pixel] = my_pixels[pixel]

    # Output the reset pixels
    pixels.show()