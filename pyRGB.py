from machine import PWM, Pin
import utime

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

class RGBLed:
    anode = 'anode'
    cathode = 'cathode'
    
    def __init__(self, red_pin, green_pin, blue_pin, ledType, red_val = 0, green_val = 0, blue_val=0):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.ledType = ledType
        self.currentValueR = red_val
        self.currentValueG = green_val
        self.currentValueB = blue_val
        self.setColor(red_val,green_val,blue_val)
     
    def show(self):
        print("Red Pin:", self.red_pin)
        print("Green Pin:", self.green_pin)
        print("Blue Pin:", self.blue_pin)
        print("Led Type:",self.ledType)
        print("Current Red Value:",self.currentValueR)
        print("Current Green Value:",self.currentValueG)
        print("Current Blue Value:",self.currentValueB)
        
    def setColor(self,r,g,b):
        if self.ledType == 'anode':
            self.currentValueR = r
            self.currentValueG = g
            self.currentValueB = b
            
            r = map(r,0,255,65534,0)
            g = map(g,0,255,65534,0)
            b = map(b,0,255,65534,0)
            red_pin_pwm = PWM(Pin(self.red_pin))
            green_pin_pwm = PWM(Pin(self.green_pin))
            blue_pin_pwm = PWM(Pin(self.blue_pin))
            red_pin_pwm.duty_u16(r)
            green_pin_pwm.duty_u16(g)
            blue_pin_pwm.duty_u16(b)
        elif self.ledType == 'cathode':
            self.currentValueR = r
            self.currentValueG = g
            self.currentValueB = b
            
            r = map(r,0,255,0,65534)
            g = map(g,0,255,0,65534)
            b = map(b,0,255,0,65534)
            red_pin_pwm = PWM(Pin(self.red_pin))
            green_pin_pwm = PWM(Pin(self.green_pin))
            blue_pin_pwm = PWM(Pin(self.blue_pin))
            red_pin_pwm.duty_u16(r)
            green_pin_pwm.duty_u16(g)
            blue_pin_pwm.duty_u16(b)
    
    def off(self):
        self.setColor(0,0,0)
        
    def white(self):
        self.setColor(255,255,255)
    
    def yellow(self):
        self.setColor(255,255,0)
    
    def magenta(self):
        self.setColor(255,0,255)
    
    def cyan(self):
        self.setColor(0,255,255)
        
    def slowSet(self,r,g,b,delay = 0.01):
        if r>self.currentValueR:
            rStep = 1
        else:
            rStep -= 1
        
        if g>self.currentValueG:
            gStep = 1
        else:
            gStep = -1
            
        if b>self.currentValueB:
            bStep = 1
        else:
            bStep = -1

        if self.ledType == 'anode':
            for i in range(self.currentValueR,r,rStep):
                x = map(i,0,255,65534,0)
                red_pin_pwm = PWM(Pin(self.red_pin))
                red_pin_pwm.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.currentValueG,g,gStep):
                x = map(i,0,255,65534,0)
                green_pin_pwm = PWM(Pin(self.green_pin))
                green_pin_pwm.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.currentValueB,b,bStep):
                x = map(i,0,255,65534,0)
                blue_pin_pwm = PWM(Pin(self.blue_pin))
                blue_pin_pwm.duty_u16(x)
                utime.sleep(delay)
                
        elif self.ledType == 'cathode':
            for i in range(self.currentValueR,r,rStep):
                x = map(i,0,255,0,65534)
                red_pin_pwm = PWM(Pin(self.red_pin))
                red_pin_pwm.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.currentValueG,g,gStep):
                x = map(i,0,255,0,65534)
                green_pin_pwm = PWM(Pin(self.green_pin))
                green_pin_pwm.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.currentValueB,b,bStep):
                x = map(i,0,255,0,65534)
                blue_pin_pwm = PWM(Pin(self.blue_pin))
                blue_pin_pwm.duty_u16(x)
                utime.sleep(delay)
                
        self.currentValueR = r
        self.currentValueG = g
        self.currentValueB = b
        self.setColor(r,g,b)
