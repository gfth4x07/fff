import py5
def setup():
    py5.size(200,200)
    #py5.full_screen()

def draw():
    py5.rect(py5.mouse_x,py5.mouse_y,10,10)
    
py5.run_sketch()