def procesar_vernam_27():
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #27 letras
    
    mensaje = input("Ingresa el mensaje a cifrar: ").upper().replace(" ", "")
    llave = input("Ingresa la llave: ").upper().replace(" ", "")
    
    # Repetir la llave
    llave_extendida = "".join([llave[i % len(llave)] for i in range(len(mensaje))])
        
    print(f"\nMensaje original:  {mensaje}")
    print(f"Llave (extendida): {llave_extendida}\n")

    cifrado_texto = ""
    print("--- Proceso XOR (Cifrado) ---")
    for i in range(len(mensaje)):
        val_msj = alfabeto.index(mensaje[i])
        val_llave = alfabeto.index(llave_extendida[i])
        
        # XOR y forzarlo a 27 caracteres con módulo
        val_xor = (val_msj ^ val_llave) % 27 
        
        cifrado_texto += alfabeto[val_xor]
        print(f"{mensaje[i]} ({val_msj:05b}) XOR {llave_extendida[i]} ({val_llave:05b}) = {alfabeto[val_xor]} ({val_xor:05b})")

    descifrado_texto = ""
    print("\n--- Proceso XOR (Descifrado) ---")
    for i in range(len(cifrado_texto)):
        val_cifrado = alfabeto.index(cifrado_texto[i])
        val_llave = alfabeto.index(llave_extendida[i])
        
        # XOR y forzarlo a 27 caracteres con módulo
        val_xor = (val_cifrado ^ val_llave) % 27
        
        descifrado_texto += alfabeto[val_xor]
        print(f"{cifrado_texto[i]} ({val_cifrado:05b}) XOR {llave_extendida[i]} ({val_llave:05b}) = {alfabeto[val_xor]} ({val_xor:05b})")

    print("\n=== RESULTADOS ===")
    print(f"Mensaje Cifrado:    {cifrado_texto}")
    print(f"Mensaje Descifrado: {descifrado_texto}")

procesar_vernam_27()