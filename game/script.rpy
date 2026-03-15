
define s  = Character("Snail",   color="#c8e6c9")
define b  = Character("Beetle",  color="#8d6e63")
define g  = Character("Gary",    color="#a5d6a7")
define c  = Character("Cecil",   color="#ce93d8")
define n  = Character("Narrator",color="#ffffff")

image snail  = "snail.png"
image beetle = "beetle.png"
image gary   = "gary.png"
image cecil  = "cecil.png"

define beetle_trust   = 0   # how much snail trusts beetle
define gary_helped    = False
define cecil_secret   = False


label start:

    scene bg garden

    $ beetle_trust = 0
    $ gary_helped  = False
    $ cecil_secret = False

    "It's a perfectly normal Tuesday in the garden."
    "The sun is shining. The dirt is dirty. Life is good."

    show snail at center

    "A snail is minding their own business."
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
    s "more urgent than this rock."
    b "THE ROCK WILL STILL BE HERE LATER."
    s "you don't KNOW that."
    b "what do you think is going to happen to the rock."
    s "anything could happen."
    s "it's a dangerous world."
    b "for the rock."
    s "for ANYONE."

    "The beetle stares at the snail."
    "The snail stares at the rock."
    "Four seconds pass."

    b "okay what if I told you there's a BIGGER rock."
    s "..."
    s "how much bigger."
    b "like. so big."
    s "...define 'so big.'"
    b "I don't know man I didn't measure it I'm a beetle."

    menu:
        "Go see the bigger rock.":
            $ beetle_trust += 1
            jump scene2_walk
        "Stay. The original rock deserves loyalty.":
            jump scene1_loyal
        "Ask the beetle what they actually need first.":
            $ beetle_trust += 1
            jump scene1_askfirst



label scene1_loyal:

    "You stay."
    "The beetle sighs."
    "Then sits down next to you."
    "..."
    "..."

    b "okay I see it now."
    s "right?"
    b "it's a pretty good rock."
    s "thank you."
    b "very... sturdy looking."
    s "extremely sturdy."
    b "classic shape."
    s "timeless."

    "Another pause."

    b "okay but I do still need your help."
    s "...with what."
    b "something happened."
    s "to the rock."
    b "NOT to the rock."
    s "okay. what then."

    jump scene1_emergency

label scene1_askfirst:

    s "what do you actually need."
    b "what do you mean."
    s "you said you needed my help."
    s "you didn't say anything about what kind of help."
    b "I was getting to it."
    s "you led with the rock."
    b "the rock was an INCENTIVE."
    s "an incentive to do what."
    b "to COME WITH ME so I could EXPLAIN."
    s "you could explain here."
    b "..."
    b "fair."

    jump scene1_emergency



label scene1_emergency:

    b "so."
    b "you know the compost pile."
    s "yes."
    b "by the big log."
    s "yes."
    b "it's gone."
    s "..."
    s "define gone."
    b "not there."
    s "where did it go."
    b "THAT'S WHAT I'M SAYING."
    b "SOMEONE TOOK IT."
    s "..."
    s "..."

    "A single raindrop falls dramatically."
    "Then stops, because it isn't actually raining."
    "The atmosphere was just trying it s   b"eAslts.o" like compost, which is a strang

    s "THE COMPOST PILE."
    b "I KNOW."
    s "THAT'S WHERE I KEEP MY THINGS."
    b "I KNOW."
    s "WHO STEALS A COMPOST PILE."
    b "THAT'S WHAT I'M SAYING."

    menu:
        "Go investigate immediately. Justice cannot wait.":
            $ beetle_trust += 1
            jump scene2_walk
        "Ask what was actually in the compost pile first.":
            jump scene1_whatsinit
        "Ask the beetle why they care so much about your compost pile.":
            jump scene1_whybeetle


label scene1_whatsinit:

    b "wait what did you even keep in there."
    s "things."
    b "what THINGS."
    s "my things."
    b "okay but specifically."
    s "..."
    s "a pebble."
    s "some dried moss."
    s "a button I found."
    s "and my diary."
    b "..."
    b "you have a diary."
    s "everyone has a diary."
    b "I don't have a diary."
    s "you should get a diary."
    b "THAT'S NOT THE POINT."
    b "someone has your diary."
    s "yes."
    b "and you're calm about this."
    s "I am a snail."
    s "I am always calm."
    s "internally I am screaming."
    b "okay."
    b "okay we are getting that diary back."
    b "nobody should read your diary."
    b "that is like the number one rule."
    s "what's the number two rule."
    b "I only follow the one."

    $ beetle_trust += 1
    jump scene2_walk


