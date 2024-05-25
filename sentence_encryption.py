#This function will help us to encrypt the sentence
def encrypt_sentence(sentence, shift):
    encrypted_sentence = ""

    for char in sentence:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_sentence += new_char
        else:
            encrypted_sentence += char

    return encrypted_sentence

# Example usage:
sentence = input("Enter the sentence to encrypt: ")
shift = int(input("Enter the shift value: "))
encrypted_sentence = encrypt_sentence(sentence, shift)
print("Encrypted sentence:", encrypted_sentence)
