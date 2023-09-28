from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('sprite.png')

mouse_x, mouse_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character_x,character_y = mouse_x,mouse_y
move_speed = 15
quit = False
hide_cursor()

class Ani:
    cur_frame =0
    offset_x = 74       # ani offset x
    offset_y = 80       # ani offset y 
    max_frame = [9,9,9,9,2,0,2,2]    # sprite max frame
    cur_ani = 0         # cur ani ( from img_bottom )

def DrawAnimation():
    global mouse_x,mouse_y,character_x,character_y
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    mouse.draw(mouse_x,mouse_y)
    MoveCharacter()
    character.clip_draw(Ani.cur_frame*Ani.offset_x,Ani.cur_ani*Ani.offset_y,Ani.offset_x,Ani.offset_y
                        ,character_x,character_y)
    update_canvas()
 
def SetFrame():
    Ani.cur_frame += 1
    if (Ani.cur_frame > Ani.max_frame[Ani.cur_ani]):    # Frame reset
        Ani.cur_frame =0
def MoveCharacter():
    pass

def handle_event():
    global quit,mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit = True
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                quit=True
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
    pass

def main():
    while (not quit):
        SetFrame()
        handle_event()
        DrawAnimation()

    close_canvas()

main()



