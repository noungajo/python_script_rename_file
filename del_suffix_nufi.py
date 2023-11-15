import os

def renommer_fichiers(repertoire):
    # Vérifiez si le répertoire existe
    if os.path.exists(repertoire):
        # Parcourez tous les fichiers dans le répertoire
        for filename in os.listdir(repertoire):
            # Construisez le chemin complet du fichier
            chemin_fichier = os.path.join(repertoire, filename)

            # Vérifiez si le chemin est un fichier
            if os.path.isfile(chemin_fichier):
                # Obtenez le nom du fichier et l'extension
                nom_fichier, extension = os.path.splitext(filename)

                # Vérifiez si le fichier a le suffixe "_nufi"
                if nom_fichier.endswith("_nufi"):
                    # Construisez le nouveau nom de fichier en supprimant "_nufi"
                    nouveau_nom = nom_fichier[:-5] + extension
                    nouveau_nom_complet = os.path.join(repertoire, nouveau_nom)

                    # Renommez le fichier
                    os.rename(chemin_fichier, nouveau_nom_complet)

        print("Renommage terminé.")
    else:
        print("Le répertoire spécifié n'existe pas.")

# Obtenez le répertoire courant
repertoire_courant = os.getcwd()

# Appelez la fonction avec le répertoire courant
renommer_fichiers(repertoire_courant)
