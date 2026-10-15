def procesar_hill():
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" # 27 letras (incluye Ñ)
    
    # Matrices fijas precalculadas (llave y su inversa modular para mod 27)
    llave = [
        [1, 2, 1],
        [0, 1, 2],
        [2, 1, 1]
    ]
    
    inversa = [
        [16, 16, 6],
        [17, 16, 5],
        [5,   6, 11]
    ]
    
    print("--- Matriz Llave ---")
    for f in llave: print(f)
    print("\n--- Matriz Inversa ---")
    for f in inversa: print(f)
    
    mensaje = input("\nIngresa el mensaje a cifrar: ").upper().replace(" ", "")
    
    # Rellenar con 'X' para que sea múltiplo de 3
    while len(mensaje) % 3 != 0:
        mensaje += 'X'
        
    cifrado_texto = ""
    print("\n--- Proceso de Cifrado (Bloques de 3) ---")
    for i in range(0, len(mensaje), 3):
        # Convertir letras a índices
        letras = [mensaje[i], mensaje[i+1], mensaje[i+2]]
        vector = [alfabeto.index(l) for l in letras]
        
        # Multiplicación de matriz (Llave * Vector) mod 27
        v_cifrado = [0, 0, 0]
        for f in range(3):
            v_cifrado[f] = (llave[f][0]*vector[0] + llave[f][1]*vector[1] + llave[f][2]*vector[2]) % 27
            
        letras_cifradas = [alfabeto[idx] for idx in v_cifrado]
        cifrado_texto += "".join(letras_cifradas)
        
        print(f"Letras: {letras} -> Índices: {vector}  |X|  Llave -> Cifrados: {v_cifrado} -> Letras: {letras_cifradas}")

    descifrado_texto = ""
    print("\n--- Proceso de Descifrado (Bloques de 3) ---")
    for i in range(0, len(cifrado_texto), 3):
        letras = [cifrado_texto[i], cifrado_texto[i+1], cifrado_texto[i+2]]
        vector = [alfabeto.index(l) for l in letras]
        
        # Multiplicación de matriz (Inversa * Vector_Cifrado) mod 27
        v_desc = [0, 0, 0]
        for f in range(3):
            v_desc[f] = (inversa[f][0]*vector[0] + inversa[f][1]*vector[1] + inversa[f][2]*vector[2]) % 27
            
        letras_descifradas = [alfabeto[idx] for idx in v_desc]
        descifrado_texto += "".join(letras_descifradas)
        
        print(f"Letras: {letras} -> Índices: {vector}  |X|  Inversa -> Descifrados: {v_desc} -> Letras: {letras_descifradas}")

    print("\n=== RESULTADOS ===")
    print(f"Mensaje Original:   {mensaje}")
    print(f"Mensaje Cifrado:    {cifrado_texto}")
    print(f"Mensaje Descifrado: {descifrado_texto}")

procesar_hill()