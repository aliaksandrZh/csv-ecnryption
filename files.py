from os import listdir

encrypted_file_prefix = "enc_"
decrypted_file_prefix = "dec_"


def get_path_to_files():
    path = input("Please enter an absolute path to the directory with files you want to protect\n"
                 "In the following format: Users/<username>/<path>/<to>/<directory>:\n")
    path_with_prefix = f"/{path}"

    return path_with_prefix


def get_files_for_encryption():
    path_to_source_files = get_path_to_files()

    try:
        list_of_files = listdir(path_to_source_files)
        list_files_for_protection = [file for file in list_of_files if should_be_encrypted(file)]
    except Exception:
        raise FileNotFoundError()

    files_for_protection = {
        file: {
            "path_to_source_file": f"{path_to_source_files}/{file}",
            "path_to_protected_file": f"{path_to_source_files}/{encrypted_file_prefix}{file}"
        } for file in list_files_for_protection
    }

    return files_for_protection


def get_files_for_decryption():
    path_to_source_files = get_path_to_files()

    try:
        list_of_files = listdir(path_to_source_files)
        list_files_for_decryption = [file for file in list_of_files if should_be_decrypted(file)]
    except Exception:
        raise FileNotFoundError()

    files_for_decryption = {
        file: {
            "path_to_source_file": f"{path_to_source_files}/{decrypted_file_prefix}{file}",
            "path_to_protected_file": f"{path_to_source_files}/{file}"
        } for file in list_files_for_decryption
    }

    return files_for_decryption


def should_be_encrypted(file_name):
    return not file_name.startswith(encrypted_file_prefix) and not file_name.startswith(".")


def should_be_decrypted(file_name):
    return file_name.startswith(encrypted_file_prefix)
