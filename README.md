# Encrypting
CLI tool for Encryptig/Decrypting 


### How to use?
First, make sure to install cryptography package that includes Fernet encrypting module 
Use `pip install cryptography`

After you made sure you are ready to run it, there are 2 possible command lines
`python3 encytool.py --encrypt path/to/your/key.bin`
`python3 encytool.py --decrypt path/to/your/key.bin`

Flags represent the operation you want to perform and `.../key.bin` is a path for your encryption key(default: key_folder/key.bin), 
after running it for the first time(encryption) you will automatically have your key and text file for further decryption generated 
