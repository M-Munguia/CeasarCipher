def encryptionAlgorithm(message):
    """
    Encrypts the input message using a Caesar cipher with a shift of 3.
    
    Parameters:
    message (str): The plain text message to encrypt.

    Returns:
    str: The encrypted message, where each letter is shifted by 3 positions.
         Non-alphabetical characters remain unchanged.
    """
    encrypted_text = ''
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            if char.isupper():  # Encrypt uppercase letters
                encrypted_text += chr((ord(char) - 65 + 3) % 26 + 65)
            else:  # Encrypt lowercase letters
                encrypted_text += chr((ord(char) - 97 + 3) % 26 + 97)
        else:
            encrypted_text += char  # Non-alphabetical characters remain unchanged
    return encrypted_text

def decryptionAlgorithm(message):
    """
    Decrypts the input message using Caesar cipher (shifts 3).
    
    Parameter:
    message (str): Encrypted message that will be decrypt.

    Returns:
    str: Returns decrypted message (each letter is shifted back by 3).
         Non-alphabetical characters remain unchanged.
    """
    decrypted_text = ''
    for char in message:
        if char.isalpha():  # checks if the character is a letter
            if char.isupper():  # decrypt uppercase letters
                decrypted_text += chr((ord(char) - 65 - 3) % 26 + 65)
            else:  # decrypts lowercase letters
                decrypted_text += chr((ord(char) - 97 - 3) % 26 + 97)
        else:
            decrypted_text += char  # Non-alphabetical characters remain unchanged
    return decrypted_text

def main():
    """
    Main function that provides a simple menu for the user to encrypt, decrypt, or exit the program.
    The user can choose to:
    1. Enter plain text to encrypt using the Caesar cipher.
    2. Enter cipher text to decrypt.
    3. Exit the program.
    """
    while True:
        print("---------Menu---------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter a number: ")

        if choice == '1':
            plaintext = input("Enter plain text: ")
            encrypted_text = encryptionAlgorithm(plaintext)
            print("Encrypted text:", encrypted_text)
        elif choice == '2':
            ciphertext = input("Enter cipher text: ")
            decrypted_text = decryptionAlgorithm(ciphertext)
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            print("Now exiting... Goodbye!")
            break
        else:
            print("Please re-enter a valid number.")

if __name__ == "__main__":
    main()
