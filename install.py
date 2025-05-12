import os
import sys
import platform
import subprocess
from pathlib import Path

# Determine platform
OS_NAME = platform.system()

# Get the script's directory
SCRIPT_DIR = Path(__file__).resolve().parent

# Define virtual environment path
VENV_DIR = SCRIPT_DIR / ".mlgenealogy"
PYTHON_EXECUTABLE = sys.executable

# Define activation script path
VENV_ACTIVATE = VENV_DIR / (
    "Scripts/activate" if OS_NAME == "Windows" else "bin/activate"
)

# List of packages to install
REQUIRED_PACKAGES = [
    "easyocr",
    "deephand",
    "trdg",
]

# Create virtual environment if it doesn't exist
if not VENV_DIR.exists():
    subprocess.run([PYTHON_EXECUTABLE, "-m", "venv", str(VENV_DIR)], check=True)


# Function to install a package
def install_package(package_name):
    try:
        subprocess.run(
            [
                str(
                    VENV_DIR / "bin/pip"
                    if OS_NAME != "Windows"
                    else VENV_DIR / "Scripts/pip"
                ),
                "install",
                package_name,
            ],
            check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


# Install packages and track successes and failures
successful_installs = []
failed_installs = []

for package in REQUIRED_PACKAGES:
    if install_package(package):
        successful_installs.append(package)
    else:
        failed_installs.append(package)

# Define PYTHONPATH entry
PYTHONPATH_ENTRY = (
    f'export PYTHONPATH="{SCRIPT_DIR}:$PYTHONPATH"'
    if OS_NAME != "Windows"
    else f"set PYTHONPATH={SCRIPT_DIR};%PYTHONPATH%"
)

# Add PYTHONPATH to the activation script if not already present
if VENV_ACTIVATE.exists():
    with open(VENV_ACTIVATE, "r") as activate_script:
        if PYTHONPATH_ENTRY not in activate_script.read():
            with open(VENV_ACTIVATE, "a") as append_script:
                append_script.write(f"\n{PYTHONPATH_ENTRY}\n")
                print(f"Added PYTHONPATH entry to {VENV_ACTIVATE}.")
        else:
            print("PYTHONPATH entry already exists in the activation script.")
else:
    print(f"Activation script {VENV_ACTIVATE} does not exist.")

# Display summary of installations
print("\nInstallation Summary:")
print("Successfully installed packages:")
for pkg in successful_installs:
    print(f"  - {pkg}")
if failed_installs:
    print("\nPackages that failed to install:")
    for pkg in failed_installs:
        print(f"  - {pkg}")

# Command to activate the virtual environment
if OS_NAME != "Windows":
    activate_command = f"source {VENV_ACTIVATE} && echo 'Activated virtual environment'"
else:
    activate_command = (
        f'cmd /c "{VENV_ACTIVATE}.bat && echo Activated virtual environment"'
    )

# Run the activation command in a shell
subprocess.run(activate_command, shell=True)

# Run the pip install command via subprocess
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
