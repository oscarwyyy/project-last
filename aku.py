def brute_force_decrypt(ciphertext):
    # Mencoba semua shift dari 0 sampai 255
    for shift in range(256):
        decrypted_text = ''.join(chr((ord(c) - shift) % 256) for c in ciphertext)
        print(f"Shift {shift}: {decrypted_text}")

# Contoh ciphertext yang ingin didekripsi (misalnya dari teks yang sudah di-shift)
ciphertext = "Uifsf!J!xjmm!gvsufe!"  

# Menjalankan brute force dekripsi
brute_force_decrypt(ciphertext)
