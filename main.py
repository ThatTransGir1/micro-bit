import random
import sys
import microbit as mb
print('Starting Program')
while True:
    mb.display.clear
    #temp = mb.temperature()
    #mb.display.scroll(temp,loop=False)
    if mb.button_a.is_pressed() is True:
        print('Button A Pressed')
        mb.display.set_pixel(1,1,5)
        mb.display.scroll('Hello World',loop=False)
    if mb.button_b.is_pressed() is True:
        print('Button B Pressed')
        ranNum = random.random()
        mb.display.scroll(ranNum,loop=False)
        #sys.exit(mb.display.scroll('Exit: 1'))