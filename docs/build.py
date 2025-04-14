import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def build_docs():
    try:
        # Get the absolute path of the docs directory
        docs_dir = Path(__file__).parent.absolute()
        source_dir = docs_dir / 'source'
        build_dir = docs_dir / '_build' / 'html'
        
        # Create build directory if it doesn't exist
        build_dir.mkdir(parents=True, exist_ok=True)
        
        # Install dependencies
        print("Installation des dépendances...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', str(docs_dir / 'requirements.txt')], check=True)
        
        # Build the documentation
        print("Construction de la documentation...")
        os.chdir(str(source_dir))
        subprocess.run(['sphinx-build', '-b', 'html', '.', str(build_dir)], check=True)
        
        # Open in browser
        index_path = build_dir / 'index.html'
        print(f"Ouverture de la documentation dans le navigateur...")
        webbrowser.open(f'file://{index_path.absolute()}')
        
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}")
        sys.exit(1)

if __name__ == '__main__':
    build_docs() 