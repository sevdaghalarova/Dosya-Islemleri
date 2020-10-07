
# Dosya acma islemi
# with open("dosya_adi","Dosya kipi",encoding="utf-8")
# -utf-8 turkce karakter desteklemesi icin
with open("deneme.txt","w",encoding="utf-8") as file:
    file.write("Merhaba")

# "w" okuma kipi - dosya acar, yazi ise her dosya acildiginda diger yazi silinir uzerine yazilir
# "a" okuma kipi-dosya acar, yazi ise dosya acildiginda onceki yazinin sonuna yazilir.
