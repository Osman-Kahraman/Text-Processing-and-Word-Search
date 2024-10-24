makale = """The data was collected over a period of four years from 22 billion automated emergency radio signals of over 70,000 ships.  Although it is not totally accurate because smaller boats are not required to use tracking signals, it does show where most of the fishing takes place. Special software was used to generate maps that show where fishing is most intensive, such as the northern Atlantic and northwestern Pacific Ocean.

The study also shows that the biggest influences on fishing come from political and cultural activities. Environmental problems, seasonal differences or the changing of ocean currents do not affect fishing that much.

"""

makale_düzeltilmiş = set()

makale_liste = makale.split(" ",)
for i in makale_liste:
    i = i.lower().replace("\n", "").strip(".").strip(",").strip(":").strip("...")
    makale_düzeltilmiş.add(i)

kelimeden_öncesi = makale.find("study") - 1
kelimeden_sonrası = makale.find(" ", makale.find(" ", makale.find("study"))) + 1

önceki_kelime_bozuk = ""
önceki_kelime = ""
sonraki_kelime = ""

aşağıdaki_çözüm = makale[0:kelimeden_öncesi]
for i in aşağıdaki_çözüm[::-1]: #Burada bir mantıksal hata var gibi. Çünkü [:kelimeden_öncesi:-1] yapınca boş değer veriyor. O yüzden üstteki çözümü uyguladım. 
    if i == " " or i == "." or i == "\n" or i == "\t":
        break
    önceki_kelime_bozuk += i
for i in önceki_kelime_bozuk[::-1]:
    önceki_kelime += i

for i in makale[kelimeden_sonrası:-1:]:
    if i == " " or i == "." or i == "\n" or i == "\t":
        break
    sonraki_kelime += i
print(önceki_kelime, sonraki_kelime)
