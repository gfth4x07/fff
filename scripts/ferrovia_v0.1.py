from gpiozero import LED

def setup():
    size(666,400)
    global bg, b1, b2, b3, b4, L, R #Para poder chmar no draw
    bg = load_shape("../painel.svg")

    b1 = Botao_toggle(115,5,60,60,"1",4)
    b2 = Botao_toggle(10,120,60,60,"2",17)
    b3 = Botao_toggle(37,252,60,60,"3",27)
    b4 = Botao_toggle(460,93,60,60,"4",22)
    L = Botao_push(520,325,60,60,"←",23)
    R = Botao_push(590,325,60,60,"→",24)


def draw():
    background(255)
    shape(bg,0,0)
    b1.display()
    b2.display()
    b3.display()
    b4.display()
    L.display()
    R.display()
    
    
def mouse_pressed():
    #print (mouse_x,mouse_y)
    pass

class Botao_push():
    '''Button with only pressed option'''
    def __init__(self, x, y, w, h, t, pin):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.t = t
        self.pressed = False
        self.led = LED(pin)
        self.led.off()

    def on(self):
        self.led.on()
        self.state = True
    
    def off(self):
        self.led.off()
        self.state = False
    
    def mouse_over(self):
        return (self.x < mouse_x < self.x + self.w and
                self.y < mouse_y < self.y + self.h)

    def display(self):
        mouse_over = self.mouse_over()
        if mouse_over and is_mouse_pressed:
            fill(140)
        elif mouse_over:
            fill(205)
        else:
            fill(255)
        rect_mode(CORNER)
        rect(self.x, self.y, self.w, self.h, 5)
        fill(0)
        text_align(CENTER, CENTER)
        text(self.t,
             self.x + self.w / 2,
             self.y + self.h / 2)

        if mouse_over and self.pressed and not is_mouse_pressed:
            self.pressed = False
            self.off()
            return True
        if mouse_over and is_mouse_pressed:
            self.pressed = True
            self.on()
        else:
            self.pressed = False
            self.off()
            
        return False
    
class Botao_toggle():
    '''Button with pressed and state option'''
    def __init__(self, x, y, w, h, t, pin):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.t = t
        self.pressed = False
        self.state = False
        self.led = LED(pin)
        self.led.off()

    def on(self):
        self.led.on()
        self.state = True
    
    def off(self):
        self.led.off()
        self.state = False


    def mouse_over(self):
        return (self.x < mouse_x < self.x + self.w and
                self.y < mouse_y < self.y + self.h)

    def display(self):
        mouse_over = self.mouse_over()
        if mouse_over:
            fill((not self.state)*185,self.state*185,0)
        else:
            fill((not self.state)*255,self.state*255,0)
        rect_mode(CORNER)
        rect(self.x, self.y, self.w, self.h, 5)
        fill(0)
        text_align(CENTER, CENTER)
        text(self.t,
             self.x + self.w / 2,
             self.y + self.h / 2)

        if mouse_over and self.pressed and not is_mouse_pressed:
            self.pressed = False
            self.state = not self.state
            self.led.toggle()
            return True
        
        if mouse_over and is_mouse_pressed:
            self.pressed = True
        else:
            self.pressed = False
            
        return False

