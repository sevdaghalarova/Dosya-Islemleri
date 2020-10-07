with open("deneme.txt","r",encoding="utf-8") as file1:
    #print(file1.read()) # dosyanin tumunu okuyor
    #print(file1.readline()) # dosyayi satir satir okuyor
    #print(file1.readlines()) # dosyayi satir satir okuyup listeye atiyor

    # for ile okuma ornegi
    for i in file1:
        print(i,end="")