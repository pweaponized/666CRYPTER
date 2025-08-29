# EXE Crypter (Educational / Testing Use Only)

**Disclaimer:**  
This tool is intended **solely for educational and testing purposes**. Do **not** use it to distribute malware or violate any laws. Misuse may result in serious legal consequences. Always test with your own harmless executables.

---

## Overview

This Python script allows you to **encrypt an executable file (EXE)** using AES-128 encryption (CBC mode) and compile it into a single executable that can decrypt and run the original EXE at runtime.

The generated output executable is named `crypted.exe`.

---

## Features

- AES-128 CBC encryption for EXE files.  
- Base64 encoding of the AES key and IV for embedding in the Python stub.  
- Generates a standalone executable (`crypted.exe`) using PyInstaller.  
- Cleans up temporary files automatically after compilation.  
- Simple command-line interface (CLI) to specify the file path.  

---

## Requirements

- Python 3.10 or higher  
- [PyCryptodome](https://pypi.org/project/pycryptodome/) (`pip install pycryptodome`)  
- [PyInstaller](https://www.pyinstaller.org/) (`pip install pyinstaller`)  

---

## Usage

1. Run the script:

```bash
python crypted_creator.py