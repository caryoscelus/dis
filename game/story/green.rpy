label green_branch:
    nvl clear
    "I decide to head into the kitchen first.{w} When i open the door, bright light almost blinds me."
    "..."
    nvl clear
    scene green
    "Green.{w} Bright, unnatural green."
    "Green.{w} Not the colour of grass and leaves, but the colour of a LED lamp in the beautiful decorated shade, hanging from the ceiling."
    scene bg kitchen censor at bg
    with dissolve
    "I look around.{w} This is indeed a kitchen.{w} Small, but cozy.{w} All the place in the centre is taken by a wooden table.{w} There's a bottle of wine and two glasses on it.{w} One glass is empty and another one is half-full."
    "Between the glasses there's something that i don't see quite clearly."
    "The rest of kitchen is filled with nice furniture, none of which pique my curiosity."
    "All of it looks normal and familiar.{w} Even lack of window feels appropriate."
    "I make a few steps forward and then suddenly..{nw}"
    $ renpy.music.set_volume(0.5, channel='sound')
    play sound "sfx/white-noise.ogg"
    show char ghost at bg:
        alpha 1.0
        pause 0.4
        alpha 0
    window hide
    pause 0.4
    window show
    "Ugh, what was that?"
    "I feel sharp pain in the back of my head.{w} And..{w} have i just seen something?"
    "Nevermind."
    "..."
    nvl clear
    "Suddenly i realize i feel thirsty.{w} I think i'll just drink this wine.{w} I sit on the nearest chair and make a few gulps of red liquid.{w} Even though i drink it hastily, i still feel it's really tasty."
    play sound "sfx/white-noise.ogg"
    show char ghost at bg:
        alpha 1.0
        pause 0.4
        alpha 0
    window hide
    pause 0.4
    window show
    "Aww..{w} the pain strikes again in the back of my head.{w} I even close my eyes for a moment.{nw}"
    scene black
    with dissolve
    pause 0.5
    scene bg kitchen at bg
    with dissolve
    "When it ceases, i'm still sitting on the chair and in front of, on the table, stays laptop.{w} I haven't payed much attention to it before, but now it's so close that i can't help being interested."
    nvl clear
    "Top lid is open and LEDs are indicating it's on.{w} I put my finger on touchpad and the screen turns on."
    "Fortunately, there's no lock screen and i see the desktop wallpaper.{w} There are few minimized windows so i skim through them.{w} File manager, IDE, music player and web browser.{w} The latter is opened on page with text \"Ludum Dare 32 theme is..\""
    "I don't feel like reading further.{w} Pain pokes me in the back of my head, but this time it's not strong."
    "I close the browser.{w} I briefly look at IDE, but there's only a freshly-created project named ld32 in it."
    "After this, i completely lose interest in laptop."
    nvl clear
    "I pour another glass of wine and start drinking it.{w} This time slowly, enjoying every bit of noble liquid."
    "Time passes slowly."
    "..."
    nvl clear
    scene black
    with blinds
    scene bg kitchen at bg
    with blinds
    "..."
    nvl clear
    scene bg kitchen blur at bg
    "Green.{w} Even a bit unnatural, this light makes me feel peacefully."
    "Green.{w} All the green coloured objects start to blur and blend in my head as alcohol gets into effect."
    "Yes, this is what i want."
    "This could be an artificial peace, but as long as i can stay here, that's ok."
    "Occasional attacks of headache are still bothering me, but they are beginning to be more and more rare."
    "This is how it should be.{w} Green."
    nvl clear
    scene green
    with dissolve
    ":: green end ::"
    $ persistent.endings.add('green')
    return
