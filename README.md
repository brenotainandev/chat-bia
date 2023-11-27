# Configuração do Projeto Chatbot (Bia) 🤖

A Bia é um chatbot desenvolvido para responder às perguntas dos clientes sobre os diversos produtos disponíveis na loja, incluindo fertilizantes, defensivos agrícolas, rações, equipamentos e sementes.

### Perguntas que a Bia Responderá:

1. Quais são os tipos de fertilizantes disponíveis na loja? 🌱
2. Vocês oferecem produtos para o controle de pragas e doenças nas plantações? 🐛🌿
3. Quais são as opções de ração para animais de criação que vocês têm disponíveis? 🐄🐖
4. Vocês vendem equipamentos agrícolas, como tratores e implementos? 🚜
5. Quais são as opções de sementes e mudas que posso encontrar na loja? 🌾🌻

Este repositório contém o código-fonte e a documentação para configurar o projeto Chatbot (Bia).

## Estrutura do Projeto 📁

O projeto está organizado da seguinte forma:

### `/backend` 🤖
Contém o código-fonte do backend do chatbot.

- `/conversas` 📂: Arquivos JSON
  - `informacoes.json`: Informações relevantes.
  - `saudacoes.json`: Saudações possíveis.
- `app.py`: Criação do serviço web.
- `main.py`: Arquivo principal do backend.
- `requirements.txt`: Dependências do backend.
- `teste_informacoes.py`: Testes unitários para informações.
- `teste_saudacao.py`: Testes unitários para saudações.

### `/frontend` 🌐
Contém o código-fonte do frontend do chatbot.

- `/src` 📂: Arquivos principais do frontend.
  - `App.js`: Arquivo principal do frontend.
  - `index.js`: Configuração do frontend.
- `package.json`: Dependências do frontend.

- `.gitignore`: Configurações de arquivos a serem ignorados pelo Git.

## Configuração do Ambiente Back-end

Para configurar o ambiente do backend do chatbot, siga os passos abaixo:

1. Certifique-se de ter o Python 3.8 instalado em sua máquina.
2. Clone este repositório em seu ambiente local.
3. Acesse a pasta `/backend` do projeto.
4. Crie um ambiente virtual executando o comando `python3.8 -m venv venv`.
5. Ative o ambiente virtual executando o comando `source venv/bin/activate`.
6. Instale as dependências do backend executando o comando `pip install -r requirements.txt`.
7. Execute o arquivo `python app.py` para iniciar o servidor web do backend.

## Configuração do Ambiente Front-end

Para configurar o ambiente do frontend do chatbot, siga os passos abaixo:

1. Certifique-se de ter o Node.js instalado em sua máquina.
   - Versão recomendada: 16.14.2 ou superior.
2. Clone este repositório em seu ambiente local.
3. Acesse a pasta `/frontend` do projeto.
4. Instale as dependências do frontend executando o comando `npm install`.
5. Execute o comando `npm start` para iniciar o servidor do frontend.

## Executando Testes Unitários

1. Navegue até a pasta `/backend` do projeto.
2. Ative o ambiente virtual. Se estiver usando venv, o comando será `source venv/bin/activate`.
3. Execute `python -m unittest teste_informacoes.py` para testar informações.
4. Execute `python -m unittest teste_saudacoes.py` para testar saudações.