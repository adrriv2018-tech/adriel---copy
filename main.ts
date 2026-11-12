basic.showLeds(`
    . # # # .
    # . # . #
    # # # # #
    # # # # #
    # . # . #
    `)
music.setTempo(233)
music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
EventBusValue.MES_DPAD_BUTTON_1_UP
music.setBuiltInSpeakerEnabled(true)
EventBusValue.MES_DPAD_BUTTON_B_DOWN
music.stopMelody(MelodyStopOptions.All)
basic.forever(function on_forever() {
    for (let index = 0; index < 262; index++) {
        music.play(music.stringPlayable("- A C5 G D C5 - C ", 120), music.PlaybackMode.UntilDone)
    }
})
music.setVolume(7456)
