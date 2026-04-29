init python:
    import random
    bgm_tracks = [
        "Everything Everything.mp3",
        "Slingshot.mp3",
        "Pox.mp3",
    ]

define s  = Character("[player_name]",   color="#c8e6c9")
define b  = Character("Beetle",  color="#8d6e63")
define g  = Character("Gary",    color="#a5d6a7")
define c  = Character("Cecil",   color="#ce93d8")
define n  = Character("Narrator",color="#ffffff")

default persistent.ending1_seen    = False
default persistent.ending2_seen    = False
default persistent.ending3_seen    = False
default persistent.secret_unlocked = False

image snail  = "snail.png"
image beetle = "beetle.png"
image gary   = "gary.png"
image cecil = im.Scale("cecil.png", 800, 1200)

image bg garden       = im.Scale("garden.jpg", 1920, 1080)
image bg garden path  = im.Scale("gardenpath.jpg", 1920, 1080)
image bg garden log   = im.Scale("gardenlog.png", 1920, 1080)
image bg garden deep  = im.Scale("gardendeep.jpg", 1920, 1080)

define beetle_trust   = 0   # sanil trust in beetle oooh yes
define gary_helped    = False
define cecil_secret   = False

label start:

    scene bg garden
    $ selected_bgm = random.choice(bgm_tracks)
    $ renpy.music.play("audio/" + selected_bgm, loop=True, fadein=1.0)

    $ beetle_trust = 0
    $ gary_helped  = False
    $ cecil_secret = False
    "Before we begin, what's yer name?"
    $ player_name = renpy.input("whats yer name?", length=67)
    $ player_name = player_name.strip() or "snail"
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
    "The atmosphere was just trying its best."

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
    "Also like compost, which is a strange combination."

    b "okay so."
    b "definite evidence of dragging."
    s "yes."
    b "and there's my pine needle from before."
    s "and look."

    "The snail points at something with great gravity."
    "It is a very small button."

    b "..."
    b "is that your button."
    s "that is MY button."
    s "from my diary bag."
    b "..."
    b "case closed basically."
    s "case closed."

    $ beetle_trust += 1

    "A rustling in the pine needles."
    "They both freeze."

    show cecil at right with moveinright

    c "oh."
    c "..."
    c "hello."

    s "Cecil."
    c "Snail."
    c "and... beetle."
    b "hi."
    c "..."
    c "I can explain."

    jump scene4_confront_midscene


label scene4_confront_direct:
    jump scene4_confront_walk


label scene4_confront_walk:

    scene bg garden deep

    show snail at left
    show beetle at right

    "The far side of the garden is quieter."
    "The pine trees make everything smell sharp and clean."
    "It's actually quite nice over here."
    "The snail makes a mental note about this."

    b "so what's the approach."
    s "we knock."
    b "on what."
    s "Cecil has a log."
    s "everyone has a log."
    b "I don't have a log."
    s "you should get a log."
    b "is this going to be a whole thing."
    s "no."
    s "here we are."

    show cecil at center with moveinright

    c "oh."
    c "visitors."
    c "how... unexpected."
    s "hello Cecil."
    c "Snail."
    c "and you brought a beetle."
    b "Beetle."
    c "how creative."
    b "says Cecil the centipede."
    c "touché."

    jump scene4_confront_main


label scene4_confront_midscene:

    "Cecil is already here."
    "This is either very convenient or very suspicious."
    "Probably both."

    jump scene4_confront_main


label scene4_confront_main:

    s "Cecil."
    s "where is my compost pile."
    c "I don't know what you're talking about."
    s "Cecil."
    c "..."
    s "Gary told us."
    c "Gary is a coward and a gossip."
    b "so you know Gary."
    c "everyone knows Gary."
    b "you didn't deny the gossip part."
    c "..."

    menu:
        "Stay calm. Give Cecil a chance to explain.":
            $ beetle_trust += 1
            jump scene5_calm
        "Tell Cecil about the diary specifically.":
            jump scene5_diary
        "Ask Cecil why. Not what happened - why.":
            $ cecil_secret = True
            jump scene5_why
        "Let the beetle take the lead on this one.":
            jump scene5_beetle_leads


label scene5_calm:

    s "Cecil."
    s "I'm not angry."
    c "..."
    s "I'm confused."
    s "and I would like my things back."
    s "but I'm not angry."
    c "..."
    c "you should be angry."
    s "probably."
    s "but I'm a snail."
    s "anger takes a lot of energy."
    c "..."

    "Cecil looks at its feet."
    "All of them."
    "This takes a moment."

    c "I took it."
    c "I needed the compost."
    c "for my side of the garden."
    c "nothing grows over here."
    s "..."
    s "Cecil."
    s "you could have asked."
    c "..."
    c "I didn't think you'd say yes."
    s "why not."
    c "..."

    jump scene5_the_truth


