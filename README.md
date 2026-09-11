<h1 align="center"> Portal do Aluno </h1>

<p align="center">
Projeto desenvolvido durante a disciplina de Redes de Computadores.
</p>

<p align="center">
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%EF%B8%8F-funcionalidades">Funcionalidades</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-fluxo-do-sistema">Fluxo do Sistema</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%EF%B8%8F-arquitetura-c4-model">Arquitetura (C4 Model)</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-licença">Licença</a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
  <img alt="Python" src="https://img.shields.io/static/v1?label=python&message=3.x&color=007bff&labelColor=000000">
  <img alt="Flask" src="https://img.shields.io/static/v1?label=flask&message=web&color=white&labelColor=000000">
</p>


<p align="center">
  <img alt="img" src="next.jpg" width="90%">
</p>

<br>

## 💻 Projeto

O Portal do Aluno é um sistema web de cadastro de estudantes desenvolvido para demonstrar na prática o funcionamento de uma aplicação full-stack, abordando conceitos de redes, servidores HTTP, autenticação e persistência de dados. O projeto simula um portal institucional com redirecionamento via `/etc/hosts`, servidor Flask e armazenamento seguro de credenciais em MySQL.

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Python
- Flask
- MySQL
- HTML e CSS
- Git e Github

## 🛠️ Funcionalidades

- **Cadastro de Alunos:** Registro de RA e senha com validação de campos obrigatórios.
- **Servidor Web Local:** Aplicação servida via Flask na porta 80 com suporte a arquivos estáticos.
- **Simulação de DNS:** Redirecionamento de domínio institucional via `/etc/hosts` para ambiente local.
- **Tratamento de Erros:** Feedback visual para RA duplicado, campos vazios e falhas de conexão.

## 🧭 Fluxo do Sistema

```mermaid
flowchart LR

A[Usuário acessa o domínio] --> B[/etc/hosts resolve para 127.0.0.1/]
B --> C[Flask serve o index.html]
C --> D[Usuário preenche RA e Senha]
D --> E[POST /login]
E --> F[Flask aplica SHA-256 na senha]
F --> G[INSERT no MySQL]
G --> H[Confirmação de Cadastro]
```

## 🏗️ Arquitetura (C4 Model)

### Contexto do Sistema

```mermaid
flowchart LR

U[Aluno] --> P[Portal do Aluno]
P --> DB[(Banco de Dados)]
P --> DNS[Resolução de Nomes]
P --> WEB[Servidor Web]
```

### Containers

```mermaid
flowchart LR

User[Usuário]
Frontend[Interface HTML/CSS]
Backend[Servidor Flask - Python]
DB[(MySQL)]

User --> Frontend
Frontend --> Backend
Backend --> DB
```

### Componentes

```mermaid
flowchart LR

API[API Flask]

Cadastro[Rota POST /login]
Static[Rota GET / e imagem]

DB[(Banco de Dados)]

API --> Cadastro
API --> Static

Cadastro --> DB
```

## 📂 Estrutura do Projeto

```
redes-computadores-dns/
├── app.py                          # Servidor Flask
├── index.html                      # Interface do portal
└── photo.jpg  # Imagem de fundo
```

## ▶️ Como Executar

**1. Instalar dependências**
```bash
pip install flask mysql-connector-python
```

**2. Criar o banco de dados**
```bash
mysql -u root -p < banco.sql
```

**3. Configurar a senha do MySQL em `app.py`**
```python
DB_CONFIG = {
    "password": "sua_senha"
}
```

**4. Adicionar o domínio ao `/etc/hosts`**
```
127.0.0.1   portal.unicap.br
```

**5. Iniciar o servidor**
```bash
sudo python3 app.py
```

Acesse: `http://portal.unicap.br`

## 📝 Licença

Esse projeto está sob a licença MIT.