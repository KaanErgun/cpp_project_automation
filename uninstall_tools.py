#!/usr/bin/env python3

import os
import sys
import platform
import subprocess

def uninstall_tool(tool_name):
    os_type = platform.system()
    if os_type == "Linux":
        subprocess.run(["sudo", "apt-get", "remove", "--purge", tool_name])
    elif os_type == "Darwin":
        if tool_name == "g++":  # g++ is provided by the gcc formula in Homebrew
            tool_name = "gcc"
        subprocess.run(["brew", "uninstall", tool_name])
    elif os_type == "Windows":
        print(f"For Windows, please uninstall '{tool_name}' manually.")
    else:
        print(f"Unsupported OS: {os_type}")

if __name__ == "__main__":
    print("This script will uninstall the tools installed by the main script.")
    choice = input("Are you sure you want to continue? [yes/NO]: ").strip().lower()

    if choice == "yes":
        uninstall_tool("make")
        uninstall_tool("g++")
        print("Uninstallation completed.")
    else:
        print("Uninstallation cancelled.")
