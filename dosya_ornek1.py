with open("dosya.txt","r",encoding="utf-8") as file:
    fb=[]
    gs=[]
    bsk=[]
    for futbolcu in file:
        futbolcu=futbolcu[:-1]
        liste1=futbolcu.split(",")
        isim=liste1[0]
        klup=liste1[1]
        if klup=="Galatasaray":
            gs.append(futbolcu + "\n")
        elif klup=="Fenerbahçe":
            fb.append(futbolcu + "\n")
        else:
            bsk.append(futbolcu + "\n")
        with open("gs.txt","w",encoding="utf-8") as gsaray:
            for i in gs:
                gsaray.write(i)

        with open("fb.txt","w",encoding="utf-8") as fbahce:
            for i in fb:
                fbahce.write(i)

        with open("bsk.txt","w",encoding="utf-8") as bstas:
            for i in bsk:
                bstas.write(i)


