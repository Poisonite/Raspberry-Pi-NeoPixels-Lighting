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

# Twinkle Settings
twinkleCountMin = 10
twinkleCountMax = 50
twinkleTimeMin = 0.01
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

# Define a structued class for the pixel data
class PixelSettings:
  def __init__(self, num, orgColor):
    self.num = num
    self.orgColor = orgColor

# Begin twinkle
print("Start twinkle pattern")
while True:
    # Store the pixels which will be changed
    pixelSettingArr = []

    # Get pixel list
    for i in range(random.randint(twinkleCountMin, twinkleCountMax)):
        # Define important info for the pixel to be changed
        pixelNum = random.randint(0, pixelCount-1)
        pixelColor = pixels[pixelNum]

        # Set white color on twinkle pixels
        pixels[pixelNum] = twinkleColor

        # Structure the collected data
        pixelSetting = PixelSettings(pixelNum, pixelColor)

        # Add structured settings to storage arr
        pixelSettingArr.append(pixelSetting)

    # Output the finished set of changes and wait
    pixels.show()
    sleep(random.uniform(twinkleTimeMin, twinkleTimeMax))

    # Set twinkle pixels back to org
    for pixelSetting in pixelSettingArr:
        pixels[pixelSetting.num] = pixelSetting.orgColor

    # Output the reset pixels
    pixels.show()