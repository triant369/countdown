let set_item_to_10 = 10
let counting = false
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (!counting) {
        counting = true
        while (set_item_to_10 > 0) {
            basic.showNumber(set_item_to_10)
            set_item_to_10 -= 1
            basic.pause(1000)
        }
        counting = false
        basic.showString("Selesai")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    set_item_to_10 = 10
})
