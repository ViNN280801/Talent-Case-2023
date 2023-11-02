import nltk
import importlib


GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

# List of packages to check and install if not found
packages_to_check = ["numpy", "torch", "transformers",
                     "sentencepiece", "json", "nltk", "spicy"]

for package in packages_to_check:
    try:
        importlib.import_module(package)  # Try to import the package
        print(f"{BLUE}{package}{GREEN} is already installed{RESET}")
    except ImportError:
        # If the package is not found, install it
        print(f"{BLUE}{package}{RESET} is not installed. Installing...")
        try:
            # Use pip to install the package
            import subprocess
            subprocess.check_call(["pip", "install", package])
            print(f"{BLUE}{package}{GREEN} has been successfully installed{RESET}")
        except Exception as excptn:
            print(f"{RED}Error installing {package}: {str(excptn)}{RESET}")


# Importing 'wordnet'
try:
    nltk.data.find('corpora/wordnet.zip')
    print(f"{BLUE}WordNet data{GREEN} is already downloaded{RESET}")
    nltk.data.find('corpora/omw-1.4.zip')
    print(f"{BLUE}omw data{GREEN} is already downloaded{RESET}")
    nltk.data.find('tokenizers/punkt/PY3/english.pickle.zip')
    print(f"{BLUE}omw data{GREEN} is already downloaded{RESET}")
except LookupError:
    nltk.download('wordnet')
    print(f"{BLUE}WordNet data{GREEN} has been downloaded{RESET}")
    nltk.download('omw-1.4')
    print(f"{BLUE}omw data{GREEN} has been downloaded{RESET}")
    nltk.download('punkt')
    print(f"{BLUE}punkt data{GREEN} has been downloaded{RESET}")
