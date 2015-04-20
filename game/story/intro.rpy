label story:
    scene red
    "Red.{w} The colour of roses, poppy and luxurious velvet."
    "Red.{w} The colour of sunset, ruby and wine."
    "Red.{w} The colour of ladybirds, apples and oldschool tiled roofs."
    "..."
    "No, that's not right.{w} There's a mistake somewhere."
    "..."
    nvl clear
    "Red.{w} Pure red.{w} Vivid, sickening colour."
    "Red.{w} The colour of blood."
    "Yes, now that is correct."
    "What is before my eyes is blood.{w} A lot of blood.{w} I could've said \"a sea of blood\" if not for the fact that it was all splattered on various objects."
    "Objects? Yes, if i concentrate i can see that blood is not the only thing i see.{w} It only covers everything around, but the normal world is still around."
    "When i look careful, it actually looks a lot like a normal room, which even seems familiar to me.{w} But something is odd.{w} The angle at which i look at it?"
    "Yes, that is correct again.{w} I finally realize i've been lying on the floor all this time.{w} I start to feel my body, but when i try to move, i meet resistance.{w} My body is really tired.{w} My muscles ache.{w} Why haven't i realized it before?"
    nvl clear
    "With a significant effort, i finally get up and look around."
    "This room.{w} Painted in blood, yet chillingly familiar.{w} I try not to think about it."
    "The window? Closed with blinds, painted in blood."
    "The door? Semi-opened, with a few red splashes on it."
    "Perhaps, i should move out of here.{w} It's hard to think in this red room.{w} It's even hard to breeze."
    "I fumble through the exit and close the door behind me."
    "..."
    nvl clear
    scene black
    "Black.{w} Darkness.{w} This is way, way better.{w} I feel like the air itself is more light here."
    "Black.{w} There are no light sources in here and i can't see anything.{w} But the more i look, the more my eyes are getting used to this darkness."
    "Soon i can make out vague shapes which make up a corridor.{w} There are several doors."
    "First, the door back to the first room behind me."
    "Second, presumably the exit door, at the end of corridor."
    "Third one i think leads to the kitchen."
    "And then there's also a door to the bathroom.{w} Or at least i have feeling it is."
    menu:
        "Return to the room":
            jump red_branch
        "Exit outside":
            jump white_branch
        "Check the kitchen":
            jump green_branch
        "Visit bathroom":
            jump blue_branch
        "Stay here":
            jump black_branch
