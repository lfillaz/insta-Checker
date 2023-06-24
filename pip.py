import subprocess

libraries = [
    "user_agent",
    "datetime",
    "requests",
    "queue",
    "pyfiglet",
    "art"
]

def install_libraries():
    for library in libraries:
        try:
            print(f"Installing {library}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            print(f"{library} installed successfully!")
        except subprocess.CalledProcessError:
            print(f"Failed to install {library}!")

install_libraries()
