from picoRGB import RGBLed

led = RGBLed(15,14,13,RGBLed.cathode)

"""
led = RGBLed(#Red pin,#Green pin, #Blue pin,#RGB Led type -anode or cathode)
led.off() -              Turn off all colors
led.set(120,50,75)       Set color Set(#Red Led,#Green Led,#Blue Led)  
led.slowSet(10,200,195)  Set color slowly SlowSet(#Red Led,#Green Led,#Blue Led,#delay - optional)
led.show()               Show last color values
led.red()              Set RGB led to red (255,0,0)
led.green()              Set RGB led to green (0,255,0)
led.blue()              Set RGB led to blue (0,0,255)
led.white()              Set RGB led to white (255,255,255)
led.yellow()             Set RGB led to yellow (255,255,0)
led.magenta()            Set RGB led to magenta (255,0,255)
led.cyan()               Set RGB led to cyan (0,255,255)  
"""
while True:
    led.slowSet(0,0,0)
    led.slowSet(255,255,255)
