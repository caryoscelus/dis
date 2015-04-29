label blue_branch:
    nvl clear
    "I realize my hands seems to be sticky and decide to visit bathroom first.{w} I open the door and hear subtle click of lamp turning on.{w} Light isn't that bright by itself, but it's reflected multiple times from glossy surfaces, so i'm forced to protect my eyes from it."
    "..."
    nvl clear
    scene blue
    "Blue.{w} Cold and somewhat mysterious colour."
    "Blue.{w} Colour of sea and sky.{w} But here on quaint ceramic tiles it doesn't bring the lightness or expansing freedom to the atmosphere of the room.{w} It only symbolizes lifeless water enclosed in the pipes."
    scene bg bathroom at bg
    with dissolve
    "I close the door behind me and look around.{w} There's a bath with a curtain, toilet in the corner and tap on opposite wall."
    "First things first.{w} I make few steps towards tap and start washing hands with warm water and soap."
    "It feels nice, except for looking at all the dirty water and realizing it all coming from my hands."
    "..."
    nvl clear
    "When my hands are finally clean, i close the faucet and start looking for towel."
    show char mirror at bg
    with dissolve
    "But instead..{w} woah, what?!"
    "I am startled looking at myself in the mirror."
    "My face..{w} it's covered with blood, which looks almost black in this blue-shaded room.{w} It's not that visible on my black hair, but by the way strands are glued and messed up i can guess they are bloody as well."
    "For a moment i see my face in the mirror make scary smile.{w} No, that's not me! I don't smile like that!"
    "But, blood!{w} I check my face with my clean hands and it feels sticky and dirty."
    "I look at my hands and sure enough they are covered with dark red substance."
    "What does that mean?!{w} Why?!"
    "I am pretty sure i'm not hurt anywhere, so this must be someone else's blood.{w} But, that much?.."
    nvl clear
    "Looking at myself more closely i notice blood is everywhere on my clothes as well.{w} It disgusts me.{w} I rip the clothes apart and take them off."
    hide char
    with dissolve
    "Only then i realize i may not be able to find new clothes, but i don't care."
    play music "sfx/24092__dobroide__20061021-just-shower.flac" fadeout 1.0 fadein 1.0
    "I enter the bath and turn hot water on."
    "Minutes pass slowly as i wash away all the blood from my body."
    "..."
    nvl clear
    "Then i close the waste drain and water starts to fill the bath."
    "I lie down on already warm curved surface and watch the water, thinking about these strange events."
    "My bloody face..{w} And that violent grin..{w} And me awakening in a bloody room — all that leads to one conclusion: i might be the one made something terrible."
    "But then, what?"
    nvl clear
    "I don't know what exactly happened there.{w} I don't know reason for that to happen.{w} I don't even..{w} yes, in fact, i don't even know who i am!"
    "I look at my reflection in the water.{w} Now my face and wet hair are clean.{w} But still, i don't feel like it belongs to me.{w} It only seems vaguely familiar."
    "I look at my naked body to the same effect.{w} It doesn't strike me as me unknown or unfamiliar, but it certainly doesn't feel like my own."
    "And maybe even more importantly, i can't remember a thing from my past.{w} It doesn't feel like bumping into invisible wall, but it feels like looking into empty abyss.{w} There's no resistance in my memory, only emptiness."
    "Just who am i?!"
    "..."
    "If there's no answer to this question, i would need to make one myself."
    nvl clear
    "Thinking that, i watch the water.{w} The process is really soothing."
    "..."
    nvl clear
    scene bg bathroom blur at bg
    with dissolve
    "Blue.{w} With growing depth, crystal-clear water gains soft blue shade."
    "Blue.{w} The colour of my future.{w} Mystical, cold, but also so pure and refreshing."
    "Yes, all is left for me is rebirth.{w} And here's a good start."
    "Only a first step on my path to the blue skies."
    "But for now, it's just good to be here, in blue."
    nvl clear
    scene blue
    ":: blue end ::"
    $ persistent.endings.add('blue')
    return
