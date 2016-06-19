import random

"""

Teresa Henderson
CST 100 - Bansal
06/10/2016

assign4-pt2.py

Part 2: Encryption and Decryption

ascii-table-dict generated with:

$ cat ascii-table.txt | gawk -F" " '{print $7": ", "\x22"$6"\x22","\n", $12," : ""\x22"$11"\x22", "\n",
$17," : ""\x22"$16"\x22"}' | sort -n | sed -e 's/$/,/g'


"""

# Creates a user menu for the user to enter information to decrypt or encrypt
def user_menu():
    request_type = input("Do you wish to (E)ncrypt or (D)ecrypt? ")
    request_type_lc = request_type.lower()
    if request_type_lc == 'e':
        plain_message = input("Please enter a phrase to encrypt: ")
        encrypt_message(plain_message)
    elif request_type_lc == 'd':
        encrypted_message = input("Please enter a phrase to decrypt: ")
        decrypt_message(encrypted_message)
    else:
        raise ValueError("You did not enter a valid option!")

# Encryption function takes user input
def encrypt_message(plain_message):
    # Randomly generates a key for encrytpion
    crypto_key = int(random.randint(1, 100))
    encrypt_generate_string = []

    print("Randomized Encryption Key: " + str(crypto_key))
    # For each letter in plain message translate to numeric value and apply
    # encryption algorithim for each letter
    for n in plain_message:
        n = ord(n)
        if n + crypto_key > 126:
            encrypt_num = ((n + crypto_key) - 127) + 32
            encrypt_char = chr(encrypt_num)
            encrypt_generate_string.append(encrypt_char)
        else:
            encrypt_num = (n + crypto_key)
            encrypt_char = chr(encrypt_num)
            encrypt_generate_string.append(encrypt_char)
    # Print the final encrypted message by joining the letters into a string
    final_encrypted_message = "".join(str(e) for e in encrypt_generate_string)
    print("Encrypted Message: " + final_encrypted_message)

# Decryption function takes user input
def decrypt_message(encrypted_message):
    # Create a range of keys to try decrypting encrypted values
    decrypt_keys = [k for k in range(0, 101, 1)]
    decrypt_text = []
    decrypt_str = ""
    # For each decryption key and each letter the encrypted message apply the decryption key
    for decrypt_key in decrypt_keys:
        for l in encrypted_message:
            l = ord(l)
            if l - decrypt_key < 32:
                decrypt_num = ((l - decrypt_key) + 127) - 32
            else:
                decrypt_num = (l - decrypt_key)
            # Use the ascii table lookup function to match numeric values post
            # decryption algorithim translation to characters
            conv_to_plain = chr(decrypt_num)
            # Create a string from the decrypted letters and print each string
            decrypt_str = str(decrypt_str) + str(conv_to_plain)
        # Print each key for each run with the string that was decrypted
        decrypt_str = "Key " + str(decrypt_key) + " :: " + decrypt_str
        decrypt_text.append(decrypt_str)
        decrypt_str = ""
    # Printthe final key and decrypted string value
    final_decrypted_message = "\n".join(str(f) for f in decrypt_text)
    print(final_decrypted_message)

user_menu()


