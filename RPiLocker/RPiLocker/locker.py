import time


class Locker():
    '''
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.enable()
    
    
    def set(self, prop, value):
        try:
            f = open("/sys/class/rpi-pwm/pwm0/" + prop, 'w')
            f.write(value)
            f.close()    
        except:
            print("Error writing to: " + prop + " value: " + value)
        
            
    def setAbsolutePosition(self, angle):
        self.set("servo", str(angle))
    
    
    def open(self):
        self.setAbsolutePosition(0)
    
    
    def close(self):
        self.setAbsolutePosition(180)
        
        
    def enable(self):
        self.set("delayed", "0")
        self.set("mode", "servo")
        self.set("servo_max", "180")
        self.set("active", "1")
    
    
    def disable(self):
        time.sleep(0.5)
        self.set("active", "0")
