from PIL import Image

afbeelding = Image.open("joakim.jpg")
afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

print("afbeelding is " + str(breedte) + " en pixels breed en " + str(hoogte) + " pixels hoog")
print(afbeelding.format, afbeelding.size, afbeelding.mode)
