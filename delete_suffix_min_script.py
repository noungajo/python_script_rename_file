import os
import argparse

def rename_files_in_directory(directory):
    # Si le répertoire est "pwd", utilisez le répertoire courant
    if directory == "pwd":
        directory = os.getcwd()
    # Parcourez tous les fichiers du répertoire
    for filename in os.listdir(directory):
        if filename.endswith("-min.png"):
            # Construisez le nouveau nom de fichier sans le suffixe "-min"
            new_filename = os.path.join(directory, filename.replace("-min", ""))
            
            # Renommez le fichier
            os.rename(os.path.join(directory, filename), new_filename)
            print(f"Renommé {filename} en {new_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Renomme les fichiers dans un répertoire en supprimant le suffixe '-min' des noms de fichiers.")
    parser.add_argument("directory", nargs="?", default=os.getcwd(),  help="Chemin du répertoire contenant les fichiers à renommer.")
    
    args = parser.parse_args()
    directory = args.directory
    
    rename_files_in_directory(directory)
