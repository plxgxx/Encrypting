import argparse
from cryptography.fernet import Fernet
from pathlib import Path

def generate_key(key_path: str):
    """
    Generates binary file that works as a key

    key_path - str: Path to the file
    """

    key = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
    print(f'Key generated and saved to {key_path}')

def load_key(key_path:str):
    """
    Loads binary file to retrieve key 

    key_path - str: Path to the file
    """
    return open(key_path, 'rb').read()

def encrypt_message(key: str, message: str) -> str:
    """
    Process of encrypting file using fernet-created key
    
    key - str: Token used for metod of encrypting text
    message - str: Message to be encrypted further 
    """

    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    """
    Process of decrypting file using fernet-created key
    
    key - str: Token used for metod of decrypting message
    message - str: Message to be decrypted further 
    """
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    """
    Main function that performs enabling of the command line interface 
    and performing operations with given flags/arguments

    """

    parser = argparse.ArgumentParser(description='Encrypt or decrypt text using a binary key file.')
    parser.add_argument('key_path', help='Path to the binary key file')
    parser.add_argument('--encrypt', action='store_true', help='Encrypt the input text')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the message file')

    args = parser.parse_args()

    if args.encrypt and args.decrypt:
        print("Please choose either --encrypt or --decrypt, not both.")
        return

    if not args.encrypt and not args.decrypt:
        print("Please choose either --encrypt or --decrypt.")
        return

    key_file = Path(args.key_path)
    if not key_file.is_file():
        generate_key(args.key_path)
    
    key = load_key(args.key_path)

    if args.encrypt:
        message = input('Enter the text to encrypt: ')
        encrypted_message = encrypt_message(key, message)
        with open('encrypted_message.txt', 'wb') as file:
            file.write(encrypted_message)
        print(f'Encrypted message: {encrypted_message} , it is saved to encrypted_message')
    else:
        with open('encrypted_message.txt', 'r') as file:
            encrypted_message = file.read()
        decrypted_message = decrypt_message(key, encrypted_message.encode())
        print(f'Decrypted message: {decrypted_message}')

if __name__ == '__main__':
    main()