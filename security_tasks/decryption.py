def letter_to_number(letter):
    return ord(letter) - ord('A')

def number_to_letter(number):
    return chr((number % 26) + ord('A'))

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    
    if len(key) < len(ciphertext):
        raise ValueError("Key must be at least as long as the ciphertext.")
    
    plaintext = ""
    for c, k in zip(ciphertext, key):
        c_num = letter_to_number(c)
        k_num = letter_to_number(k)
        p_num = (c_num - k_num + 26) % 26
        plaintext += number_to_letter(p_num)
    
    return plaintext

ciphertext = input("Enter ciphertext (only capital letters A-Z): ").upper()
key = input("Enter key (must be >= length of ciphertext): ").upper()

plaintext = decrypt(ciphertext, key)
print("Ciphertext:", ciphertext)
print("Key:", key[:len(ciphertext)])
print("Decrypted Plaintext:", plaintext)
