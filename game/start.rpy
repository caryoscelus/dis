image ctc_normal = Text(' ➤', color='#eeeeee', outlines=[(1, '#222222cc', 0, 0)],)

define narrator = Character(
        kind=nvl,
        what_size=24,
        what_color='#eeeeee',
        what_outlines=[(3, '#222222cc', 0, 0)],
        ctc='ctc_normal',
        ctc_pause='ctc_normal',
        ctc_position='nestled'
    )

label start:
    call story
    call discuss
    call credits
    return
