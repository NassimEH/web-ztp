import os
import subprocess
import sys


def generate_docs():
    try:
        # Vérifier si Sphinx est installé
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "../requirements.txt"],
            check=True,
        )

        # Générer la documentation
        os.chdir("docs")
        subprocess.run(["make", "html"], check=True)

        print("Documentation générée avec succès !")
        print(
            "Vous pouvez accéder à la documentation en ouvrant _build/html/index.html"
        )

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la génération de la documentation : {e}")
        sys.exit(1)


if __name__ == "__main__":
    generate_docs()
