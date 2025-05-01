from Crypto.Cipher import DES, AES          # Cryptographic ciphers
from Crypto.Random import get_random_bytes  # Secure random key generation
from Crypto.Util.Padding import pad, unpad  # Padding utilities for block ciphers
from PIL import Image                       # Image processing (not used directly here but imported)
import os
import glob                                 # File pattern matching

# -------------------- Encryption Functions --------------------

# Encrypt data using DES in ECB mode
def encrypt_des(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, DES.block_size))

# Decrypt DES-encrypted data
def decrypt_des(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), DES.block_size)

# Encrypt data using AES in ECB mode
def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, AES.block_size))

# Decrypt AES-encrypted data
def decrypt_aes(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

# -------------------- File Handling Functions --------------------

# Encrypt an image file using either DES or AES
def encrypt_image(input_file, output_file, key, algorithm='DES'):
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    if algorithm == 'DES':
        ciphertext = encrypt_des(plaintext, key)
    elif algorithm == 'AES':
        ciphertext = encrypt_aes(plaintext, key)

    with open(output_file, 'wb') as f:
        f.write(ciphertext)

# Decrypt an encrypted image file using either DES or AES
def decrypt_image(input_file, output_file, key, algorithm='DES'):
    with open(input_file, 'rb') as f:
        ciphertext = f.read()

    if algorithm == 'DES':
        plaintext = decrypt_des(ciphertext, key)
    elif algorithm == 'AES':
        plaintext = decrypt_aes(ciphertext, key)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

# -------------------- Attack Simulation --------------------

# Corrupt at least 50% of the ciphertext to simulate an attack
def attack_generator(input_file, output_file):
    with open(input_file, 'rb') as f:
        ciphertext = f.read()

    corrupted_ciphertext = bytearray(ciphertext)
    for i in range(len(corrupted_ciphertext) // 2):
        corrupted_ciphertext[i] = 0xFF  # Overwrite half of the bytes with 0xFF

    with open(output_file, 'wb') as f:
        f.write(corrupted_ciphertext)

# -------------------- Main Driver Code --------------------

def main():
    # Prompt user to select encryption algorithm
    algorithm_choice = input("Enter 'DES' or 'AES' to choose the encryption algorithm: ").strip().upper()
    if algorithm_choice not in ['DES', 'AES']:
        print("Invalid choice.")
        return

    # Search for .jpg and .jpeg files recursively
    image_files = glob.glob("**/*.jpg", recursive=True) + glob.glob("**/*.jpeg", recursive=True)
    if not image_files:
        print("No JPEG images found in the current directory or subdirectories.")
        return

    # Display available images
    print("\nAvailable images:")
    for idx, img in enumerate(image_files):
        print(f"{idx + 1}. {img}")

    # Get user image selection
    try:
        selection = int(input("\nSelect the image to encrypt (enter the number): "))
        input_file = image_files[selection - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    # Generate a secure key for the chosen algorithm
    key = get_random_bytes(8) if algorithm_choice == 'DES' else get_random_bytes(16)

    # Prepare output folder
    output_folder = algorithm_choice
    os.makedirs(output_folder, exist_ok=True)

    # Define output file paths
    filename = os.path.basename(input_file)
    name, ext = os.path.splitext(filename)
    encrypted_file = os.path.join(output_folder, f'{name}_encrypt{ext}')
    decrypted_file = os.path.join(output_folder, f'{name}_decrypt{ext}')
    corrupted_file = os.path.join(output_folder, f'{name}_corrupted_encrypt{ext}')
    decrypted_corrupted_file = os.path.join(output_folder, f'{name}_decrypted_corrupted{ext}')

    # Encrypt the image
    encrypt_image(input_file, encrypted_file, key, algorithm_choice)
    print(f"Image encrypted to: {encrypted_file}")

    # Decrypt the encrypted image
    decrypt_image(encrypted_file, decrypted_file, key, algorithm_choice)
    print(f"Image decrypted to: {decrypted_file}")

    # Simulate a corruption attack
    attack_generator(encrypted_file, corrupted_file)
    print(f"Corrupted file created: {corrupted_file}")

    # Attempt to decrypt the corrupted file
    decrypt_image(corrupted_file, decrypted_corrupted_file, key, algorithm_choice)
    print(f"Decryption after corruption saved as: {decrypted_corrupted_file}")

# Run the main function
if __name__ == "__main__":
    main()
