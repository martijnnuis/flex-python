from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

lettertype = ImageFont.truetype("impact", 30)

tekengebied = ImageDraw.Draw(achtergrond)
tekst = "groningers\ncompenseren\nen redelijkheid\nzijn"
tekst2 = "overheid"
tekengebied.multiline_text((50,80), tekst, font=lettertype, fill=(0,0,0))
tekengebied.multiline_text((450, 50), tekst2, font=lettertype, fill=(0,0,0))
achtergrond.show()
achtergrond.save("meme_background.jpg")