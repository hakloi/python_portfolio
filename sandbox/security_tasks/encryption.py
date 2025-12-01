def letter_to_number(letter):
    return ord(letter) - ord('A')

def number_to_letter(number):
    return chr((number % 26) + ord('A'))

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    
    if len(key) < len(plaintext):
        raise ValueError("Key must be at least as long as the plaintext.")
    
    cipher_text = ""
    for p, k in zip(plaintext, key):
        p_num = letter_to_number(p)
        k_num = letter_to_number(k)
        cipher_num = (p_num + k_num) % 26
        cipher_text += number_to_letter(cipher_num)
    
    return cipher_text

plaintext = input("Enter plaintext (only capital letters A-Z): ").upper() 
key = input("Enter key (must be >= length of plaintext): ").upper()

cipher = encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Key:", key[:len(plaintext)])
print("Ciphertext:", cipher)
