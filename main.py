basic.show_leds("""
    . # # # .
    # . # . #
    # # # # #
    # # # # #
    # . # . #
    """)
music.set_tempo(233)
music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
    music.PlaybackMode.UNTIL_DONE)
EventBusValue.MES_DPAD_BUTTON_1_UP
music.set_built_in_speaker_enabled(True)
EventBusValue.MES_DPAD_BUTTON_B_DOWN
music.stop_melody(MelodyStopOptions.ALL)

def on_forever():
    for index in range(262):
        music.play(music.string_playable("- A C5 G D C5 - C ", 120),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
music.set_volume(7456)