label scene1_whybeetle:

    s "why do you care so much."
    b "..."
    b "what do you mean."
    s "it's my compost pile."
    s "you didn't have to come find me."
    b "I... was just passing by."
    b "and I noticed."
    b "and I thought you should know."
    s "..."
    s "that was kind of you."
    b "I'm a kind beetle."
    s "I didn't say you weren't."
    b "okay."

    "A pause."

    s "...thank you."
    b "don't mention it."
    s "..."
    s "beetle."
    b "yeah."
    s "I'm going to mention it."
    b "okay."

    $ beetle_trust += 2
    jump scene2_walk


label scene2_walk:

    scene bg garden path

    show snail at left
    show beetle at right

    "They set off toward the compost pile's last known location."
    "The beetle walks, even though they could fly."
    "The snail notices but doesn't say anything."
    "The snail files this information away."

    b "so do you have any idea who could have done this."
    s "several."
    b "really."
    s "this garden has a lot of characters."
    b "like who."
    s "Cecil."
    b "the centipede?"
    s "Cecil has always had opinions about my compost pile."
    b "what kind of opinions."
    s "unwelcome ones."

    "A pause."

    b "who else."
    s "the ants."
    b "which ants."
    s "all of them."
    s "ants are very organized."
    s "organized creatures always want more resources."
    b "that's a bit much."
    s "I contain multitudes."

    menu:
        "Check the compost pile's old location for clues.":
            jump scene2_clues
        "Go find Gary first. Gary knows everything.":
            jump scene2_gary
        "Ask the beetle what they saw exactly.":
            $ beetle_trust += 1
            jump scene2_beetlesaw


label scene2_clues:

    scene bg garden log

    "They make their way to where the compost pile used to be."
    "There is a very conspicuous empty space where it was."
    "The dirt is disturbed."

    s "..."
    b "yeah."
    s "something was definitely dragged."
    b "there are tracks."
    s "a lot of legs."
    b "how many."
    s "I'm going to say more than four."
    b "..."
    b "Cecil."
    s "or the ants working in formation."
    b "can ants do that."
    s "ants can do anything."
    s "that's what makes them unsettling."

    "The beetle finds something near the tracks."

    b "hey."
    b "pine needle."
    s "..."
    s "Cecil."
    b "yeah."
    s "okay."
    s "let's go find Gary first."
    b "why Gary first."
    s "Gary sees everything."
    s "Gary just never says anything unless you ask."
    b "that seems like an inefficient system."
    s "Gary is a worm."
    s "Gary contains multitudes."

    jump scene3_gary_visit


label scene2_gary:

    s "we need to find Gary."
    b "who's Gary."
    s "the worm."
    s "lives under the big log."
    b "I thought the worm was named Dave."
    s "that's a different worm."
    b "how many worms are there."
    s "this is a garden."
    b "fair point."

    jump scene3_gary_visit


label scene2_beetlesaw:

    s "what did you see exactly."
    b "I was flying past."
    b "and I looked down."
    b "and where the compost pile was."
    b "there was just. not a compost pile."
    s "and you saw no one."
    b "I saw a pine needle."
    s "a pine needle."
    b "yeah."
    s "..."
    s "Cecil."
    b "you keep saying that."
    s "Cecil lives near the pine trees."
    s "Cecil has always had opinions about my compost pile."
    b "should we just go confront Cecil."
    s "we should find Gary first."
    b "who's Gary."
    s "the worm. under the big log."
    s "Gary sees everything."
    b "then why didn't Gary stop it."
    s "because Gary is a worm."
    s "Gary is a witness, not a hero."
    b "okay."

    jump scene3_gary_visit


label scene3_gary_visit:

    scene bg garden log

    show gary at center

    "Gary is under the log."
    "Gary is always under the log."
    "Gary looks like he was hoping nobody would come today."

    g "oh."
    g "oh no."
    g "you found me."

    s "Gary."
    g "I didn't do anything."
    s "I didn't say you did."
    g "I'm just saying. proactively."
    b "Gary we just want to know what you saw."
    g "I saw a lot of things."
    s "about the compost pile."
    g "...specifically?"
    s "specifically."
    g "..."

    menu:
        "Be patient. Let Gary take his time.":
            $ gary_helped = True
            $ beetle_trust += 1
            jump scene3_gary_patient
        "Tell Gary it's urgent. The diary is at stake.":
            jump scene3_gary_diary
        "Offer Gary something in return for information.":
            $ gary_helped = True
            jump scene3_gary_bribe


