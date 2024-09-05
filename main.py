import os
import random
import subprocess

def play_random_sound():

    #available sounds
    sound_files = [
        'sounds/Wololo.mp3',
        'sounds / spellCast1.mp3',
        'sounds/Magic Ambiance.mp3'
    ]

    random_index = random.randint(0, len(sound_files) -1)

    random_sound = sound_files[random_index]

    subprocess.Popen(['mpg123', random_sound])




play_random_sound()
