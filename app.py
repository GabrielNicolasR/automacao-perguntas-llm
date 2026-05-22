import os
import pandas as pd
from dotenv import load_dotenv
from groq import Groq
from perguntas import LISTA_DE_PERGUNTAS


MODELO = "llama-3.3-70b-versatile"
ARQUIVO_TXT = "perguntas.txt"
ARQUIVO_CSV = "resultado.csv"

def configurar_cliente():
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("A variável GROQ_API_KEY não foi encontrada no arquivo .env")
    return Groq(api_key=api_key)

def preparar_arquivo_perguntas(perguntas, caminho):
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            for pergunta in perguntas:
                arquivo.write(pergunta + "\n")
    except Exception as e:
        print(f"Erro ao salvar arquivo de texto: {e}")

def carregar_perguntas_do_arquivo(caminho):
    lista = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            lista = [linha.strip() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
    return lista

def obter_respostas(client, lista_perguntas):
    resultados = []
    for pergunta in lista_perguntas:
        print(f"Processando: {pergunta}")
        try:
            completion = client.chat.completions.create(
                model=MODELO,
                messages=[
                    {"role": "system", "content": "Responda de forma extremamente curta e direta, em no máximo duas frases"},
                    {"role": "user", "content": pergunta}
                ],
                stream=False
            )
            resposta = completion.choices[0].message.content
            resultados.append({"Pergunta": pergunta, "Resposta": resposta})
        except Exception as e:
            print(f"Erro ao consultar a API para a pergunta '{pergunta}': {e}")
            resultados.append({"Pergunta": pergunta, "Resposta": "ERRO NA RESPOSTA"})
    return resultados

def salvar_csv(dados, caminho):
    df = pd.DataFrame(dados)
    df.to_csv(caminho, index=False, encoding="utf-8")
    print(f"\nResultados salvos com sucesso em: {caminho}")

def main():
    try:
        client = configurar_cliente()
        
        preparar_arquivo_perguntas(LISTA_DE_PERGUNTAS, ARQUIVO_TXT)
        perguntas_carregadas = carregar_perguntas_do_arquivo(ARQUIVO_TXT)
        
        if not perguntas_carregadas:
            print("Nenhuma pergunta para processar.")
            return

        dados_finais = obter_respostas(client, perguntas_carregadas)
        

        salvar_csv(dados_finais, ARQUIVO_CSV)
        
        print("\nVisualizando prévia dos resultados:")
        print(pd.read_csv(ARQUIVO_CSV))

    except Exception as e:
        print(f"Ocorreu um erro crítico no programa: {e}")

if __name__ == "__main__":
    main()
