#!/usr/bin/env python3

import os
import sys
import platform
import subprocess
import threading
import time

VERSION = "0.1.8"

def is_tool_installed(name):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which
    return which(name) is not None

def is_connected():
    try:
        import requests
        response = requests.get("https://www.kaanergun.com", timeout=5)
        return True
    except ImportError:
        subprocess.run(["pip3", "install", "requests"])
        import requests
        response = requests.get("https://www.kaanergun.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

class LoadingAnimation:
    def __init__(self, message="Processing"):
        self.message = message
        self.is_running = False

    def start(self):
        self.is_running = True
        threading.Thread(target=self.animate).start()

    def stop(self):
        self.is_running = False

    def animate(self):
        symbols = ['|', '/', '-', '\\']
        idx = 0
        while self.is_running:
            sys.stdout.write('\r' + symbols[idx] + ' ' + self.message + '...')
            sys.stdout.flush()
            idx = (idx + 1) % 4
            time.sleep(0.2)
        sys.stdout.write('\rDone!          \n')  # Clear the animation

def install_tool_with_animation(tool_name):
    animation = LoadingAnimation(f"Installing {tool_name}")
    animation.start()

    os_type = platform.system()
    if os_type == "Linux":
        subprocess.run(["sudo", "apt-get", "update"])
        subprocess.run(["sudo", "apt-get", "install", tool_name])
    elif os_type == "Darwin":
        if tool_name == "g++":  # g++ is provided by the gcc formula in Homebrew
            tool_name = "gcc"
        if not is_tool_installed("brew"):
            print("Homebrew is not installed. Installing now...")
            subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])
        subprocess.run(["brew", "install", tool_name])
    elif os_type == "Windows":
        print(f"For Windows, please install '{tool_name}' using MinGW or Cygwin.")
    else:
        print(f"Unsupported OS: {os_type}")

    animation.stop()

# Check if make is installed
if not is_tool_installed("make"):
    if not is_connected():
        print("Error: No internet connection detected. Please ensure you are connected to the internet and try again.")
        sys.exit(1)
    print("'make' is not installed. Installing now...")
    install_tool_with_animation("make")

# Check if g++ is installed
if not is_tool_installed("g++"):
    if not is_connected():
        print("Error: No internet connection detected. Please ensure you are connected to the internet and try again.")
        sys.exit(1)
    print("'g++' is not installed. Installing now...")
    install_tool_with_animation("g++")

def display_help():
    print("Usage: python3 initiate_cpp_project.py <project_name>")
    print("Options:")
    print("  -h, --help     Display this help menu.")
    print("  -u, --usage    Display usage information.")
    print("  -a, --author   Display author information.")
    print("  -v, --version  Display version information.")

def display_author():
    print("Author: Kaan Ergun")
    print("Website: \033[4mhttps://kaanergun.com/\033[0m")

def display_version():
    print(f"Version: {VERSION}")

def handle_existing_project(project_name):
    choice = input(f"The project '{project_name}' already exists. Do you want to override (O) or cancel (C)? [default: C]: ").strip().lower()
    if choice == "o":
        import shutil
        shutil.rmtree(project_name)
        return True
    else:  # Default to cancel
        return False

def create_cpp_project(project_name):
    if os.path.exists(project_name):
        if not handle_existing_project(project_name):
            return

    # Create the project directory
    os.makedirs(project_name)

    # Create the main.cpp file
    with open(os.path.join(project_name, "main.cpp"), "w") as f:
        f.write("""#include <iostream>

int main() {
    //Code here
    return 0;
}
""")

    # Create the Makefile
    with open(os.path.join(project_name, "Makefile"), "w") as f:
        f.write(f"""all: {project_name}

{project_name}: main.o
    g++ main.o -o {project_name}

main.o: main.cpp
    g++ -c main.cpp

clean:
    rm -rf *o {project_name}
""")

    print(f"C++ project successfully created in the '{project_name}' directory!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid usage. Use -h or --help for more information.")
    elif sys.argv[1] in ["-h", "--help", "-u", "--usage"]:
        display_help()
    elif sys.argv[1] in ["-a", "--author"]:
        display_author()
    elif sys.argv[1] in ["-v", "--version"]:
        display_version()
    else:
        project_name = sys.argv[1]
        create_cpp_project(project_name)
