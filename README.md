# Desafio Python - Integração com LLM (Groq)

Este projeto automatiza o processo de enviar perguntas para uma IA (Llama 3 via Groq API) e salvar as respostas em um arquivo CSV usando Pandas.

## 📋 Objetivos cumpridos:
1. Criar um arquivo `.txt` a partir de uma lista em Python.
2. Ler as perguntas do `.txt` e salvá-las em uma lista.
3. Obter respostas de um LLM para cada pergunta.
4. Salvar os resultados em um arquivo `.csv`.
5. Ler o arquivo `.csv` usando Pandas.

## 🚀 Como executar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure sua API Key:**
   Crie um arquivo `.env` na raiz do projeto e adicione sua chave da Groq:
   ```env
   GROQ_API_KEY=sua_chave_aqui
   ```

3. **Execute o script:**
   ```bash
   python app.py
   ```

## 🛠️ Tecnologias
- Python
- Pandas
- Groq Cloud API
- Python-dotenv
