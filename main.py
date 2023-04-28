from files import get_files_for_encryption, get_files_for_decryption
from key_provider import get_protection_key
from protection import encrypt_files, decrypt_files

encrypt_or_decrypt = input("What do you want to do? 1.Protect or 2.Unprotect\n")

if encrypt_or_decrypt == "1":
    source_files = get_files_for_encryption()
    protection_key = get_protection_key()
    encrypt_files(source_files, protection_key)
elif encrypt_or_decrypt == "2":
    source_files = get_files_for_decryption()
    protection_key = get_protection_key()
    decrypt_files(source_files, protection_key)
else:
    print("Wrong operation")