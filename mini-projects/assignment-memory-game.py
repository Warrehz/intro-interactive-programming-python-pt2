# implementation of card game - Memory

import simplegui
import random

card_list = ["0", "0", "1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7"]
random.shuffle(card_list)
exposed_list = ["false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false"]
turns = 0

# helper function to initialize globals
def new_game():
    global state
    state = 0
    global turns
    turns = 0
    global exposed_list
    exposed_list = ["false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false"]
    random.shuffle(card_list)

# define event handlers
def mouseclick(pos):
    global exposed_list
    global state
    global card1
    global idx_card1
    global card2
    global idx_card2
    global turns
    # add game state logic here
    for i in range(0, 16):
        if (i * 50) <= pos[0] <= ((i + 1) * 50):
            if exposed_list[i] == "false":
                if state == 0:
                    exposed_list[i] = "true"
                    card1 = card_list[i]
                    idx_card1 = i
                    state = 1
                elif state == 1:
                    exposed_list[i] = "true"
                    card2 = card_list[i]
                    idx_card2 = i
                    state = 2
                    turns += 1
                else:
                    if card1 == card2:
                        state = 1
                        card1 = card_list[i]
                        idx_card1 = i
                        exposed_list[i] = "true"
                    else:
                        exposed_list[idx_card1] = "false"
                        exposed_list[idx_card2] = "false"
                        state = 1
                        card1 = card_list[i]
                        idx_card1 = i
                        exposed_list[i] = "true"
            else:
                pass

# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(0, 16):
        if exposed_list[i] == "false":
            canvas.draw_polygon([[0 + i * 50, 0], [50 + i * 50, 0], [50 + i * 50, 100], [0 + i * 50, 100]], 1, "Green", "Green")
        else:
            canvas.draw_text(card_list[i], (20 + (i * 50 ) , 55), 20, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("turns label")
label.set_text("Turns = %s" % turns)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
