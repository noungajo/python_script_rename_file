# delete_suffix_min.py

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

# add_suffix_param.py
Voici une documentation du code fourni :

Script de Renommage de Fichiers avec Suffixe

Description :
Ce script Python renomme tous les fichiers dans un répertoire en ajoutant un suffixe spécifié aux noms de fichiers. Le répertoire peut être spécifié en utilisant le chemin absolu ou en utilisant "pwd" pour le répertoire courant. Le suffixe est fourni en tant qu'argument en ligne de commande.

Utilisation :
python script.py [répertoire] [suffixe]

Arguments :
- répertoire (optionnel) : Chemin du répertoire contenant les fichiers à renommer. Si non spécifié, le répertoire courant sera utilisé.
- suffixe : Suffixe à ajouter aux noms de fichiers.

Exemple d'utilisation :
1. Renommer les fichiers dans le répertoire courant avec le suffixe "_nufi" :
   ```
   python script.py pwd _nufi
   ```
2. Renommer les fichiers dans un répertoire spécifique avec le suffixe "123" :
   ```
   python script.py /chemin/vers/le/repertoire 123
   ```

Notes :
- Les fichiers dans le répertoire spécifié seront renommés en ajoutant le suffixe fourni à leur nom d'origine.
- Le script utilise la commande `pwd` pour obtenir le répertoire courant.
- Les changements seront affichés à mesure que les fichiers sont renommés.

# del_suffix_nufi.py
Voici une documentation du code fourni :


Script de Renommage de Fichiers avec Suffixe "_nufi"

Description :
Ce script Python renomme tous les fichiers dans un répertoire en supprimant le suffixe "_nufi" de leurs noms. Le répertoire utilisé par défaut est le répertoire courant, mais vous pouvez spécifier un répertoire différent en modifiant la variable "repertoire_courant" dans le script.

Utilisation :
1. Placez le script dans le répertoire contenant les fichiers à renommer.
2. Exécutez le script avec Python :
   ```
   python script.py
   ```

Notes :
- Les fichiers dans le répertoire spécifié (ou le répertoire courant) seront renommés en supprimant le suffixe "_nufi" de leur nom d'origine.
- Les changements seront affichés à mesure que les fichiers sont renommés.




