from pico2d import *

open_canvas(736,521)
background = load_image('TUK_GROUND.png')
character = load_image('sprite.png')

center = get_canvas_width()/2,get_canvas_height()/2 # window center

x,y = 400,center[1]   # character pos
move_speed = 15
quit = False

class Ani:
    cur_frame =0
    offset_x = 74       # ani offset x
    offset_y = 80       # ani offset y 
    max_frame = [9,9,9,9,2,0,2,2]    # sprite max frame
    cur_ani = 0         # cur ani ( from img_bottom )

def DrawAnimation():
    global x,y
    clear_canvas()
    background.draw(center[0],center[1])
    MoveCharacter()
    character.clip_draw(Ani.cur_frame*Ani.offset_x,Ani.cur_ani*Ani.offset_y,Ani.offset_x,Ani.offset_y
                        ,x,y)
    update_canvas()
 
def SetFrame():
    Ani.cur_frame += 1
    if (Ani.cur_frame > Ani.max_frame[Ani.cur_ani]):    # Frame reset
        Ani.cur_frame =0

    delay(0.1)

def MoveCharacter():
    pass

def handle_event():
    global quit,dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit = True
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                quit=True
            elif event.key ==SDLK_UP:
                Ani.cur_ani = 1
                Ani.cur_frame = 0
            elif event.key == SDLK_DOWN:
                Ani.cur_ani = 3
                Ani.cur_frame = 0
            elif event.key == SDLK_LEFT:
                Ani.cur_ani = 2
                Ani.cur_frame = 0
            elif event.key == SDLK_RIGHT:
                Ani.cur_ani = 0
                Ani.cur_frame = 0

while (not quit):
    SetFrame()
    handle_event()
    DrawAnimation()


close_canvas()