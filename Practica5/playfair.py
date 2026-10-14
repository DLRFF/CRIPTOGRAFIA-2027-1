def generar_matriz(llave):
    # Limpiamos la llave: mayúsculas, quitamos espacios, cambiamos J por I
    llave = llave.upper().replace('J', 'I').replace(' ', '')
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # Sin la J
    matriz_plana = []
    
    # Agregar letras de la llave sin repetir
    for letra in llave:
        if letra not in matriz_plana and letra in alfabeto:
            matriz_plana.append(letra)
            
    # Agregar el resto del alfabeto
    for letra in alfabeto:
        if letra not in matriz_plana:
            matriz_plana.append(letra)
            
    # Convertir a matriz 5x5
    matriz = [matriz_plana[i:i+5] for i in range(0, 25, 5)]
    return matriz

def preparar_mensaje(mensaje):
    # Limpiar mensaje: mayúsculas, sin espacios, J por I
    mensaje = mensaje.upper().replace('J', 'I').replace(' ', '')
    preparado = ""
    i = 0
    
    # Separar en pares y agregar 'X' si hay letras repetidas juntas
    while i < len(mensaje):
        letra1 = mensaje[i]
        if i + 1 < len(mensaje):
            letra2 = mensaje[i+1]
            if letra1 == letra2:
                preparado += letra1 + 'X'
                i += 1 # Solo avanzamos uno
            else:
                preparado += letra1 + letra2
                i += 2 # Avanzamos el par
        else:
            # Letra suelta al final, agregamos 'X'
            preparado += letra1 + 'X'
            i += 1
            
    return preparado

def buscar_posicion(matriz, letra):
    # Buscar en qué fila y columna está una letra
    for f in range(5):
        for c in range(5):
            if matriz[f][c] == letra:
                return f, c
    return -1, -1

def procesar_playfair(mensaje, matriz, modo):
    resultado = ""
    # Si es cifrar sumamos 1 a la posición, si es descifrar restamos 1
    desplazamiento = 1 if modo == 'cifrar' else -1
    
    for i in range(0, len(mensaje), 2):
        l1, l2 = mensaje[i], mensaje[i+1]
        f1, c1 = buscar_posicion(matriz, l1)
        f2, c2 = buscar_posicion(matriz, l2)
        
        if f1 == f2: # Misma fila: mover a la derecha (o izquierda)
            resultado += matriz[f1][(c1 + desplazamiento) % 5]
            resultado += matriz[f2][(c2 + desplazamiento) % 5]
            
        elif c1 == c2: # Misma columna: mover abajo (o arriba)
            resultado += matriz[(f1 + desplazamiento) % 5][c1]
            resultado += matriz[(f2 + desplazamiento) % 5][c2]
            
        else: # Rectángulo: mantener fila, intercambiar columnas
            resultado += matriz[f1][c2]
            resultado += matriz[f2][c1]
            
    return resultado

#FLUJO PRINCIPAL
llave_input = input("Ingresa la llave para el cifrado Playfair: ")
mensaje_input = input("Ingresa el mensaje a cifrar: ")

matriz = generar_matriz(llave_input)
mensaje_listo = preparar_mensaje(mensaje_input)

print("\n--- Matriz 5x5 ---")
for fila in matriz:
    print(" ".join(fila))
print("------------------\n")

# Cifrar
texto_cifrado = procesar_playfair(mensaje_listo, matriz, 'cifrar')
print(f"Mensaje Cifrado:   {texto_cifrado}")

# Descifrar (a partir del texto cifrado)
texto_descifrado = procesar_playfair(texto_cifrado, matriz, 'descifrar')
print(f"Mensaje Descifrado: {texto_descifrado}")