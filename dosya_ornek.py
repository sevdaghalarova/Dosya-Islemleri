def not_hesapla(s):
    s=s[:-1]
    liste=s.split(",")

    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    son_not=(not1*3/10)+(not2*3/10)+(not3 * 4/10)
    harf=""
    if son_not>=90:
        harf="AA"
    elif son_not>=70:
        harf="BB"
    elif son_not>=60:
        harf="CC"
    elif son_not>=40:
        harf="DD"
    else:
        harf="FF"
    return isim + "-------->" + harf +"\n"

with open("dosya.txt","r",encoding="utf-8") as file:

    eklenecekler_listesi=[]
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("Notlar.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)


