import os
import openai
import dotenv
import tiktoken

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("./dados/lista_de_compras_10_clientes.csv")

codificador = tiktoken.encoding_for_model("gpt-3.5-turbo")

#descobrir a quantidade de tokens do contexto (entrada sistema, entrada usuario)
lista_de_tokens = codificador.encode(prompt_usuario + prompt_sistema)
numero_de_tokens = len(lista_de_tokens)
print(f"Número de tokens na entrada: {numero_de_tokens}")


#definir quel modelo usar baseado no numero de tokens (docs da openai)
modelo = "gpt-3.5-turbo"

#o total de tokens deve conter entrada-sistema e entrada-usuario e saida, neste caso 256 já estão reservados pelo
# max_tokens e precisa ser subtraido de 4096
if numero_de_tokens >= 3840:
    modelo = "gpt-3.5-turbo-16k"

print(f"Modelo Escolhido: {modelo}")

resposta = openai.ChatCompletion.create(
  model=modelo,
  messages=[
    {
      "role": "system",
      "content": prompt_sistema
    },
    {
      "role": "user",
      "content": prompt_usuario
    }
  ],
  temperature=1,
  #o max_tokens vai limitar tamanho de retorno. Independentemente da capacidade do modelo
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(resposta.choices[0].message.content)