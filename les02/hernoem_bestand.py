from distutils.file_util import move_file
import os
import time

bestandsnaam = "demobestand.txt"
huidigemap = os.getcwd()
volledige_pad = os.path.join(huidigemap, bestandsnaam)

print("dit bestand gaan we hernoemen: " + volledige_pad)

nieuwe_naam = input("Nieuwe bestandsnaam: ")
if len(nieuwe_naam) > 0:
    nieuwe_volledige_pad = os.path.join(huidigemap, nieuwe_naam)
    print("bestand wordt hernoemd naar: " + nieuwe_volledige_pad)
    os.rename(volledige_pad, nieuwe_volledige_pad)
    print("bestand hernoemd")
else:
    print("sorry, geen geldige invoer, einde programma")

time.sleep(2)
os.rename(nieuwe_volledige_pad, volledige_pad)
