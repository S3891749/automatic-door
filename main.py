def on_sound_loud():
    global lightson
    lightson = not (lightson)
    if lightson:
        servos.P0.set_angle(0)
        music.play_melody("- B A G A G A B ", 120)
    basic.show_leds("""
        . . . . .
                # . # . #
                # . # . #
                . # # # .
                . . . . .
    """)
    basic.show_leds("""
        # # # . .
                # . . . .
                # # # . .
                # . . . .
                # # # . .
    """)
    basic.show_leds("""
        # . . . .
                # . . . .
                # . . . .
                # . . . .
                # # # . .
    """)
    basic.show_leds("""
        . # # . .
                # . . . .
                # . . . .
                # . . # .
                . # # . .
    """)
    basic.show_leds("""
        . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                # # . # #
                # . # . #
                # . # . #
                # . . . #
    """)
    basic.show_leds("""
        # # # . .
                # . . . .
                # # # . .
                # . . . .
                # # # . .
    """)
    basic.clear_screen()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

lightson = False
servos.P0.set_angle(180)

def on_forever():
    pass
basic.forever(on_forever)
