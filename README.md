# 👥 Projack Impulse — Microsserviço de Gestão de Colaboradores

> Microsserviço responsável pelo gerenciamento de colaboradores, solicitações de participação e equipes de projetos na plataforma **Projack Impulse**.

## 📌 Sobre o Microsserviço

O **Micro_Colaboradores** é um serviço independente desenvolvido em Python responsável por gerenciar a entrada, saída, listagem e requisições de colaboradores nos projetos.

Ele faz parte do ecossistema de microsserviços do **Projack Impulse** e lida diretamente com a camada de dados dos membros vinculados aos projetos.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12 (`runtime.txt`)
* **Framework Web:** Flask (`application.py`)
* **Banco de Dados:** SQLite (`meusistema.db`)
* **Camada de Dados:** DAO (`gerenciar_colaboradores/dao.py`)
* **Servidor de Produção:** Gunicorn (`startup.sh`)
* **CI/CD / Automação:** GitHub Actions (`main_aulaazuremack.yml`)

## 🏗️ Estrutura do Projeto

```text
Micro_Colaboradores-main/
│
├── .github/
│   └── workflows/
│       └── main_aulaazuremack.yml  # Workflow de CI/CD para deploy no Azure
│
├── database/                       # Módulo de conexão com o banco de dados
│   └── connection.py
│
├── gerenciar_colaboradores/        # Lógica de negócio e acesso a dados
│   ├── app.py                      # Rotas do módulo de colaboradores
│   └── dao.py                      # Data Access Object (consultas e manipulação no DB)
│
├── application.py                  # Ponto de entrada e servidor Flask
├── meusistema.db                   # Banco de dados SQLite
├── requirements.txt                # Dependências do projeto
├── runtime.txt                     # Versão do Python (3.12)
├── startup.sh                      # Script de inicialização (Gunicorn)
└── README.md                       # Documentação do microsserviço

```

## 🚀 Como Executar Localmente

### Pré-requisitos

* Python 3.12
* Git e pip

### 1. Clone o repositório e entre na pasta

```bash
git clone https://github.com/Fabricio-Alencar/Micro_Colaboradores.git
cd Micro_Colaboradores-main

```

### 2. Crie e ative um ambiente virtual

* **Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate

```


* **Windows:**
```bash
python -m venv venv
venv\Scripts\activate

```



### 3. Instale as dependências

```bash
pip install -r requirements.txt

```

### 4. Execute a aplicação

```bash
python application.py

```

Ou via script de inicialização:

```bash
bash startup.sh

```

## 🔗 Integração com o Ecossistema

Este microsserviço fornece os endpoints consumidos pelo Front-end do **Projack Impulse** para exibir colaboradores de um projeto, aceitar novos participantes e gerenciar a equipe.
