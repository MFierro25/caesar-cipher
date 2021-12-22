def encrypt(text, key):
    cipher = ''
    
    for char in text:
        # checks to see if string is empty ( no change happens)
        # checks upper case
        if char.isupper():
            cipher += chr((ord(char)+key-65) % 26 + 65)
        # checks lower case
        elif char.islower():
            cipher += chr((ord(char)+key-97) % 26 + 97)
        # checks for characters NOT letters
        else:
            cipher += char
            
    return cipher

def decrypt(encoded, key):
    return encrypt(encoded, -key)

