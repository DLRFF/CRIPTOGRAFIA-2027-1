def cifrado_vigenere(mensaje, clave, encriptar=True):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""
    
    # Convertimos todo a mayúsculas para simplificar
    mensaje = mensaje.upper()
    clave = clave.upper()
    
    indice_clave = 0
    
    for caracter in mensaje:
        # Solo ciframos si es una letra (ignoramos espacios y números)
        if caracter in alfabeto:
            pos_letra = alfabeto.index(caracter)
            letra_clave = clave[indice_clave % len(clave)]
            pos_clave = alfabeto.index(letra_clave)
            
            # Sumamos las posiciones para cifrar, las restamos para descifrar
            if encriptar:
                nueva_pos = (pos_letra + pos_clave) % 26
            else:
                nueva_pos = (pos_letra - pos_clave) % 26
                
            resultado += alfabeto[nueva_pos]
            indice_clave += 1
        else:
            # Los espacios y signos de puntuación se quedan igual
            resultado += caracter
            
    return resultado


print("CIFRADO VIGENÈRE")
mensaje_usuario = input("Introduce el mensaje: ")
clave_usuario = input("Introduce la palabra clave: ")

# Cifrar
texto_cifrado = cifrado_vigenere(mensaje_usuario, clave_usuario, encriptar=True)
print(f"\nMensaje cifrado: {texto_cifrado}")

# Descifrar (para comprobar que funciona)
texto_descifrado = cifrado_vigenere(texto_cifrado, clave_usuario, encriptar=False)
print(f"Mensaje descifrado: {texto_descifrado}")