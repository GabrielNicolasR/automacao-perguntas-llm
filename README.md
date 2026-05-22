# Automação de Perguntas com LLM (Groq API) | LLM Question Automation (Groq API)

[Português](#português) | [English](#english)

---

## Português

### Descrição
Este projeto automatiza o processo de gerar respostas para uma lista de perguntas pré-definidas utilizando a API do Groq (modelo Llama-3). O script lê as perguntas, consulta a IA para obter respostas curtas e diretas, e exporta o resultado final para um arquivo CSV.

### Funcionalidades
- **Leitura/Escrita:** Gerencia uma lista de perguntas em um arquivo de texto.
- **Integração com LLM:** Utiliza o modelo `llama-3.3-70b-versatile` via Groq Cloud.
- **Exportação:** Salva o par Pergunta/Resposta em um arquivo `resultado.csv` usando Pandas.

### Pré-requisitos
- Python 3.x
- Uma chave de API do [Groq](https://console.groq.com/)

### Instalação
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Crie um arquivo `.env` baseado no `.env.example` e adicione sua chave:
   ```env
   GROQ_API_KEY=sua_chave_aqui
   ```

### Como usar
Execute o script principal:
```bash
python app.py
```

---

## English

### Description
This project automates the process of generating answers for a predefined list of questions using the Groq API (Llama-3 model). The script reads the questions, queries the AI for short and direct answers, and exports the final result to a CSV file.

### Features
- **Read/Write:** Manages a list of questions in a text file.
- **LLM Integration:** Uses the `llama-3.3-70b-versatile` model via Groq Cloud.
- **Export:** Saves Question/Answer pairs into a `resultado.csv` file using Pandas.

### Prerequisites
- Python 3.x
- A [Groq](https://console.groq.com/) API Key

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on `.env.example` and add your key:
   ```env
   GROQ_API_KEY=your_key_here
   ```

### How to use
Run the main script:
```bash
python app.py
```
