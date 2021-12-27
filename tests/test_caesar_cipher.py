from caesar_cipher.caesar_cipher import decrypt, encrypt, crack

def test_encrypt_shift_1():
    actual = encrypt('car', 1)
    expected = "dbs"
    assert actual == expected

def test_encrypt_shift_5():
    actual = encrypt('car', 5)
    expected = 'hfw'
    assert actual == expected
    
def test_encrypt_upper():
    actual = encrypt('CAR', 1)
    expected = 'DBS'
    assert actual == expected
    
def test_encrypt_space():
    actual = encrypt('my one car', 1)
    expected = 'nz pof dbs'
    assert actual == expected
    
def test_non_alpha():
    actual = encrypt("Gimme 1 car!", 1)
    expected = "Hjnnf 1 dbs!"
    assert actual == expected
    
def test_decrypt():
    phrase = 'I Made this work!'
    shift = 2
    encrypted = encrypt(phrase, shift)
    
    actual = decrypt(encrypted, shift)
    expected = phrase
    assert actual == expected
    
def test_crack_phrase():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = phrase
    assert actual == expected


def test_crack_nonsense():
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = ""
    assert actual == expected