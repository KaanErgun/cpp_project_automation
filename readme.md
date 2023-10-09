# C++ Project Initializer

This repository contains two scripts to help you set up and tear down a basic C++ project environment:

1. `initiate_cpp_project.py`: Initializes a new C++ project with a `main.cpp` file and a `Makefile`.
2. `uninstall_tools.py`: Uninstalls the tools that were installed by the main script.

## initiate_cpp_project.py

### Description

This script sets up a new C++ project in the specified directory. If the required tools (`make` and `g++`) are not installed, the script will attempt to install them.

### Usage

```bash
python3 initiate_cpp_project.py <project_name>
```

### Options

- `-h, --help`: Display the help menu.
- `-u, --usage`: Display usage information.
- `-a, --author`: Display author information.
- `-v, --version`: Display version information.

## uninstall_tools.py

### Description

This script uninstalls the tools (`make` and `g++`) that were installed by the main script. Before proceeding, it will ask for user confirmation.

### Usage

```bash
python3 uninstall_tools.py
```

## Requirements

- Python 3
- Internet connection (for installing tools if they're not already installed)

## Author

Kaan Ergun - [https://kaanergun.com/](https://kaanergun.com/)
