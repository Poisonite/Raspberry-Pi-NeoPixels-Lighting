import board
import neopixel

# Welcome Message
print("Hello, Light Master!\n")
print("Beginning the test!")

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(
    board.D18, 2000, brightness=0.5, pixel_order=neopixel.RGB)

# Clear any Existing color data
pixels.fill((0, 255, 0))
print("Set 1000 lights to 0,255,0 (green)")