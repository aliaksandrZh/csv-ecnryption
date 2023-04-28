from cryptography.fernet import Fernet


def encrypt_files(files, key):
    f = Fernet(key)

    for (file, path) in files.items():
        path_to_source_file = path["path_to_source_file"]
        path_to_encrypted_file = path["path_to_protected_file"]

        try:
            with open(path_to_source_file, 'rb') as source_file:
                source_file_data = source_file.read()
                encrypted_data = f.encrypt(source_file_data)

            with open(path_to_encrypted_file, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
        except Exception as error:
            print(error)
            print(f"Was not able to encrypt {file}")
        else:
            print(f"{path_to_source_file} -> {path_to_encrypted_file}")


def decrypt_files(files, key):
    f = Fernet(key)

    for (file, path) in files.items():
        path_to_source_file = path["path_to_source_file"]
        path_to_encrypted_file = path["path_to_protected_file"]

        try:
            with open(path_to_encrypted_file, 'rb') as encrypted_file:
                encrypted_file_data = encrypted_file.read()
                decrypted_data = f.decrypt(encrypted_file_data)

            with open(path_to_source_file, "wb") as source_file:
                source_file.write(decrypted_data)
        except Exception as error:
            print(error)
            print(f"Was not able to decrypt {file}")
        else:
            print(f"{path_to_encrypted_file} -> {path_to_source_file}")
