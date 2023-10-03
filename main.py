set_item_to_10 = 10
counting = False

def on_button_pressed_a():
    global set_item_to_10, counting
    if not counting:
        counting = True
        while set_item_to_10 > 0:
            basic.show_number(set_item_to_10)
            set_item_to_10 -= 1
            basic.pause(1000)
        counting = False
        basic.show_string("Selesai")

def on_button_pressed_b():
    global set_item_to_10
    set_item_to_10 = 10

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
