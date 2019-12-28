import hashlib
print()
print("dir(hashlib): ",dir(hashlib),len(dir(hashlib)))
print()
def SHA256(Text):
    Sha256_Sig = hashlib.sha256(Text.encode()).hexdigest()
    return Sha256_Sig
r = 1
while r:
    Text = input("Geben Sie einen Text ein: ")
    Sha256_Sig = SHA256(Text)
    print()
    print("Der Sha256 der Eingabe: ", Text, "lautet: ",Sha256_Sig)
    print()
    r = input("Soll noch ein Sha256-Wert berechnet werden, dann geben Sie ein bel. Zeichen ein. Ansonsten drücken Sie die Enter-taste.")
#Vergleich von zwei Hashwerten
print()
print("Jetzt vergleichen wir zwei sehr ähnliche Texte und deren SHA256-Werte.")
print()
s = 1
while s:
    print()
    Text1 = input("Erster Text: ")
    print()
    print("Der Sha256 der Eingabe: ", Text1, "lautet: ",SHA256(Text1), type(SHA256(Text1)))
    print()
    Text2 = input("Zweiter Text: ")
    print()
    print("Der Sha256 der Eingabe: ", Text2, "lautet: ",SHA256(Text2), type(SHA256(Text2)))
    print()
    Zahl = 0
    for i in range(64):
        if SHA256(Text1)[i] == SHA256(Text2)[i]:
            Zahl +=1
            print(i,"-te Stelle",SHA256(Text1)[i])
            print()
    print("Die Hashwerte stimmen an: ",Zahl," Stelle/Stellen überein.")
    print()
    s = input("Noch ein Vergleich? Dann geben Sie ein bel. Zeichen ein, ansonsten drücken Sie die Enter-Taste.")
