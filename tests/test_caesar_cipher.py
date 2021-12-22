from caesar_cipher.caesar_cipher import encrypt

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