import base64
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import subprocess
import sys
import shutil

# --- Get EXE path from user ---
exe_path = input("Enter the path of the EXE file to encrypt: ").strip()
if not os.path.isfile(exe_path):
    print("Error: File does not exist!")
    sys.exit(1)

# --- Generate AES key and encrypt ---
key = get_random_bytes(16)  # 128-bit key
with open(exe_path, "rb") as f:
    original_data = f.read()

cipher = AES.new(key, AES.MODE_CBC)
encrypted_bytes = cipher.encrypt(pad(original_data, AES.block_size))

iv_b64 = base64.b64encode(cipher.iv).decode('utf-8')
encrypted_b64 = base64.b64encode(encrypted_bytes).decode('utf-8')
key_b64 = base64.b64encode(key).decode('utf-8')

# --- Create Python decryption and run code ---
decryption_code = f"""
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import subprocess
import os

iv = '{iv_b64}'
encrypted_b64 = '{encrypted_b64}'
key = base64.b64decode('{key_b64}')

encrypted_bytes = base64.b64decode(encrypted_b64)
iv_bytes = base64.b64decode(iv)

cipher = AES.new(key, AES.MODE_CBC, iv_bytes)
original_data = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)

exe_name = "temp.exe"
with open(exe_name, "wb") as f:
    f.write(original_data)

try:
    subprocess.call([exe_name])
finally:
    if os.path.exists(exe_name):
        os.remove(exe_name)
"""

# --- Save temporary Python file ---
temp_py = "temp_run.py"
with open(temp_py, "w", encoding="utf-8") as f:
    f.write(decryption_code)

# --- Compile with PyInstaller ---
print("Compiling encrypted EXE, please wait...")
subprocess.run(["pyinstaller", "--onefile", "--noconsole", temp_py])

# --- Rename output to crypted.exe ---
dist_path = os.path.join("dist", "temp_run.exe")
if os.path.exists(dist_path):
    os.rename(dist_path, "crypted.exe")
    print("Encrypted executable created: crypted.exe")
else:
    print("Error: Failed to create encrypted EXE.")

# --- Clean up temporary files ---
os.remove(temp_py)
if os.path.exists("build"):
    shutil.rmtree("build")
if os.path.exists("dist"):
    shutil.rmtree("dist")
if os.path.exists("temp_run.spec"):
    os.remove("temp_run.spec")

print("Temporary files cleaned up.")