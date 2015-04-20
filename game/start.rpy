define narrator = Character(
        kind=nvl,
        what_size=24,
        what_color='#eeeeee',
        what_outlines=[(3, '#222222cc', 0, 0)],
    )

label start:
    call story
    call credits
    return
