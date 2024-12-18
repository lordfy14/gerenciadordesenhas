import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

# Definir a fonte para a interface
font = ("Helvetica", 12)

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

# Função para salvar o usuário e senha criptografados
def save_user_credentials(username, password):
    encrypted_password = cipher.encrypt(password.encode())
    with open("users.txt", "a") as file:
        file.write(f"{username},{encrypted_password.decode()}\n")
    messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")

# Função para verificar as credenciais do usuário
def check_credentials(username, password):
    if not os.path.exists("users.txt"):
        return False

    with open("users.txt", "r") as file:
        for line in file:
            stored_username, encrypted_password = line.strip().split(",")
            if stored_username == username:
                decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
                if decrypted_password == password:
                    return True
    return False

# Função para exibir a tela de login
def login_window():
    login_screen = tk.Toplevel()
    login_screen.title("Tela de Login")
    login_screen.geometry("400x300")
    
    username_label = tk.Label(login_screen, text="Usuário:", font=font)
    username_label.pack(pady=10)
    username_entry = tk.Entry(login_screen, font=font, width=30, bd=2, relief="solid")
    username_entry.pack(pady=10)

    password_label = tk.Label(login_screen, text="Senha:", font=font)
    password_label.pack(pady=10)
    password_entry = tk.Entry(login_screen, font=font, width=30, bd=2, relief="solid", show="*")
    password_entry.pack(pady=10)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if check_credentials(username, password):
            login_screen.destroy()  # Fecha a tela de login
            password_manager_window()  # Abre a tela do gerenciador de senhas
        else:
            messagebox.showerror("Erro", "Credenciais inválidas. Tente novamente.")

    login_button = tk.Button(login_screen, text="Entrar", font=font, command=login, bg="#2196F3", fg="white", relief="flat", width=15)
    login_button.pack(pady=15)

    register_button = tk.Button(login_screen, text="Registrar Novo Usuário", font=font, command=register_window, bg="#FF9800", fg="white", relief="flat", width=20)
    register_button.pack(pady=10)

# Função para exibir a tela de registro de novo usuário
def register_window():
    register_screen = tk.Toplevel()
    register_screen.title("Registrar Novo Usuário")
    register_screen.geometry("400x300")
    
    username_label = tk.Label(register_screen, text="Usuário:", font=font)
    username_label.pack(pady=10)
    username_entry = tk.Entry(register_screen, font=font, width=30, bd=2, relief="solid")
    username_entry.pack(pady=10)

    password_label = tk.Label(register_screen, text="Senha:", font=font)
    password_label.pack(pady=10)
    password_entry = tk.Entry(register_screen, font=font, width=30, bd=2, relief="solid", show="*")
    password_entry.pack(pady=10)

    def register():
        username = username_entry.get()
        password = password_entry.get()

        if username and password:
            save_user_credentials(username, password)
            register_screen.destroy()
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

    register_button = tk.Button(register_screen, text="Registrar", font=font, command=register, bg="#2196F3", fg="white", relief="flat", width=15)
    register_button.pack(pady=15)

# Função para exibir a janela do gerenciador de senhas
def password_manager_window():
    password_manager_screen = tk.Toplevel()
    password_manager_screen.title("Gerenciador de Senhas")
    password_manager_screen.geometry("500x600")
    
    # Criar a interface do gerenciador de senhas (como já foi feito antes)
    frame = tk.Frame(password_manager_screen, bg="#ffffff", padx=20, pady=20)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Título da aplicação
    title_label = tk.Label(frame, text="Gerenciador de Senhas", font=font, bg="#ffffff", fg="#333333")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Criando os campos de entrada e rótulos
    tk.Label(frame, text="Serviço:", font=font, bg="#ffffff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    service_entry = tk.Entry(frame, font=font, width=30, bd=2, relief="solid")
    service_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    tk.Label(frame, text="Usuário:", font=font, bg="#ffffff").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    username_entry = tk.Entry(frame, font=font, width=30, bd=2, relief="solid")
    username_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    tk.Label(frame, text="Senha:", font=font, bg="#ffffff").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    password_entry = tk.Entry(frame, font=font, width=30, show="*", bd=2, relief="solid")
    password_entry.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    # Botões de ação
    save_button = tk.Button(frame, text="Salvar Senha", font=font, command=save_password, bg="#2196F3", fg="white", relief="flat", width=15)
    save_button.grid(row=4, column=0, columnspan=3, pady=15)

    retrieve_button = tk.Button(frame, text="Recuperar Senha", font=font, command=retrieve_password, bg="#FF9800", fg="white", relief="flat", width=15)
    retrieve_button.grid(row=5, column=0, columnspan=3, pady=15)

    result_text = tk.StringVar()
    result_label = tk.Label(frame, textvariable=result_text, font=("Helvetica", 10), bg="#ffffff", fg="#333333", justify="left")
    result_label.grid(row=6, column=0, columnspan=4, pady=10)

# Função para salvar a senha
def save_password(service, username, password):
    encrypted_password = cipher.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{service},{username},{encrypted_password.decode()}\n")
    messagebox.showinfo("Sucesso", f"Senha para {service} salva com sucesso!")

# Função para recuperar a senha
def retrieve_password(service):
    if not os.path.exists("passwords.txt"):
        messagebox.showinfo("Erro", "Nenhuma senha armazenada.")
        return

    with open("passwords.txt", "r") as file:
        for line in file:
            stored_service, username, encrypted_password = line.strip().split(",")
            if stored_service == service:
                decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
                messagebox.showinfo("Senha Encontrada", f"Serviço: {stored_service}\nUsuário: {username}\nSenha: {decrypted_password}")
                return
    messagebox.showinfo("Erro", f"Nenhuma senha encontrada para o serviço: {service}")

# Criando a tela de login diretamente
login_window()

# Rodar a interface gráfica
root = tk.Tk()
root.withdraw()  # Esconde a janela principal
root.mainloop()
