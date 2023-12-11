# The script of the game goes in this file.

# help

translate japanese python:
    gui.text_font = "SourceHanSansLite.ttf"
    gui.name_text_font = "SourceHanSansLite.ttf"
    gui.interface_text_font = "SourceHanSansLite.ttf"

translate japanese style default:
    language "japanese-strict"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = _(adv_narrator)

define n = Character(_("Neko-san"), color = "#f60")
define s = Character(_("Sakana-han"), color = "#f6f")

# Adds a 'jumper' transform. Use 'show ... at jumper' to make the char jump.

transform jumper:
    ease .06 yoffset 24
    ease .06 yoffset -24
    ease .05 yoffset 20
    ease .05 yoffset -20
    ease .04 yoffset 16
    ease .04 yoffset -16
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0 

# Adds a 'jiggle' transform. Use 'show ... at jumper' to make the char wiggle.

transform jiggle:
    ease .06 xoffset 24
    ease .06 xoffset -24
    ease .05 xoffset 20
    ease .05 xoffset -20
    ease .04 xoffset 16
    ease .04 xoffset -16
    ease .03 xoffset 12
    ease .03 xoffset -12
    ease .02 xoffset 8
    ease .02 xoffset -8
    ease .01 xoffset 4
    ease .01 xoffset -4
    ease .01 xoffset 0 

# Zooms into slightly too small background
image bg village mountain:
    "images/bg_village_mountain.png"
    zoom 1.15

# Zooms out of the giant images
image cat idle:
    "images/cat_idle.png"
    zoom 0.5
image cat alert:
    "images/cat_alert.png"
    zoom 0.5
image cat batting:
    "images/cat_batting.png"
    zoom 0.5
image cat shy:
    "images/cat_shy.png"
    zoom 0.5
image cat earnest:
    "images/cat_earnest.png"
    zoom 0.5
image fish faded:
    "images/fish_faded.png"
    zoom 0.5
image fish tiltinghead:
    "images/fish_tiltinghead.png"
    zoom 0.5
image fish idle:
    "images/fish_idle.png"
    zoom 0.5
image fish surprised:
    "images/fish_surprised.png"
    zoom 0.5
image fish laughing:
    "images/fish_laughing.png"
    zoom 0.5

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default.

    scene bg village mountain

    # Start describing the narration of a cat "trying" to catch a fish.

    "Once upon a time, a village sat on a mountain overlooking the sea."
    "In the village was a normal cat."

    show cat batting at left

    "Long-tailed Neko-san was cute."
    "Neko-san saw a fish and tried to catch it every day."

    show fish faded at right
    show fish faded at jiggle

    "The mythical fish, Sakana-han, became curious."

    show fish idle at center with move

#    nvl clear

    show cat idle

    "Sakana-han addressed Neko-san,"

#    nvl clear

    show cat alert at jumper
    show fish tiltinghead

    s "Why, a cat that cannot catch a fish."

    show cat idle

    s "This very place I await; do I not, Neko-chan?"
    s "Something ought be the matter."
    s "Are you quite alright?"

    show cat shy

    "The cat contemplated."

#    nvl clear

    n "Well, I'm a scaredy-cat, aren't I?"
    
    s "And why would that be?"

    show cat batting

    n "I'm scared that, were I to catch you, I would be sad."

    show fish surprised at jumper

    s "Whyever so, Neko-chan?"

    show fish idle

    show cat shy

    n "I..."

    show cat earnest at jiggle

    n "I want to be friends!"

    show fish surprised at jumper

    s "Interesting, that is."

    show fish laughing

    "Sakana-han chortled at the idea."

#    nvl clear

    s "Very well. Let us proceed!"

    "And so, the pair became friends."

    "... the end?"

    # This ends the game.

    return
