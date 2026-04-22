from py5 import size, mouse_x, mouse_y, run_sketch
def setup():
    size(200,200)

def draw():
    rect(mouse_x,mouse_y,10,10)
    
run_sketch()