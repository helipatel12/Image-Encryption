# 🛡️ Image Encryption using DES and AES

This project allows you to encrypt and decrypt image files using two widely known symmetric encryption algorithms: **DES (Data Encryption Standard)** and **AES (Advanced Encryption Standard)**. It also includes functionality to simulate an attack by corrupting the ciphertext and attempting decryption.

---

## 📸 Features

- 🔐 Encrypt JPEG images using DES or AES
- 🔓 Decrypt encrypted images
- 🧪 Simulate a corrupted ciphertext and attempt to decrypt it
- 📁 Automatically stores results in structured folders (DES/ and AES/)

---

## 🛠️ Technologies Used

- Python 3
- [PyCryptodome](https://pypi.org/project/pycryptodome/) – for cryptographic operations
- [Pillow](https://pypi.org/project/Pillow/) – for image handling

---

## 📂 File Structure

```
Image-Encryption/
├── AES/
│   ├── plaintext_encrypt.jpeg
│   ├── plaintext_decrypt.jpeg
│   ├── plaintext_corrupted_encrypt.jpeg
│   └── plaintext_decrypted_corrupted.jpeg
├── DES/
│   ├── plaintext_encrypt.jpeg
│   ├── plaintext_decrypt.jpeg
│   ├── plaintext_corrupted_encrypt.jpeg
│   └── plaintext_decrypted_corrupted.jpeg
├── plaintext.jpeg
├── ed.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Use

### 📥 Clone the Repository

```bash
git clone https://github.com/helipatel12/Image-Encryption.git
cd Image-Encryption
```

### 🧱 Create and Activate a Virtual Environment (Optional)

```bash
# Create virtual environment
python -m venv env

# Activate on Windows
env\Scripts\activate

# Activate on macOS/Linux
source env/bin/activate
```

### 📦 Install Required Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the Program

Make sure a JPEG image named `plaintext.jpeg` is in the root directory. Then run:

```bash
python ed.py
```

Follow the prompts:
- Choose either AES or DES.
- The script will:
  - Encrypt the image.
  - Decrypt it back.
  - Corrupt the encrypted file.
  - Attempt to decrypt the corrupted file.

Encrypted and decrypted images will be saved in the appropriate `AES/` or `DES/` folder.

---

## 🧪 Sample Output Files

- `plaintext_encrypt.jpeg` — Encrypted version
- `plaintext_decrypt.jpeg` — Decrypted version (should match original)
- `plaintext_corrupted_encrypt.jpeg` — Corrupted ciphertext
- `plaintext_decrypted_corrupted.jpeg` — Decryption result of corrupted data

---

## 📄 requirements.txt

To generate this file manually:

```bash
pip freeze > requirements.txt
```

Or copy this content:

```
pycryptodome
Pillow
```

---

## ⚠️ Disclaimer

This project is for **educational purposes** only. ECB mode is used, which is insecure for real-world use due to its pattern leakage. For production-grade encryption, consider secure modes like CBC or GCM.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Heli Patel**  
🔗 [GitHub Profile](https://github.com/helipatel12)