label scene3_gary_patient:

    s "take your time Gary."
    g "..."
    g "really?"
    s "really."
    g "nobody ever says that."
    s "I'm a snail."
    s "I understand taking your time."
    g "..."
    g "okay."

    "Gary visibly relaxes."
    "The beetle resists the urge to hurry things along."
    "The snail notices and files this away too."

    g "I was minding my business."
    g "which I do."
    g "I am a very minds-his-business type of worm."
    g "and I saw something being dragged."
    g "toward the pine trees."
    g "it smelled like compost."
    g "and pine needles."
    g "and whoever was doing it had a lot of legs."
    g "more than four."
    g "a lot more."

    b "Cecil."
    g "I didn't say that."
    s "you described Cecil."
    g "I described a lot of legs and pine needles."
    g "I'm a witness, not an accuser."
    s "fair enough."
    g "..."
    g "it was probably Cecil though."

    jump scene3_gary_end


label scene3_gary_diary:

    b "Gary someone stole a diary."
    g "oh no."
    g "whose diary."
    s "mine."
    g "oh."
    g "oh that's bad."
    g "I would hate it if someone read my diary."
    b "you have a diary?"
    g "everyone has a diary."
    b "WHY DOES EVERYONE HAVE A DIARY."
    s "beetle."
    b "sorry."
    g "okay."
    g "I saw something dragged toward the pine trees."
    g "lot of legs."
    g "smelled like pine needles."
    g "I didn't see a face."
    g "but."
    g "I did see a very familiar very long shadow."
    s "Cecil."
    g "I didn't say that."
    s "but it was."
    g "..."
    g "probably."

    jump scene3_gary_end


label scene3_gary_bribe:

    s "Gary."
    s "I will owe you a favor."
    g "..."
    g "what kind of favor."
    s "I have some very good dried moss."
    g "..."
    g "what kind of moss."
    s "the good kind."
    g "..."
    g "okay."

    "Gary tells them everything."
    "Gary also asks for the moss upfront."
    "The snail respects this negotiation tactic."

    g "lot of legs. pine needle smell. dragged toward the far fence."
    g "that's all I know."
    g "and I want the moss."
    s "you'll get the moss."
    g "good."
    g "I'm going back under my log."

    jump scene3_gary_end


label scene3_gary_end:

    hide gary

    b "okay so. Cecil."
    s "Cecil."
    b "what do we know about Cecil."
    s "centipede."
    s "lives by the far fence near the pine trees."
    s "has expressed opinions about my compost pile before."
    s "specifically has called it 'an eyesore.'"
    b "rude."
    s "I thought so."
    b "okay."
    b "do we have a plan."

    menu:
        "Go confront Cecil directly. No plan needed.":
            jump scene4_confront_direct
        "Spend some time making a proper plan first.":
            jump scene4_plan
        "Check the pine tree area for more evidence before confronting anyone.":
            jump scene4_evidence



label scene4_plan:

    scene bg garden path

    show snail at left
    show beetle at right

    "They find a sunny patch and sit down to think."
    "The beetle paces."
    "The snail watches the beetle pace."
    "This is very dizzying at beetle speed."

    s "stop."
    b "I think better when I move."
    s "I think better when things aren't moving."
    b "opposite problem."
    s "yes."

    "The beetle sits down."

    b "okay."
    b "so we go to Cecil."
    b "and we say..."
    s "we know."
    b "just like that."
    s "just like that."
    b "what if Cecil denies it."
    s "Cecil won't deny it."
    b "how do you know."
    s "Cecil is many things."
    s "a liar is not one of them."
    b "what IS Cecil."
    s "..."
    s "complicated."
    b "..."
    b "do you know Cecil well."
    s "we grew up in the same garden."
    b "oh."
    s "Cecil was always a bit..."
    s "..."
    s "alone."
    b "..."

    "A pause."
    "The beetle looks at the snail."
    "The snail looks at a nearby rock."
    "It's a good rock."

    b "okay."
    b "we go talk to Cecil."
    b "and we're... nice about it."
    s "..."
    s "yes."
    s "we're nice about it."

    $ beetle_trust += 1
    jump scene4_confront_walk


label scene4_evidence:

    scene bg garden deep

    show snail at left
    show beetle at right

    "They make their way to the pine tree area."
    "It does smell like pine needles."
 

    