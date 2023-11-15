import os
import sys
import subprocess

def renommer_fichiers(repertoire, suffixe):
    # Vérifiez si le répertoire existe
    if os.path.exists(repertoire):
        # Parcourez tous les fichiers dans le répertoire
        for filename in os.listdir(repertoire):
            # Construisez le chemin complet du fichier
            fichier_complet = os.path.join(repertoire, filename)

            # Vérifiez si le chemin est un fichier
            if os.path.isfile(fichier_complet):
                # Ajoutez le suffixe au nom du fichier
                nom_fichier, extension = os.path.splitext(filename)
                nouveau_nom = f"{nom_fichier}{suffixe}{extension}"
                nouveau_nom_complet = os.path.join(repertoire, nouveau_nom)

                # Renommez le fichier
                os.rename(fichier_complet, nouveau_nom_complet)

        print("Renommage terminé.")
    else:
        print("Le répertoire spécifié n'existe pas.")

# Obtenez le répertoire courant en utilisant la commande `pwd`
repertoire_courant = subprocess.check_output(["pwd"], universal_newlines=True).strip()

# Vérifiez si les arguments sont corrects
if len(sys.argv) != 3:
    print("Utilisation: python script.py pwd <suffixe>")
    sys.exit(1)

# Récupérez le suffixe de la ligne de commande
suffixe_a_ajouter = sys.argv[2]

# Appelez la fonction avec les arguments fournis
renommer_fichiers(repertoire_courant, suffixe_a_ajouter)
