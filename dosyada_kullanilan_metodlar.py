with open("deneme.txt","r",encoding="utf-8") as file1:
    file1.seek(5) #imleci 5'ci bayta getiriyor
    print(file1.read(10))
    print(file1.tell()) # imlecin hangi baytda oldugunu soyluyor


