# -*- coding: utf-8 -*-

# template for "Stopwatch: The Game"

import simplegui
# define global variables
t = 0
text = '0:00.0'
win = '0/0'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenth = str(t % 10)
    rest = t // 10
    sec = str(rest % 60)
    if int(sec) < 10:
        sec = '0'+sec
    minute = str(rest//60)
    return (minute + ':' + sec + '.' + tenth)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def strt_button_handler():   
    global timer
    timer.start()
    return
    
def stp_button_handler():
    global t,timer,win
    timer.stop()  
    total = int(win[-1])+1
    if int(t)%10==0:
        won = int(win[0])+1
    else:
        won = int(win[0])
    win = str(won)+'/'+str(total)
    return 

def rst_button_handler():
    global t, timer, text, win
    timer.stop()
    t=0
    text = '0:00.0'
    win = '0/0'
    

# define event handler for timer with 0.1 sec interval
def event_handler():
    global t,text
    t+=1
    #print (format(t))
    text = format(t)
    

# define draw handler
def draw(canvas):
    canvas.draw_text(text, [110, 110], 36, "White")
    canvas.draw_text(win, [260, 20], 24, "Red")
    
# create frame
frame = simplegui.create_frame("Home", 300, 200)
frame.set_canvas_background('Black')

# register event handlers
timer = simplegui.create_timer(100, event_handler)
frame.add_button("Start", strt_button_handler, 100)
frame.add_button("Stop", stp_button_handler, 100)
frame.add_button("Reset", rst_button_handler, 100)
frame.set_draw_handler(draw)



# start frame
frame.start()

# Please remember to review the grading rubric
