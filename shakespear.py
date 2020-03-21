#!/usr/bin/python
#project files and license available at https://github.com/phydeauxarf/shakespeare

import random
from os import system, name
from time import sleep
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from inky import InkyPHAT

#if you are using the Yellow, Black, White version of the InkypHAT the bolow is what you want.
#if you are using the Red, Black, White or Black, White version you'll need to modify approproately
inky_display = InkyPHAT("yellow")

inky_display.set_border(inky_display.WHITE)
font = ImageFont.truetype(FredokaOne, 17)
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

#wordlist obtained from https://www.sadanduseless.com/insult-generator-funny/
column1 = ["artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish", "dankish", "dissembling", "droning", "errant", "fawning", "fobbing", "froward", "forthy", "gleeking", "goatish", "gorbellied", "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "mammering", "mangled", "mewling", "paunchy", "pribbling", "puking", "puny", "qualling", "rank", "reeky", "roguish", "ruttish", "saucy", "spleeny", "spongy", "surly", "tottering", "unmuzzeled", "vain", "venomed", "villainous", "warped", "wayward", "weedy", "yeasty"]
column2 = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-gripped", "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle-headed", "ill-breading", "ill-nurtured", "knotty-pated", "milk-livered", "motley-minded","onion-eyed", "plume-plucked", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne", "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted", "unchin-snouted", "weather-bitten"]
column3 = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "deberry", "flap-dragon", "flax-wench", "flirt-gill", "foot-licker", "fusilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "joithead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow", "mscreant", "moldwap", "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet", "varlot", "vassal", "whey-face", "wagtail"]

#lets randmoize this sucker, push up our image+text  and get into a groove!
while img:
   message1 = ("Thou " + random.choice(column1))
   message2 = random.choice(column2)
   message3 = random.choice(column3)

   img = Image.open("/home/pi/sp.png")
   draw = ImageDraw.Draw(img)

   x=0
   y=0
   draw.text((x, y), message1, inky_display.BLACK, font)
   draw.text((x, y+40), message2, inky_display.BLACK, font)
   draw.text((x, y+80), message3, inky_display.BLACK, font)
   inky_display.set_image(img)
   inky_display.show()
   sleep(30)
