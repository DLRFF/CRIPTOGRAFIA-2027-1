msg = input("Ingrese el mensaje: ")
k = int(input("Llave: "))

abecedario = {chr(i + 97): i for i in range(26)}

msg_num = [abecedario[char] for char in msg]
msg_cifrado_num = [(abecedario[char] + k) % 26 for char in msg]
msg_cifrado_char = [chr(i+97) for i in msg_cifrado_num]


print(abecedario)

print(msg_num)
print(msg_cifrado_num)
print(msg_cifrado_char)