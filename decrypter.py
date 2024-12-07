import os
import pyaes

def decrypt_file(encrypted_file_name: str, decryption_key: bytes):
    # Abrir o arquivo criptografado
    with open(encrypted_file_name, "rb") as file:
        encrypted_data = file.read()

    # Criar a instância de descriptografia
    aes = pyaes.AESModeOfOperationCTR(decryption_key)

    # Descriptografar os dados
    decrypted_data = aes.decrypt(encrypted_data)

    # Remover o arquivo criptografado
    os.remove(encrypted_file_name)

    # Salvar o arquivo descriptografado
    original_file_name = encrypted_file_name.replace(".encrypted", "")
    with open(original_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Arquivo descriptografado: {original_file_name}")

# Exemplo de uso
key = b"testeransomwares"  # Chave de 16 bytes
encrypted_file_name = "teste.txt.encrypted"

decrypt_file(encrypted_file_name, key)
