import random
import re

Names = ['Stephen', 'Daan', 'Kees', 'Tim']

Beroepen = ['leraar', 'advocaat', 'putjesschepper']

def get_name():
    naam = random.choice(Names)
    return naam

print("Hoi, i am {naam}".format(naam=get_name()))
