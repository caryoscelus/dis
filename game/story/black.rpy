label black_branch:
    nvl clear
    "I am tired.{w} I don't want to go anywhere.{w} I sit on the floor and make myself comfortable."
    "..."
    scene black
    nvl clear
    "Black.{w} Colour of nothingness, emptiness.{w} Colour of death? No, that's not it.{w} Death is only a process of dying and thus have other colours.."
    "Black.{w} Colour of calmness."
    "I still can feel myself sitting on corridor floor, but as minutes pass that feeling becomes more and more transparent."
    "Soon there's nothing but black.{w} Perhaps i closed my eyes at some moment, but does it matter now?{w} I don't even feel eyes as long as i don't think about them."
    "And who's that \"i\" thinking here?{w} No answer emerges in the darkness and weird question slowly fades away."
    "It's good to feel nothing.{w} To feel completely black."
    nvl clear
    stop music
    scene black
    with fade
    ":: black end ::"
    $ persistent.endings.add('black')
    return
