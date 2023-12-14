import openai
import dotenv
import os

def categoriza_produto(nome_produto, categorias_validas):

    prompt_sistema = f"""
    Você é um categorizador de produtos que mostra apenas o nome da categoria, sem necessidade de descrição.
    Você deve categorizar de acordo com a lista abaixo:
    {categorias_validas}
    """

    resposta = openai.chat.completions.create(
        model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt_sistema
                },
                {
                    "role": "user",
                    "content": nome_produto
                }
            ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    print(resposta.choices[0].message.content)

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

categorias_validas = input("Digite as categorias válidas: ")
continua ='S'

while continua == ('S' or 's'):
    nome_produto = input("Digite o nome do produto: ")
    categoriza_produto(nome_produto, categorias_validas)
    continua = input("Deseja continuar (S/s ou N/n)? ")