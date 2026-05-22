import os
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

lista_de_perguntas = [
    "O que é Inteligência Artificial?",
    "Qual a diferença entre Machine Learning e Deep Learning?",
    "Como criar um modelo simples usando Python?",
    "Para que serve a biblioteca scikit-learn?",
    "Como treinar uma IA com dados?"
]

with open("perguntas.txt", "w", encoding="utf-8") as arquivo :
    for pergunta in lista_de_perguntas:
        arquivo.write(pergunta + "\n")
        
nova_lista = []

with open("perguntas.txt", "r", encoding="utf-8") as arquivo :
    for linha in arquivo:
        nova_lista.append(linha.strip())
        
lista_de_respostas = []
        
for pergunta in nova_lista:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            { "role": "system", "content": "Responda de forma extremamente curta e direta, em no máximo duas frases"},
            
            { "role": "user", "content": pergunta}
        ],
        stream=False
    )
    resposta = completion.choices[0].message.content
    lista_de_respostas.append({
        "Pergunta": pergunta,
        "Resposta": resposta
    })
    
df_perguntas_e_respostas = pd.DataFrame(lista_de_respostas)

df_perguntas_e_respostas.to_csv("resultado.csv", index=False, encoding="utf-8")

novo_df = pd.read_csv("resultado.csv")
print(novo_df)