label scene5_diary:

    b "there was a diary in there."
    c "..."
    b "a personal diary."
    b "with private thoughts in it."
    c "I didn't read it."
    b "you have it though."
    c "..."
    c "I have it."
    c "I didn't read it."
    c "I found it when I was going through the compost."
    c "I put it aside."
    c "I was going to return it."
    s "..."
    s "Cecil."
    c "I'm not a monster."
    s "I know."
    c "I just needed the compost."
    c "nothing grows here."
    c "I thought maybe if I had better soil..."
    s "..."

    jump scene5_the_truth


label scene5_why:

    s "Cecil."
    s "why."
    c "..."
    c "what do you mean why."
    s "you could have just asked."
    s "you know where I live."
    s "you pass my rock every day."
    c "..."
    c "you noticed that."
    s "I notice things."
    s "I'm a snail."
    s "I have a lot of time to notice things."
    c "..."

    "Cecil is quiet for a long time."

    c "I didn't think you'd want to talk to me."
    s "why not."
    c "..."
    c "I'm a lot."
    c "I have a hundred legs."
    c "I trip over things."
    c "I'm not very..."
    c "easy."
    s "..."
    s "Cecil."
    c "yeah."
    s "I have been staring at the same rock for three years."
    s "I am also not very easy."
    c "..."
    c "huh."

    $ beetle_trust += 1
    $ cecil_secret = True
    jump scene5_the_truth


label scene5_beetle_leads:

    "The snail steps back."
    "The beetle steps forward."
    "The beetle seems surprised by this."
    "But also rises to the occasion."

    b "okay Cecil."
    b "look."
    b "we're not here to cause trouble."
    b "we just want to understand what happened."
    b "and get the stuff back."
    b "and then maybe everyone can just... move on."
    c "..."
    c "that simple?"
    b "that simple."
    c "..."

    "Cecil looks at the beetle."
    "Then at the snail."
    "The snail nods very slightly."

    c "I needed the compost."
    c "for my garden."
    c "nothing grows on this side of the fence."

    b "..."
    b "you have a garden?"
    c "I'm trying to."
    c "it's not going very well."

    $ beetle_trust += 2
    jump scene5_the_truth


label scene5_the_truth:

    "A pause settles over everything."
    "The pine trees are very still."

    b "wait."
    b "so you took an entire compost pile."
    b "to try to grow a garden."
    c "yes."
    b "..."
    b "over here."
    b "where it's very shady."
    c "..."
    c "yes."
    b "Cecil that's not going to work."
    c "I know that NOW."
    s "what were you trying to grow."
    c "..."
    c "flowers."
    s "..."
    b "..."
    c "I just thought."
    c "if there were flowers here."
    c "it would be nicer."
    c "over here."
    s "Cecil."
    c "yeah."
    s "why do you want it to be nicer over here."

    "Cecil looks at its feet again."

    c "..."
    c "it gets lonely."
    c "over here."
    c "nobody really comes to this side."

    "A very long pause."

    if cecil_secret == True:
        "The snail does not look surprised."
    
    if beetle_trust >= 4:
        "The beetle sits down on a pine needle, thinking."
        "The snail watches the beetle."
        "Something is happening in the beetle's expression."
        "The snail files this away."

    menu:
        "Tell Cecil they can just have some compost. Properly this time.":
            jump ending1_justice
        "Ask Cecil if they want company. The real question.":
            jump ending2_everyone_lonely
        "Look at the beetle. Really look at them.":
            jump ending3_beetle
        
        "Ask Cecil to show you the garden they're trying to grow.":
            jump ending2_everyone_lonely



label ending1_justice:

    s "Cecil."
    s "give it back."
    s "all of it."
    c "..."
    c "fine."

    "Cecil produces the diary."
    "And the button."
    "And the pebble."
    "And the dried moss."
    "And approximately forty percent of the compost pile."
    "The beetle makes seven trips."

    b "okay I think that's everything."
    s "..."
    s "this is more than I started with."
    c "I added to it."
    c "I felt bad."
    s "...Cecil."
    c "what."
    s "did you want some of the compost."
    s "you could have just asked."
    c "..."
    b "yeah we're pretty chill about compost."
    c "I didn't know that."
    s "now you know."

    "Cecil gets some compost."
    "A real amount. A generous amount."
    "The snail helps Cecil figure out which spot in the garden actually gets enough light."
    "It is not this spot."
    "They relocate the whole operation to a better patch."
    "The beetle helps dig, because the beetle is like that apparently."
    "By the end of the afternoon something resembling a garden bed exists."
    "It is small and the soil is lumpy."
    "It is a start."

    c "..."
    c "thank you."
    s "don't mention it."
    b "mention it a little."
    s "mention it a normal amount."
    c "..."
    c "thank you a normal amount."

    "The snail gets their diary back."
    "The beetle gets nothing material but feels very good about the whole situation."
    "The rock is still out there."
    "Being a rock."
    "Everything is fine."

    "THE END."
    "ENDING 1: JUSTICE IS SERVED (QUESTIONABLY)"
    "The garden is slightly better than it was this morning."
    "That's fun, lol"
    $ persistent.ending1_seen = True
    jump check_secret_unlock


