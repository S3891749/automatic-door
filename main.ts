input.onSound(DetectedSound.Loud, function () {
    lightson = !(lightson)
    if (lightson) {
        servos.P0.setAngle(0)
        music.playMelody("- B A G A G A B ", 120)
    }
    basic.showLeds(`
        . . . . .
        # . # . #
        # . # . #
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        # # # . .
        # . . . .
        # # # . .
        # . . . .
        # # # . .
        `)
    basic.showLeds(`
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # # # . .
        `)
    basic.showLeds(`
        . # # . .
        # . . . .
        # . . . .
        # . . # .
        . # # . .
        `)
    basic.showLeds(`
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        # # . # #
        # . # . #
        # . # . #
        # . . . #
        `)
    basic.showLeds(`
        # # # . .
        # . . . .
        # # # . .
        # . . . .
        # # # . .
        `)
    basic.clearScreen()
})
let lightson = false
servos.P0.setAngle(180)
basic.forever(function () {
	
})
