def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    son_not=(not1*3/10)+(not2*3/10)+(not3*4/10)
    harf = ""
    if son_not>=90:
        harf="AA"
    elif son_not>=80:
        harf="BB"
    elif son_not>=70:
        harf="BC"
    elif son_not>=60:
        harf="CC"
    elif son_not>=50:
        harf="DD"
    else:
        harf="FF"
    return isim+","+harf+"\n"

with open ("dosya.txt","r",encoding="utf-8") as file:
    eklenecekler_listesi=[]
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    with open("notlar.txt","w",encoding="utf-8") as file1:
        for i in eklenecekler_listesi:
            file1.write(i)
    with open("notlar.txt","r",encoding="utf-8") as file2:
        kalanlar=[]
        gecenler=[]
        for i in file2:
            i=i[:-1]
            liste=i.split(",")
            isim=liste[0]
            harf=liste[1]
            if harf=="FF":
                kalanlar.append(i+"\n")
            else:
                gecenler.append(i+"\n")

    with open("gecenler.txt","w",encoding="utf-8") as file3:
        for i in gecenler:
            file3.write(i)
    with open("kalanlar.txt","w",encoding="utf-8") as file4:
        for i in kalanlar:
            file4.write(i)