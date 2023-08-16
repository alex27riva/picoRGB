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
        self.red_val = red_val
        self.green_val = green_val
        self.blue_val = blue_val
        self.red_pin_pwm = PWM(Pin(self.red_pin))
        self.green_pin_pwm = PWM(Pin(self.green_pin))
        self.blue_pin_pwm = PWM(Pin(self.blue_pin))
        self.setColor(red_val,green_val,blue_val)
     
    def show(self):
        print("Led pins ({},{},{}), current values ({},{},{})".format(self.red_pin,self.green_pin, self.blue_pin, self.red_val, self.green_val, self.blue_val))
        
    def setColor(self,r,g,b):
        if self.ledType == 'anode':
            self.red_val = r
            self.green_val = g
            self.blue_val = b
            r = map(r,0,255,65534,0)
            g = map(g,0,255,65534,0)
            b = map(b,0,255,65534,0)
            self.red_pin_pwm.duty_u16(r)
            self.green_pin_pwm.duty_u16(g)
            self.blue_pin_pwm.duty_u16(b)
        elif self.ledType == 'cathode':
            self.red_val = r
            self.green_val = g
            self.blue_val = b
            r = map(r,0,255,0,65534)
            g = map(g,0,255,0,65534)
            b = map(b,0,255,0,65534)
            self.red_pin_pwm.duty_u16(r)
            self.green_pin_pwm.duty_u16(g)
            self.blue_pin_pwm.duty_u16(b)
    
    def off(self):
        self.setColor(0,0,0)
    
    def red(self):
        self.setColor(255,0,0)

    def green(self):
        self.setColor(0,255,0)
    
    def blue(self):
        self.setColor(0,0,255)

    def white(self):
        self.setColor(255,255,255)
    
    def yellow(self):
        self.setColor(255,255,0)
    
    def magenta(self):
        self.setColor(255,0,255)
    
    def cyan(self):
        self.setColor(0,255,255)
        
    def slowSet(self,r,g,b,delay = 0.01):
        if r>self.red_val:
            rStep = 1
        else:
            rStep -= 1
        
        if g>self.green_val:
            gStep = 1
        else:
            gStep = -1
            
        if b>self.blue_val:
            bStep = 1
        else:
            bStep = -1

        if self.ledType == 'anode':
            for i in range(self.red_val,r,rStep):
                x = map(i,0,255,65534,0)
                self.red_pin_pwm.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.green_val,g,gStep):
                x = map(i,0,255,65534,0)
                self.green_pin_pwm.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.blue_val,b,bStep):
                x = map(i,0,255,65534,0)
                self.blue_pin_pwm.duty_u16(x)
                utime.sleep(delay)
                
        elif self.ledType == 'cathode':
            for i in range(self.red_val,r,rStep):
                x = map(i,0,255,0,65534)
                self.red_pin_pwm.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.green_val,g,gStep):
                x = map(i,0,255,0,65534)
                self.green_pin_pwm.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.blue_val,b,bStep):
                x = map(i,0,255,0,65534)
                self.blue_pin_pwm.duty_u16(x)
                utime.sleep(delay)
                
        self.red_val = r
        self.green_val = g
        self.blue_val = b
        self.setColor(r,g,b)
