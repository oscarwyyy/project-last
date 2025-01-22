def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ''
    
    for char in plaintext:
        char_code = ord(char)
    
        shifted_char_code = (char_code + shift) % 256
        
        encrypted_text += chr(shifted_char_code)
    
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ''
    
    for char in ciphertext:
        char_code = ord(char)
        
        shifted_char_code = (char_code - shift) % 256
        
        decrypted_text += chr(shifted_char_code)
    
    return decrypted_text

shift = 5  
plaintext = "Hello"  

encrypted = caesar_cipher_encrypt(plaintext, shift)
print(f"Encrypted: {repr(encrypted)}")

decrypted = caesar_cipher_decrypt(encrypted, shift)
print(f"Decrypted: {repr(decrypted)}")
