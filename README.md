# script_renommer_fichier.py

Script de Renommage de Fichiers

Description :
Ce script Python renomme les fichiers dans un répertoire en supprimant le suffixe '-min' des noms de fichiers. Vous pouvez spécifier le répertoire en fournissant son chemin en tant qu'argument du script.

Utilisation :
python script.py [directory]

Arguments :
- directory (optionnel) : Chemin du répertoire contenant les fichiers à renommer. Si non spécifié, le répertoire courant sera utilisé.

Exemple d'utilisation :
1. Renommer les fichiers dans le répertoire courant :
   ```
   python script.py
   ```
2. Renommer les fichiers dans un répertoire spécifique :
   ```
   python script.py /chemin/vers/le/repertoire
   ```

Notes :
- Le script prend en charge le répertoire courant si l'argument "directory" est spécifié comme "pwd".
- Les fichiers avec le suffixe '-min' dans leur nom seront renommés sans ce suffixe.
- Les changements seront affichés à mesure que les fichiers sont renommés.


