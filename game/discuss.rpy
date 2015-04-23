init python:
    if persistent.endings is None:
        persistent.endings = set()
    
    def merge_endings(old, new, current):
        current.update(old)
        current.update(new)
    
    renpy.register_persistent('endings', merge_endings)

label discuss:
    $ finished = len(persistent.endings)
    menu:
        "Hi there, did you enjoy the game?":
            # duh, dirty trick
            jump discuss
        "Yes":
            "Great!"
            if finished == 1:
                "Then why don't check out other endings?"
            "You have seen [finished] of 5 endings."
            if finished == 5:
                "Good job!"
        "No":
            "Not a bit of it?{w} That's a bit sad."
            if finished == 5:
                "Still you finished all the endings!{w} Good job!"
            else:
                if finished == 1:
                    "This isn't the only way for story to end though."
                "Why not check out another ending to see if you like it better?"
                "You have seen [finished] of 5 endings."
        "End questions..":
            return
label discuss_0:
    menu:
        "So, are you from Ludum Dare?":
            jump discuss_0
        "Yes":
            "Here's a {a=http://ludumdare.com/compo/ludum-dare-32/?action=preview&uid=17960}link{/a}
            for voting"
            "And here's a {a=https://github.com/caryoscelus/dis/releases/download/v0.1-ld32/dis-0.1-all.zip}secret link{/a} to the Jam version of the game!"
        "No":
            "Well, in case you're interested, this game was {a=http://ludumdare.com/compo/ludum-dare-32/?action=preview&uid=17960}initially made{/a} for Ludum Dare."
        "End questions..":
            return
label discuss_1:
    
    return