label ending2_everyone_lonely:

    s "Cecil."
    s "do you want company."
    c "..."
    c "what?"
    s "over here."
    s "on this side of the garden."
    s "do you want someone to come over sometimes."
    c "..."
    c "I."
    c "yes."
    c "but I didn't think anyone would want to."
    s "why not."
    c "nobody ever comes here."
    b "because nobody knew it was here."
    c "..."
    b "I didn't know this side of the garden existed."
    b "I've been flying over it for a whole season."
    b "I just never came down."
    c "..."
    c "oh."
    b "yeah."

    "A very long pause."
    "The pine trees drop a few needles, gently."

    s "Cecil."
    s "return my things."
    s "and we'll come back tomorrow."
    c "..."
    c "why."
    s "because you wanted flowers and you have bad soil placement."
    s "and I know where the good light is."
    s "and the beetle can dig faster than either of us."
    b "I do dig very fast."
    c "..."
    c "just like that."
    s "just like that."

    "Cecil returns everything."
    "All of it, including the button, which Cecil had polished."
    "The snail doesn't mention this."
    "But notes it."

    "They come back the next day."
    "And the day after that."
    "The garden on the shady side of the fence is relocated to a better spot."
    "Eventually something actually grows."
    "It's not much."
    "But Cecil tends to it every morning."
    "And sometimes there are visitors."

    "THE END."
    "ENDING 2: NOBODY WAS OKAY AND THAT WAS THE THING THEY HAD IN COMMON LMAO"
    "the flowers are doing fine, actually."

    $ persistent.ending2_seen = True
    jump check_secret_unlock


label ending3_beetle:

    "The snail looks at the beetle."
    "Really looks."
    "The beetle is looking at Cecil."
    "The beetle's expression is very complicated."
    "Something is clicking into place."

    s "beetle."
    b "yeah."
    s "is there something you want to say."
    b "..."
    b "no."
    s "beetle."
    b "..."

    "Cecil looks between them."
    "Cecil decides to go check on the compost pile situation."
    "Cecil is perceptive like that."

    hide cecil with moveoutright

    "They are alone."

    b "..."
    s "."
    b "okay."
    b "okay so."
    b "there wasn't really an emergency."
    s "I know."
    b "the compost pile is gone that part is true."
    s "I know."
    b "but I."
    b "I fly past your rock a lot."
    b "like. a lot."
    b "and you're always just."
    b "looking at stuff."
    b "and you seem really into it."
    b "and I just."
    b "I wasn't into anything."
    b "and I thought if I said there was an emergency you'd come with me."
    b "and we'd just."
    b "walk around."
    b "and look at stuff."
    b "together."

    "A very long silence."

    s "..."
    b "I'm sorry."
    s "..."
    s "beetle."
    b "yeah."
    s "you can just ask."
    b "..."
    b "really."
    s "I would say yes."
    b "..."
    b "how do you know."
    s "because you walked the whole way here."
    s "even though you can fly."
    b "..."
    b "I."
    b "yeah."

    "The beetle looks at the ground."
    "The snail looks at the beetle."
    "A pine needle falls between them."

    s "that was kind."
    b "I'm a kind beetle."
    s "I know."

    "Cecil comes back."
    "Cecil has retrieved the diary and the button and the pebble and the moss."
    "Cecil holds them out, all of them, without being asked."
    "Cecil says nothing."
    "The snail takes them."

    s "thank you Cecil."
    c "..."
    c "sorry about the compost pile."
    s "we'll sort it out."
    c "okay."

    "And somehow they all end up sitting on the pine needle side of the garden."
    "As the sun gets lower."
    "Nobody planned this."
    "It just happened."

    b "hey."
    s "yeah."
    b "same time tomorrow?"
    s "..."
    s "I'll be by my rock."
    b "okay."
    s "you know where it is."
    b "I do."
    s "good."

    "The fireflies come out."
    "The snail watches them."
    "The beetle watches the snail watch them."
    "Cecil watches both of them and says nothing and this is its own kind of happiness."

    "THE END."
    "ENDING 3: BEETLE IS JS A LIL GUY"
    "and honestly same."
    "thanks for playing critterbeats :)"

    $ persistent.ending3_seen = True
    jump check_secret_unlock

label check_secret_unlock:

    if persistent.ending1_seen and persistent.ending2_seen and persistent.ending3_seen and not persistent.secret_unlocked:
        $ persistent.secret_unlocked = True
        "..."
        "hey."
        "you're still here."
        "you've seen all of it, haven't you."
        "every ending. every choice."
        "you watched the snail stare at rocks."
        "you watched the beetle walk when it could fly."
        "you watched Cecil polish a button for someone who didn't know."
        "..."
        "there's one more thing."
        "the rock the snail was staring at at the beginning?"
        "the beetle put it there."
        "three weeks ago."
        "thought it was a good rock."
        "thought maybe the snail would like it."
        "left it and flew away before anyone could see."
        "..."
        "that's all. that's the secret."
        "go outside. notice something."
        "SECRET ENDING: THE ROCK"
        "you found it :)"
    else:
        if not persistent.ending1_seen or not persistent.ending2_seen or not persistent.ending3_seen:
            "..."
            "there might be more to find."
            "just saying."

    return

