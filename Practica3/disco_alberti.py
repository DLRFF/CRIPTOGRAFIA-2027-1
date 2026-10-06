def alberti_cipher(text, key_shift=0, step=3):
    ext_disk = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    int_disk = "QWERTYUIOPASDFGHJKLZXCVBNMÑ"
    
    res = []
    shift = key_shift
    count = 0
    
    for ch in text.upper():
        if ch in ext_disk:
            idx = ext_disk.index(ch)
            new_idx = (idx - shift) % len(int_disk)
            res.append(int_disk[new_idx])
            count += 1
            if count % step == 0:
                shift = (shift + 1) % len(int_disk)
        else:
            res.append(ch)
            
    return "".join(res)


def alberti_decipher(text, key_shift=0, step=3):
    ext_disk = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    int_disk = "QWERTYUIOPASDFGHJKLZXCVBNMÑ"
    
    res = []
    shift = key_shift
    count = 0
    
    for ch in text:
        if ch in int_disk:
            idx = int_disk.index(ch)
            orig_idx = (idx + shift) % len(ext_disk)
            res.append(ext_disk[orig_idx])
            count += 1
            if count % step == 0:
                shift = (shift + 1) % len(int_disk)
        else:
            res.append(ch)
            
    return "".join(res)


msg = "Ataque al amanecer"
encrypted = alberti_cipher(msg, key_shift=4, step=3)
decrypted = alberti_decipher(encrypted, key_shift=4, step=3)

print("Original :", msg)
print("Cifrado  :", encrypted)
print("Descifrado:", decrypted)