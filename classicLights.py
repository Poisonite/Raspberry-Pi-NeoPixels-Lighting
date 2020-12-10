import random
from time import sleep

import board
import neopixel

# Welcome Message
print("Hello, Light Master!\n")
print("Beginning the classic light show!")

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(
    board.D18, 1000, brightness=0.5, auto_write=False, pixel_order=neopixel.RGB)

# Clear any Existing color data
pixels.fill((0, 0, 0))
pixels.show()
print("Cleared existing pixel info.")
sleep(0.5)

# Set Base color
for i in range(1000):
    if (i % 2) == 0:
        pixels[i] = (190, 60, 0)
    else:
        pixels[i] = (30, 30, 35)
pixels.show()

# Begin twinkle
while True:
    # Get pixel list
    i = random.randint(0, 999)
    j = random.randint(0, 999)
    k = random.randint(0, 999)
    l = random.randint(0, 999)
    m = random.randint(0, 999)
    n = random.randint(0, 999)

    # Set white color on twinkle pixels
    pixels[i] = (200, 200, 215)
    pixels[j] = (200, 200, 215)
    pixels[k] = (200, 200, 215)
    pixels[l] = (200, 200, 215)
    pixels[m] = (200, 200, 215)
    pixels[n] = (200, 200, 215)
    pixels.show()
    sleep(0.1)

    # Set twinkle pixels back to normal
    pixels[i] = (190, 60, 0)
    pixels[k] = (190, 60, 0)
    pixels[l] = (190, 60, 0)
    pixels[m] = (190, 60, 0)
    pixels[n] = (190, 60, 0)
    pixels[j] = (190, 60, 0)
    pixels.show()
