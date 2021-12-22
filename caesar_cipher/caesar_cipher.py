def encrypt(text, key):
    cipher = ''
    
    for char in text:
        # checks to see if string is empty ( no change happens)
        if char == '':
            cipher = cipher + char
        # checks upper case
        elif char.isupper():
            cipher = cipher + chr((ord(char)+key-65) % 26 + 65)
        # checks lower case
        else:
            cipher = cipher + chr((ord(char)+key-97) % 26 + 97)

    return cipher

def decrypt(encoded, key):
    return encrypt(encoded, -key)

