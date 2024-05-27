import os
test = int(input("Veux tu vraiment suprimer ? (0) non , (1) oui "))

if test == 1:
    contenue = "LvL:\n1\nID de Zone:\n-1;0;0\nMoney:\n0\nNiveau de Quetes:\n0\nsac:\nNULL;NULL;NULL;LOCK;LOCK;LOCK;LOCK;LOCK;LOCK\nTouches:\n0b11010;0b100;0b10110;0b111;0b101100;0b1000"
    if os.path.isfile("sauvegarde.txt"):
        os.remove("sauvegarde.txt")

    with open("sauvegarde.txt", "w") as fichier:
        fichier.write(contenue)
    fichier.close()