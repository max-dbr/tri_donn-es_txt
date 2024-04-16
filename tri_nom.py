from pathlib import Path

chemin_actuel = Path(__file__).parent
fichier_a_lire = chemin_actuel / "prenoms.txt"

with open(fichier_a_lire , "r") as f :
    lecture = f.read()

print("\nContenu du fichier que l'on va devoir trier :")
print(lecture)

liste_de_mot = lecture.split()
mise_en_forme = [concat.strip(", . " ) for concat in liste_de_mot]
ordre_alphabetique = sorted(mise_en_forme)
liste_en_string = '\n'.join(ordre_alphabetique)

nom_fichier_a_creer = "noms_tris.txt"
chemin_fichier_a_créer = chemin_actuel / nom_fichier_a_creer
chemin_fichier_a_créer.touch(exist_ok=True)

with open(chemin_fichier_a_créer , "w") as f :
    f.write(liste_en_string)

with open(chemin_fichier_a_créer , "r") as f :
    lecture2 = f.read()

print("\nContenu du fichier que l'on a créé :")
print(lecture2)