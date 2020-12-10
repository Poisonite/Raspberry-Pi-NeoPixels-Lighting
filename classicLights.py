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
        pixels[i] = (51, 50, 46)
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

    # Collect existing pixel info
    iColor = pixels[i]
    jColor = pixels[j]
    kColor = pixels[k]
    lColor = pixels[l]
    mColor = pixels[m]
    nColor = pixels[n]

    # Set white color on twinkle pixels
    pixels[i] = (255, 250, 236)
    pixels[j] = (255, 250, 236)
    pixels[k] = (255, 250, 236)
    pixels[l] = (255, 250, 236)
    pixels[m] = (255, 250, 236)
    pixels[n] = (255, 250, 236)
    pixels.show()
    sleep(0.15)

    # Set twinkle pixels back to normal
    pixels[i] = iColor
    pixels[k] = jColor
    pixels[l] = kColor
    pixels[m] = lColor
    pixels[n] = mColor
    pixels[j] = nColor
    pixels.show()
