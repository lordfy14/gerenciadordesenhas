# Gerenciador de Senhas

Este é um **gerenciador de senhas** simples desenvolvido em Python, que utiliza criptografia para garantir a segurança das senhas armazenadas. O projeto permite que você armazene e recupere suas senhas de maneira segura, utilizando a biblioteca `cryptography` para encriptação.

## Funcionalidades

- **Armazenamento seguro de senhas**: As senhas são criptografadas antes de serem salvas em um arquivo.
- **Recuperação de senhas**: Você pode recuperar senhas armazenadas de forma segura, após descriptografá-las.
- **Sistema de autenticação**: O sistema requer login para acessar as funções do gerenciador de senhas.

## Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: Para a interface gráfica.
- **Cryptography**: Para criptografar e descriptografar as senhas.
- **Git**: Para versionamento e controle de alterações no código.

## Instalação

Siga os passos abaixo para instalar e executar o projeto:

### 1. Clone o repositório

Para clonar o repositório, use o comando abaixo:

```
git clone https://github.com/lordfy14/gerenciadordesenhas.git
```

### 2. Crie um ambiente virtual

Recomenda-se criar um ambiente virtual para gerenciar as dependências do projeto. Para isso, execute os seguintes comandos:

```
cd gerenciadordesenhas
python -m venv .venv
```

### 3. Ative o ambiente virtual

No Windows, execute:

```
.venv\Scripts\activate
```

No Linux/MacOS, execute:

```
source .venv/bin/activate
```

### 4. Instale as dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```
pip install -r requirements.txt
```

### 5. Execute o projeto

Para executar o projeto, use o seguinte comando:

```
python main.py
```

Isso abrirá a interface gráfica onde você pode interagir com o gerenciador de senhas.

## Como Usar

1. Ao iniciar o aplicativo, será solicitado o **login**.
2. Após o login, você poderá:
   - **Adicionar uma nova senha**: Insira o serviço, o nome de usuário e a senha. A senha será criptografada e salva de forma segura.
   - **Recuperar uma senha**: Digite o nome do serviço e o sistema irá buscar a senha criptografada associada a ele e exibirá a senha descriptografada.

## Contribuição

Se você deseja contribuir para este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas alterações (`git checkout -b minha-branch`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin minha-branch`).
5. Crie um pull request.
