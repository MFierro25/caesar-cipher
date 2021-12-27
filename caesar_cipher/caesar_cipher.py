from caesar_cipher.corpus_loader import word_list, name_list


def encrypt(text, key):
    cipher = ''
    
    for char in text:

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

def crack(encoded):
    for i in range(26):
        total = 0
        message = encrypt(encoded, i)
        list = message.split()
        for text in list:
            if text in name_list or text.lower() in word_list:
                total += 1
        
        if (total / len(list)) > .5:
            return ' '.join(list)

    return ''
