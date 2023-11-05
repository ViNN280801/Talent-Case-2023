import importlib


GREEN = '\033[1m\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m\033[1m'

# List of packages to check and install if not found
packages_to_check = ['re', 'json', 'time', 'psutil']

for package in packages_to_check:
    try:
        importlib.import_module(package)  # Try to import the package
        print(f'{BLUE}{package}{GREEN} is already installed{RESET}')
    except ImportError:
        # If the package is not found, install it
        print(f'{BLUE}{package}{RESET} is not installed. Installing...')
        try:
            # Use pip to install the package
            import subprocess
            subprocess.check_call(['pip', 'install', package])
            print(f'{BLUE}{package}{GREEN} has been successfully installed{RESET}')
        except Exception as excptn:
            print(f'{RED}Error installing {package}: {str(excptn)}{RESET}')
