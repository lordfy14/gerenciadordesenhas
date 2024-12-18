from cryptography.fernet import Fernet
import os

# Gerar ou carregar a chave de criptografia
def load_or_generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

key = load_or_generate_key()
cipher = Fernet(key)

# Função para salvar uma senha
def save_password(service, username, password):
    encrypted_password = cipher.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{service},{username},{encrypted_password.decode()}\n")
    print(f"Senha para {service} salva com sucesso!")

# Função para recuperar uma senha
def retrieve_password(service):
    if not os.path.exists("passwords.txt"):
        print("Nenhuma senha armazenada.")
        return

    with open("passwords.txt", "r") as file:
        for line in file:
            stored_service, username, encrypted_password = line.strip().split(",")
            if stored_service == service:
                decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
                print(f"Serviço: {stored_service}\nUsuário: {username}\nSenha: {decrypted_password}")
                return
    print(f"Nenhuma senha encontrada para o serviço: {service}")

# Menu principal
def main():
    while True:
        print("\nGerenciador de Senhas")
        print("1. Adicionar nova senha")
        print("2. Recuperar senha")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            service = input("Serviço: ")
            username = input("Usuário: ")
            password = input("Senha: ")
            save_password(service, username, password)
        elif choice == "2":
            service = input("Digite o nome do serviço: ")
            retrieve_password(service)
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
