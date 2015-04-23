label white_branch:
    nvl clear
    "I don't want to spend any more time in this apartment so i head straight to the exit door in the end of corridor and unlock it.{w} Upon opening the door bright sun blinds me."
    "..."
    nvl clear
    scene white
    $ renpy.music.set_volume(0.25, delay=0.5)
    play music "sfx/169906__ainayave__ambient-city.ogg" fadeout 2.0 fadein 2.0
    "White.{w} The colour of empty canvas."
    "White.{w} Pure brightness which knows no competition.{w} Pure light of the distant star bringing energy and life to our planet."
    "When i finally able to see, i find myself on open-air corridor of a high apartment building.{w} I faintly hear the sound of music playing coming from one of the apartment doors.{w} In the background there's also the usual city noise: cars, trains, factories all contribute to the ambience."
    "It feels so good outside i don't want to be even near that creepy apartment.{w} I head towards elevator."
    "..."
    nvl clear
    $ renpy.music.set_volume(0.5, delay=1.0)
    "When i exit the building, i feel great.{w} Fresh spring air is filling my lungs.{w} I hear wailing of the siren somewhere in the distance, but even such disturbing sound cannot break my positive spirit."
    "I walk along the street in direction of the park i've seen earlier from the height of eleventh floor.{w} For some reason most of the passer-by i meet have anxious or even plain frightened expressions on their faces.{w} I smile at them, but they only cast their eyes down to avoid my gaze."
    "So dull and grey, all those people.{w} If they can't enjoy beautiful spring day, what can they admire?"
    nvl clear
    scene bg park at bg
    with dissolve
    "Thinking like that i pass through the park gate.{w} Small flock of pigeons flies out of the ground as i approach them."
    "Bright sun light is reflected in the drops of water on the little green leaves.{w} That's odd.{w} It's like there was a rain, but all the pavement was pretty dry.{w} Perhaps it rained for a bit and then hot sun dried most of water in the city, but here in the woods it still can hide."
    "My thoughts are interrupted by now quite loud sirens behind my back.{w} It gets quite annoying, so i walk faster to escape from unpleasant sound."
    "But then.."
    nvl clear
    "\"Hey you! Don't move! Drop your weapon!\""
    "Somebody behind me calls out in a loud commanding voice.{w} There's also a sound of many people running in this direction."
    "I freeze."
    "..."
    nvl clear
    scene bg park blur at bg
    with dissolve
    $ renpy.music.set_volume(1.0, delay=4.0)
    play music "sfx/85670__cgeffex__heartbeat.mp3" fadeout 4.0 fadein 4.0
    "White.{w} Gust of wind bends the trees and direct sun rays are suddenly feeling my vision again."
    "White.{w} It makes me remember.{w} It makes me realize what is happening here."
    "I put my hand in the pocket and slowly turn around.{w} I know what i am doing.{w} I know what's going to happen next.{w} I have no regrets."
    "With these thoughts, not paying any attention to a bunch of policemen in front of me, i pull out a small metallic object and aim directly forward."
    "All i can see now is my gun, so clean and glossy, reflecting bright light."
    "I don't hear anything, but i understand they are going to start shooting any moment.{w} I still manage to turn safety off and pull the trigger."
    "Recoil is harder than i expected, but then there's no time to be bothered by it."
    "I don't quite feel pain, but i realize being shot."
    "I am going to disappear now.{w} My vision blurs until all the world becomes white."
    nvl clear
    scene white
    with dissolve
    ":: white ending ::"
    $ persistent.endings.add('white')
    return
