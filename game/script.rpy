define s = Character("Snail", color="#c8e6c9")
define b = Character("Beetle", color="#8d6e63")

label start:
scene bg garden

    "It's a perfectly normal Tuesday in the garden."
    "The sun is shining. The dirt is dirty. Life is good."

    show slug at center

    "A snail is minding their own business, doing snail things."
    "Specifically, they are staring at a rock."
    "They have been staring at this rock for 45 minutes."

    s "..."
    s "..."
    s "incredible."

    "A beetle lands nearby with the grace of a garbage truck."

    show beetle at right with moveinright

    b "HEY."

    s "I am busy."

    b "you have been staring at a rock."

    s "I KNOW what I have been doing."

    b "okay but I need your help."

    s "..."
    s "is it urgent."

    b "extremely."

    s "..."
    s "more urgent than this rock?"

    b "THE ROCK WILL STILL BE HERE LATER."

    s "you don't KNOW that."

    "The beetle stares at the snail."
    "The snail stares at the rock."
    "Three seconds pass."

    b "okay what if I told you there's a BIGGER rock over there."

    s "..."

    s "how much bigger."

    b "like. so big."

    s "...define 'so big.'"

    b "I don't know man I didn't measure it I'm a beetle."

    menu:
        "Go see the bigger rock":
            jump bigger_rock
        "Stay. The original rock deserves loyalty.":
            jump loyal_to_rock

label bigger_rock:
    s "...fine. but if this rock is disappointing I am going home."
    b "it won't be disappointing trust me."
    s "I have never trusted anyone in my life."
    b "okay."
    s "but I will try."
    "They begin the journey."
    "It takes a very long time."
    "The beetle could fly but walks anyway, out of solidarity."
    "This is the beginning of something."
    "Nobody knows what."
    return

label loyal_to_rock:
    "You stay."
    "The beetle sits down next to you."
    "..."
    "..."
    b "okay I see it now."
    s "right?"
    b "it's a pretty good rock."
    s "thank you."
    "This is also the beginning of something."
    "It just started slower."
    return


    